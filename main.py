#
# Tweepyを使ってみる
#
import dotenv, os, json
import tweepy

def main():
    # load environmental variables from .env
    dotenv.load_dotenv()

    # prepare
    consumer_key = os.getenv("CLIENT_ID")
    consumer_secret = os.getenv("CLIENT_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # call API Endpoints
    api = tweepy.API(auth)
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)
  
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Ctrl+C")
        exit(0)