FROM python:3.10-slim

WORKDIR /app

COPY pubImg.py .
COPY requirements.txt .
COPY images.jpeg .

run pip install -r requirements.txt

CMD ["python", "pubImg.py"]
