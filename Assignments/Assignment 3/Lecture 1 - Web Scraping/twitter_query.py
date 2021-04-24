import tweepy
import json
import sys
from tweepy.error import TweepError

def get_tweets(username, N = 1):
  tweets1 = []
  tweets2 = api.user_timeline(username, count = N, include_rts=False)
  tweets3 = api.user_timeline(username, include_rts=False)
  number = N
  while len(tweets2) < N < len(tweets3):
    number += 1
    tweets2 = api.user_timeline(username, count = number, include_rts=False)
  for t in tweets2:
      tweets1.append((t.created_at.strftime("%Y-%m-%d"), t.text))

  return tweets1


if __name__ == "__main__":
    with open('credentials.json', 'r') as infile:
        data = json.load(infile)

    auth = tweepy.OAuthHandler(data['consumer_key'], data['consumer_secret'])
    auth.set_access_token(data['access_token'], data['access_token_secret'])

    api = tweepy.API(auth)
    count = None

    if len(sys.argv) == 2:
        user = sys.argv[1]
    elif len(sys.argv) == 3:
        user = sys.argv[1]
        count = int(sys.argv[2])
    else:
        print("usage: python3 twitter_query.py USERNAME (COUNT)")
        exit()

    try:
        if count:
            tweets = get_tweets(user, N = count)
        else:
            tweets = get_tweets(user)
        for t in tweets:
            print(t[0], t[1])
    except TweepError:
        print('Sorry, there is no such user on Twitter.')






