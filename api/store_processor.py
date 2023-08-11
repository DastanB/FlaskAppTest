import os
import cv2
import asyncio

# import multiprocessing utilities
from multiprocessing import cpu_count, Pool

from api.services.detection_service import DetectionService


def store_objects(group_number, filename):
    processed_video = cv2.VideoCapture(f'{os.path.join("static", filename)}')
    if not processed_video.isOpened():
        return

    service = DetectionService(filename, cpu_count())
    return service.process_frames(group_number, processed_video)


def main(filename):
    with Pool(cpu_count()) as pool:
        multiple_results = []

        for i in range(cpu_count()):
            multiple_results.append(pool.apply_async(store_objects, (i, filename)).get())

    return multiple_results
