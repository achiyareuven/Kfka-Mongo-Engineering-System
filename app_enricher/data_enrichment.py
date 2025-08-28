import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.data.path.append("./docker_enricher/Enrichher/vader_lexicon/vader_lexicon.txt")
nltk.data.path.append("./nltk_data")
from datetime import datetime
import os
from dotenv import load_dotenv
from comman_utils.processor import TextProcessor

load_dotenv()


class Enricher:
    def __init__(self,message:dict):
        self.message = message
        self.clean_data = message["cleaned_text"]
        self.dirty_data = message["text"]
        self.path = os.getenv("PATH_TO_WEAPONS_LIST")
        with open(self.path)as file:
            self.weapons_string = file.read()
        self.prossor = TextProcessor(self.weapons_string)

    def is_positive_or_negative(self):
        nltk.download('vader_lexicon')
        score = SentimentIntensityAnalyzer().polarity_scores(self.clean_data)["compound"]
        print(score)
        if score >= 0.5:
            return "positive"
        if score < -0.5:
            return "negative"
        else:
            return "normal"


    def check_if_their_is_weapons(self):
        weapons_clean = self.prossor.process_all_and_get()
        print(weapons_clean)
        list_of_weapons = []
        for weapon in weapons_clean:
            if weapon in self.clean_data:
                list_of_weapons.append(weapon)
        return list_of_weapons


    def find_the_latest_date(self):
        list_of_dates = []
        for word in self.dirty_data.split(" "):
            try:
                date_obj = datetime.strptime(word, "%d-%m-%y")
                list_of_dates.append(date_obj)
            except ValueError:
                pass
        if len(list_of_dates) == 0:
            return "their not datas"
        return max(list_of_dates)


    def start_all_function_on_every_data(self):
        self.message["sentiment"] = self.is_positive_or_negative()
        self.message["detected_weapons"] = self.check_if_their_is_weapons()
        self.message["timestamp_relevant"] = self.find_the_latest_date()


