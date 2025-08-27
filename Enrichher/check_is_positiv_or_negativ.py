import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

r = {"text":"is the data good or bed 1970-01-87 1960-02-89 gun arrow uivishui ujfbk 123588","clean_data":"gyudsgh syug sy 1970-01-87 1960-02-89 gxgjys guysg guysgf "}


class Enricher:
    def __init__(self,message:dict):
        self.message = message
        self.clean_data = message["clean_data"]
        self.dirty_data = message["text"]
        self.path = os.getenv("PATH_TO_WEAPONS_LIST")
        with open(self.path)as file:
            self.weapons_list = file.read().split("\n")

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
        list_of_weapons = []
        for weapon in self.weapons_list:
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


e = Enricher(r)
e.start_all_function_on_every_data()
# print(e.is_positive_or_negative())
# print(e.find_the_latest_date())
# print(e.check_if_their_is_weapons())
print(e.message)