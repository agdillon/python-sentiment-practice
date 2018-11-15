# list of stuff I changed from tutorial because it didn't make sense to me:
# from time import sleep --- unnecessary?  never used anywhere
# analysis = TextBlob(tweet.text).sentiment --- they had an extra line for no reason
# number += 1 --- they had number = number + 1, meh
# except StopIteration: break --- redundant with the for loop ending, I think

import config
api_key = config.api_key
api_secret = config.api_secret
access_token = config.access_token
token_secret = config.token_secret

import tweepy
from datetime import datetime
from textblob import TextBlob

# auth and setup for Twitter API
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, token_secret)
api = tweepy.API(auth)

# hardcode for now, want to get this data from form on frontend (post route)
search_term = 'python'
number_of_tweets = 50

# polarity_list is a list of sentiment polarity of each different tweet
polarity_list = []

for tweet in tweepy.Cursor(api.search, search_term, lang='en').items(number_of_tweets):
    try:
        analysis = TextBlob(tweet.text).sentiment
        polarity = analysis.polarity
        polarity_list.append(polarity)

    except tweepy.TweepError as e:
        print(e.reason)

timestamp = datetime.now().strftime('%c')

response_dictionary = {}
response_dictionary['number_of_tweets'] = number_of_tweets
response_dictionary['polarity_list'] = polarity_list
response_dictionary['timestamp'] = timestamp

print(response_dictionary)
