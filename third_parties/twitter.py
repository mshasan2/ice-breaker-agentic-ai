import os
from dotenv import load_dotenv
import tweepy
import requests

load_dotenv()

twitter_client = tweepy.Client(
    bearer_token=os.getenv("TWITTER_BEARER_TOKEN"),
    consumer_key=os.getenv("TWITTER_API_KEY"),
    consumer_secret=os.getenv("TWITTER_API_SECRET_KEY"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
)

def scrape_user_tweets(username, num_tweets=5, mock=False):
    """
    Scrapes a user's original tweets from Twitter/X.

    Args:
        username (str): The Twitter username to scrape.
        num_tweets (int): The number of tweets to scrape.
        mock (bool): If True, returns a mock response instead of scraping.

    Returns:
        list: A list of tweets from the user's timeline.
    """
    tweet_list = []

    if mock:
        mock_tweets_url = "https://gist.githubusercontent.com/mshasan2/c0549e133fe1911472ba3c271384ca20/raw/c98d42f1db69c059c14e6debd9bf23f220cba316/mshasan2-tweets.json"
        tweets = requests.get(mock_tweets_url, timeout=10).json()

    else:
        user_id = twitter_client.get_user(username=username).data.id
        tweets = twitter_client.get_users_tweets(
            id=user_id,
            max_results=num_tweets,
            exclude=["replies", "retweets"]
        )
        tweets = tweets.data

    for tweet in tweets:
        tweet_dict = {}
        tweet_dict["text"] = tweet["text"]
        tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet['id']}"
        tweet_list.append(tweet_dict)

    return tweet_list




if __name__ == "__main__":
    tweets = scrape_user_tweets(username="elonmusk", num_tweets=5, mock=True)
    print(tweets)