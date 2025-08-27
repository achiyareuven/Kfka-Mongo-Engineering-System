from commen.concumer_clean_txt import Consumer
from check_is_positiv_or_negativ import Enricher
from commen.producer_antisemitic_and_not import Producer

class Manager_the_enricher:
    def __init__(self):
        self.consumer = Consumer()
        self.enricher = Enricher()
        self.producer = Producer()

    def
