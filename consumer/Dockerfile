FROM python:3.7-slim

ENV PYTHONDONTWRITEBYTECODE=1

COPY consumer .
RUN pip install -r consumer_requirements.txt

CMD ["python3", "-u", "./consumer.py"]
