from flask import Flask, jsonify, request

from api.services.get_result_service import GetResultService
from api.store_processor import main as store_processor

api = Flask(__name__)


@api.route('/objects/', methods=['POST'])
def get_objects_api():
    if not request.files or not request.files.get('video'):
        return jsonify({'error': 'Video was not provided.'}), 400

    service = GetResultService(request.files.get('video'))
    success, filename = service.save()

    if not success:
        return jsonify({'error': 'Wrong file format.'}), 400

    results = store_processor(filename)

    return jsonify({'results': results}), 200
