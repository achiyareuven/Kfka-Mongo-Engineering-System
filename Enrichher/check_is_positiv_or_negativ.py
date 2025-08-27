import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


r = {"op":"hhcdhjhb","rtyt":"retrfc","Text":"is the data good or bed"}


class Enricher:
    def __init__(self,data:dict):
        self.data = data

    def is_positive_or_negative(self, tweet):
        nltk.download('vader_lexicon')
        score = SentimentIntensityAnalyzer().polarity_scores(tweet)
        print(score)
        # if score >= 0.5:
        #     return "positive"
        # if score < -0.5:
        #     return "negative"
        # else:
        #     return "normal"


    def check_the_score(self):
        self.data["score"] = self.data["Text"].apply(self.is_positive_or_negative)



e = Enricher(r)
print(e.check_the_score())