import numpy as np
from deep_utils import face_detector_loader, Box, img_to_b64
from flask import jsonify


class Inference:
    def __init__(self, model_name, **model_config):
        self.detector = face_detector_loader(model_name, **model_config)

    @staticmethod
    def preprocessing(img) -> np.ndarray:
        if type(img) is not np.ndarray:
            img = np.array(img).astype(np.uint8)
        return img

    def infer(self, img):
        img = self.preprocessing(img)
        objects = self.detector.detect_faces(img, is_rgb=False)
        faces = dict()
        boxes = objects['boxes']
        if boxes and len(boxes[0]):
            images = Box.get_box_img(img, boxes)
            faces = {f"face_{i}": [int(b) for b in box] for i, box in enumerate(boxes, 1)}
        return jsonify(faces)
