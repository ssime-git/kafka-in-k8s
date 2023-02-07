from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
import faker
from datetime import datetime
import logging
import time

logging.basicConfig(level=logging.INFO)


class Producer:

    def __init__(self):
        self._init_kafka_producer()

    def _init_kafka_producer(self):
        self.kafka_host = "kafka-local.kafkaplaypen.svc.cluster.local:9092" # kafka-local.kafkaplaypen.svc.cluster.local
        self.kafka_topic = "my-topic"
        self.producer = KafkaProducer(

            bootstrap_servers=self.kafka_host, value_serializer=lambda v: json.dumps(v).encode(),
            api_version=(0, 10, 1)

        )

    def publish_to_kafka(self, message):
        try:
            self.producer.send(self.kafka_topic, message)
            self.producer.flush()

        except KafkaError as ex:

            logging.error(f"Exception {ex}")
        else:
            logging.info(f"Published message {message} into topic {self.kafka_topic}")

    @staticmethod
    def create_random_email():
        f = faker.Faker()

        new_contact = dict(
            username=f.user_name(),
            first_name=f.first_name(),
            last_name=f.last_name(),
            email=f.email(),
            date_created=str(datetime.utcnow()),
        )

        return new_contact


if __name__ == "__main__":
    producer = Producer()
    while True:
        random_email = producer.create_random_email()
        producer.publish_to_kafka(random_email)

        time.sleep(5)
