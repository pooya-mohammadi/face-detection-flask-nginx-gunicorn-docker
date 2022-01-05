import os
from werkzeug.datastructures import FileStorage
from service import Inference
from flask import Flask
from flask_restful import Api, reqparse

# define the app and the api variables
ENDPOINT = os.getenv('ENDPOINT', '/face')
# HOST = "0.0.0.0"
app = Flask(ENDPOINT)
api = Api(app)

PORT_NUMBER = int(os.getenv('PORT_NUMBER', 8080))

# get debugging mode condition, default is True:
debugging = os.getenv("DEBUGGING", 'True').lower() in ('true', '1', 't')
print(f"[INFO] debugging mode is set to: {debugging}")
# load the model and weights
FACE_DETECTION_MODEL = os.getenv('FACE_DETECTION_MODEL', 'MTCNNTorchFaceDetector')

# The addresses for weights go here
if FACE_DETECTION_MODEL == "MTCNNTorchFaceDetector":
    rnet = '/app/weights/rnet.npy'
    onet = '/app/weights/onet.npy'
    pnet = '/app/weights/pnet.npy'
    model_configs = dict(rnet=rnet, onet=onet, pnet=pnet)
    print(f"[INFO] Face detection mode is set to {FACE_DETECTION_MODEL}")
else:
    # The configs of models other than mtcnn go here
    model_configs = dict()
    print(
        f"[INFO] the configs for model:{FACE_DETECTION_MODEL} is set to {model_configs}."
        f" If it's empty, the deep_utils library will use the defaults configs and most surely will download "
        f"the weights each time you run the dockerfile ")

inference = Inference(FACE_DETECTION_MODEL, **model_configs)
POST_TYPE = os.getenv("POST_TYPE", "FORM")

# set global variables
app.config['inference'] = inference
app.config['POST_TYPE'] = POST_TYPE

# file Parser arguments. Only Form is implemented
app.config['PARSER'] = reqparse.RequestParser()
app.config['PARSER'].add_argument('image',
                                  type=FileStorage,
                                  location='files',
                                  required=True,
                                  help='provide an image file')
