from detectron2.utils.logger import setup_logger

# import common libraries
import cv2

# import detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.data import MetadataCatalog


setup_logger()


class DetectionService:
    def __init__(self, filename, cpu_count):
        self._filename = filename
        self._cfg = self.setup_cfg()
        self._predictor = DefaultPredictor(self._cfg)
        self._class_catalog = MetadataCatalog.get(self._cfg.DATASETS.TRAIN[0]).thing_classes
        self.cpu_count = cpu_count

    @staticmethod
    def setup_cfg():
        cfg = get_cfg()
        # add project-specific config (e.g., TensorMask) here if you're not running a model in detectron2's core library
        cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
        cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # set threshold for this model
        # Find a model from detectron2's model zoo. You can use the https://dl.fbaipublicfiles... url as well
        cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")
        cfg.MODEL.DEVICE = 'cpu'

        return cfg

    def _get_scores_from_instances(self, instances):
        detected_class_indexes = instances.pred_classes
        scores = instances.scores

        results = []
        for idx, score in enumerate(scores):
            class_index = detected_class_indexes[idx]
            class_name = self._class_catalog[class_index]
            results.append({class_name: round(score.item(), 2)})

        return results

    def _read_frames(self, processed_video):
        max_frames = 5
        frames = 0

        while True:
            has_frame, image = processed_video.read()

            if not has_frame:
                break

            predictions = self._predictor(image)
            instances = predictions.get('instances')
            results = self._get_scores_from_instances(instances)

            with open('result.txt', 'a') as file:
                file.write(str(results) + '\n')

            frames += 1
            if frames >= max_frames:
                break

        processed_video.release()

    def process_frames(self, group_number, processed_video):
        total_frames = processed_video.get(cv2.CAP_PROP_FRAME_COUNT)
        frames_per_cpu = total_frames / self.cpu_count
        processed_video.set(cv2.CAP_PROP_POS_FRAMES, frames_per_cpu * group_number)

        self._read_frames(processed_video)