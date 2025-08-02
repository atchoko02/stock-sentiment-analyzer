import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from data import reddit_scraper as scraper
from datetime import datetime, timezone

# removes noise, combines title and text
def clean_text(txt: str):
    txt = txt.lower()
    txt = re.sub(r'http\S+|www\S+|https\S+', '', txt, flags=re.MULTILINE)  # remove URLs
    txt = re.sub(r'[^a-zA-Z0-9\s$]', '', txt)  # remove special characters
    txt = re.sub(r'\s+', ' ', txt).strip()  # remove extra whitespace
    return txt

# gets sentiment score using VADER
def get_sentiment_score(text: str):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    return score['compound']

# classifies sentiment based on the score
def classify_sentiment(score: float):
    if score >= 0.05:
        return 'positive'
    elif score <= -0.05:
        return 'negative'
    else:
        return 'neutral'

# Analyzes sentiment of reddit posts about a stock
def analyze_sentiment(posts: list[dict]):
    df = pd.DataFrame(posts)
    df['cleaned_text'] = (df['title'] + ' ' + df['text']).apply(clean_text)
    df['sentiment_score'] = df['cleaned_text'].apply(get_sentiment_score)
    df['sentiment_label'] = df['sentiment_score'].apply(classify_sentiment) 
    df['date'] = df['date'].apply(lambda ts: datetime.fromtimestamp(ts, tz=timezone.utc).date())

    sentiment_daily = df.groupby('date').agg({
        'score': 'mean'
    }).reset_index()
    sentiment_daily.rename(columns={'score': 'sentiment_score', 'date': 'Date'})
    return sentiment_daily

def 