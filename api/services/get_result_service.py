import os

import cv2


class GetResultService:
    """
    This service is designed to store input video and
    extract results from permanent txt file
    """
    def __init__(self, video):
        self._video = video
        self._allowed_extension = 'mp4'
        self._objects = []

    def _is_allowed_extension(self):
        return self._video.filename.split('.')[-1] == self._allowed_extension

    @staticmethod
    def _is_allowed_duration(filename):
        video = cv2.VideoCapture(f'{os.path.join("static", filename)}')
        duration = int(video.get(cv2.CAP_PROP_FRAME_COUNT)) / video.get(cv2.CAP_PROP_FPS)
        if duration > 5:
            # no more than 5 sec
            os.remove(os.path.join("static", filename))
            return False

        return True

    def save(self):
        """
        This method saves video to static folder
        :return:
        """
        if not self._is_allowed_extension():
            success = False
            response = 'Not allowed extension.'
        else:
            success = True
            response = ''
            self._video.save(os.path.join("static", self._video.filename))

        if not self._is_allowed_duration(self._video.filename):
            success = False
            response = 'Duration of the video is more than 5 sec.'

        return success, response, self._video.filename
