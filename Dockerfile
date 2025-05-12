FROM python:3.9-alpine

RUN pip install flask prometheus_client

COPY app.py .

CMD ["python", "app.py"]
