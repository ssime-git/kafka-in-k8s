FROM python:3.7-slim

ENV PYTHONDONTWRITEBYTECODE=1

#RUN pip3 install kafka-python
#RUN pip3 install faker

# copy everything in producer folder
COPY producer .
RUN pip install -r requirements.txt


CMD ["python3", "-u", "./producer.py"]
