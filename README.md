# Face-Detection-flask-gunicorn-nginx

This is a simple demonstration of dockerized face-detection API which is implemented with flask and nginx and scaled
with gunicorn.

# Notes

1. For face-detection, I used pytorch version of mtcnn from deep_utils library. For more information check
   out [deep_utils](https://github.com/pooya-mohammadi/deep_utils).
2. The service is scaled up using gunicorn. The gunicorn is a simple library with high throughput for scaling python services.
    1. To increase the number workers, increase number of `workers` in the `docker-compose.yml` file.
    2. For more information about gunicorn workers and threads check the following stackoverflow question
    3. [gunicorn-workers-and-threads](https://stackoverflow.com/questions/38425620/gunicorn-workers-and-threads)
3. nginx is used as a reverse proxy

# Setup

1. The face-detection name in docker-compose can be changed to any of the models available by deep-utils library.
2. For simplicity, I placed the weights of the mtcnn-torch model in app/weights.
3. To use different face-detection models in deep_utils, apply the following changes:
    1. Change the value of `FACE_DETECTION_MODEL` in the `docker-compose.yml` file.
    2. Modify configs of a new model in `app/base_app.py` file.
    3. It's recommended to run the new model in your local system and acquire the downloaded weights from `~/.deep_utils`
       directory and place it inside `app/weights` directory. This will save you tons of time while working with models with
       heavy weights.
    4. If your new model is based on `tensorflow`, comment the `pytorch` installation section in `app/Dockerfile` and
       uncomment the `tensorflow` installation lines.

# ScaleUp

I scaled the project using gunicorn

# RUN

To run the API, install `docker` and `docker-compose`, execute the following command:

## windows

`docker-compose up --build`

## Linux

`sudo docker-compose up --build`

# Inference

To send an image and get back the boxes run the following commands:
`curl --request POST ip:port/endpoint -F image=@img-add`

If you run the service on your local system the following request shall work perfectly:

```terminal
curl --request POST http://127.0.0.1:8000/face -F image=@./sample-images/movie-stars.jpg
```

# Issues

If you find something missing, please open an issue or kindly create a pull request.  

# References

1.https://github.com/pooya-mohammadi/deep_utils

# Licence

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at: http://www.apache.org/licenses/LICENSE-2.0.

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

See the License for the specific language governing permissions and limitations under the License.
