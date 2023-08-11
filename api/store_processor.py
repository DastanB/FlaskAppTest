# import common libraries
import os
import cv2
import sys

# import multiprocessing utilities
from multiprocessing import Pool, cpu_count

from api.services import DetectionService


def store_objects(group_number, filename):
    processed_video = cv2.VideoCapture(f'{os.path.join("static", filename)}')
    if not processed_video.isOpened():
        return

    service = DetectionService(filename, cpu_count())
    service.process_frames(group_number, processed_video)


def main(filename):
    with Pool(cpu_count()) as pool:
        pool.starmap(store_objects, [(i, filename) for i in range(cpu_count())])
