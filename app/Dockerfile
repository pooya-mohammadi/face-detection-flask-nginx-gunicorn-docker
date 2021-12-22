FROM python:3.9.7-buster


LABEL author="Pooya Mohammadi Kazaj <https://github.com/pooya-mohammadi>"

# os and opencv libraries
RUN apt-get update -y \
  && apt install libgl1-mesa-glx -y \
  && apt-get install 'ffmpeg' 'libsm6' 'libxext6'  -y \
  && python -m pip install --no-cache-dir --upgrade pip

# fixed python libraries for pytorch models
RUN pip install --no-cache-dir torch==1.10.0+cpu torchvision==0.11.1+cpu \
  -f https://download.pytorch.org/whl/torch_stable.html \
  && pip install --no-cache-dir numpy==1.21.4 \
  && pip install --no-cache-dir opencv-python==4.5.4.58 \
  && pip install --no-cache-dir deep_utils==0.8.8 \
  && pip install --no-cache-dir scikit-learn==1.0.1 \
  && pip install --no-cache-dir matplotlib==3.4.3 \
  && pip install --no-cache-dir pandas==1.3.4 \
  && rm -rf /root/.cache/pip

# fixed python libraries for tensorflow models
# RUN pip install --no-cache-dir tensorflow==2.7.0 \
#   && pip install --no-cache-dir numpy==1.21.4 \
#   && pip install --no-cache-dir opencv-python==4.5.4.60 \
#   $$ pip install --no-cache-dir deep_utils==0.8.8 \
#   && rm -rf /root/.cache/pip

# Add new python libraries here or to requirements.txt
# RUN pip install --no-cache-dir <python-package>

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD gunicorn --workers=2 -b 0.0.0.0:660 entry_point:app --worker-class sync
