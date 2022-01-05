from endpoints import FaceDetection
from base_app import app, api, ENDPOINT

api.add_resource(FaceDetection, ENDPOINT)

if __name__ == '__main__':
    app.run("127.0.0.1", port=3000)
