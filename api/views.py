from flask import Flask, jsonify, request
from ast import literal_eval
import os

from api.services import SaveVideoService
from api.store_processor import main as store_processor

api = Flask(__name__)


@api.route('/objects/', methods=['POST'])
def get_objects_api():
    if not request.files or not request.files.get('video'):
        return jsonify({'error': 'video was not provided'}), 400

    service = SaveVideoService(request.files.get('video'))
    success, filename = service.save()

    if not success:
        return jsonify({'error': 'video formar is incorrect'}), 400

    store_processor(filename)

    objects = []
    with open('readme.txt') as file:
        for line in file.readlines():
            objects.append(literal_eval(line))

    os.remove('readme.txt')

    return jsonify({'result': objects}), 200
