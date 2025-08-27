import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


r = {"op":"hhcdhjhb","rtyt":"retrfc","Text":"is the data good or bed"}


class Enricher:
    def __init__(self,data:dict):
        self.data = data

    def is_positive_or_negative(self, tweet):
        nltk.download('vader_lexicon')
        score = SentimentIntensityAnalyzer().polarity_scores(tweet)["compound"]
        print(score)
        if score >= 0.5:
            return "positive"
        if score < -0.5:
            return "negative"
        else:
            return "normal"


    def check_the_score(self):
        new_data = self.is_positive_or_negative(self.data["Text"])
        self.data["score"] = new_data

    def check_if_their_is_weapons

e = Enricher(r)
print(e.check_the_score())