import os

from ast import literal_eval


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

    def save(self):
        """
        This method saves video to static folder
        :return:
        """
        if not self._is_allowed_extension():
            success = False
        else:
            self._video.save(os.path.join("static", self._video.filename))
            success = True

        return success, self._video.filename

    def get_objects(self):
        """
        This method converts data from permanent txt file to list of results
        :return: List
        """
        with open('result.txt') as file:
            for line in file.readlines():
                self._objects.append(literal_eval(line))

        os.remove('result.txt')

        return self._objects
