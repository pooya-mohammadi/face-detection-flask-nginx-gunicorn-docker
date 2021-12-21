import sys
from flask import jsonify
from flask_restful import Resource
from base_app import app
from deep_utils import b64_to_img
import cv2
import numpy as np


class FaceDetection(Resource):
    @staticmethod
    def post():
        args = app.config['PARSER'].parse_args()
        contents = args['image']
        if app.config['POST_TYPE'] == 'JSON':
            image = b64_to_img(contents)
        elif app.config['POST_TYPE'] == 'FORM':
            image = np.array(bytearray(contents.read()), dtype=np.uint8)
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        else:
            print(f"[ERROR] POST_TYPE:{app.config['POST_TYPE']} is not valid!, exiting ...")
            sys.exit(1)
        res = app.config['inference'].infer(image)
        return res

    @staticmethod
    def get():
        """
        Bug test
        :return: some text
        """
        return jsonify({"Just": "Fine!"})
