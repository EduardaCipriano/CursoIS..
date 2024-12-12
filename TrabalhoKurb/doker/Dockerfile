WORKDIR /app

COPY . /app/

RUN apt-get update && apt-get install -y \
    libglib2.0-0 libsm6 libxrender1 libxext6 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip install --no-cache-dir \
    six==1.16.0 \
    is-wire==1.2.1 \
    is-msgs==1.1.18 \
    opencv-python-headless \
    numpy==1.24.4

RUN mkdir -p ./data/images

CMD ["python", "sub_imgs.py"]

