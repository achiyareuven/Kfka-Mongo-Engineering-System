from comman_utils.consumer_interface import Consumer
from data_enrichment import Enricher
from comman_utils.producer_interface import Producer
import os
from dotenv import load_dotenv


load_dotenv()


class Manager_the_enricher:
    topic_read_anti = os.getenv("TOPIC_CLEAN_ANTISEMITIC")
    topic_read_not_anti =os.getenv("TOPIC_CLEAN_NOT_ANTISEMITIC")
    group = os.getenv("GROUP_NAME_ENRICHER")

    topic_send_anti =os.getenv("TOPIC_ENRICHED_ANTISEMITIC")
    topic_send_not_anti =os.getenv("TOPIC_ENRICHED_NOT_ANTISEMITIC")
    def __init__(self):

        self.consumer = Consumer(self.topic_read_anti,self.topic_read_not_anti,self.group)
        self.producer = Producer()

    def enrich_the_data_and_send_to_kafka(self):
        for msg in self.consumer.get_consumer_events():
            print(msg.value,msg)
            enricher = Enricher(msg.value)
            enricher.start_all_function_on_every_data()
            msg.value = enricher.message
            print(enricher.message)
            if msg.topic == self.topic_read_anti:
                producer_topic = self.topic_send_anti
            elif msg.topic  == self.topic_read_not_anti:
                producer_topic = self.topic_send_not_anti
            else:
                continue
            self.producer.publish_message(producer_topic,msg.value)
            print(type(msg.value))
            print(f"Message sent to topic {producer_topic}")


meneger = Manager_the_enricher()
meneger.enrich_the_data_and_send_to_kafka()