FROM python:3.11-slim

COPY . /app
WORKDIR /app

RUN pip install requests

CMD ["python3", "req.py"]

# docker build . --tag test_requests:0
# docker run test_requests:0 -d 