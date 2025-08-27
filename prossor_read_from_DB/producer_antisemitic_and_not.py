from kafka import KafkaProducer
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Producer config
class Producer:

    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=[os.getenv("ADDRESS")],
            value_serializer=lambda x: json.dumps(x).encode('utf-8')
        )
        print(self.producer.config)

# producer send message
    def publish_message(self, topic, message):
        self.producer.send(topic, value=message)
        self.producer.flush()


