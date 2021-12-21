from endpoints import FaceDetection
from base_app import app, api, ENDPOINT, HOST, PORT_NUMBER

api.add_resource(FaceDetection, ENDPOINT)

if __name__ == '__main__':
    app.run(HOST, port=PORT_NUMBER)
