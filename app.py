# This app is partially based on the tutorial at
# https://medium.freecodecamp.org/basic-data-analysis-on-twitter-with-python-251c2a85062e
# Note: I had to modify tweepy code because of use of async keyword, see issue at
# https://github.com/tweepy/tweepy/issues/1017

# list of stuff I changed because it didn't make sense to me:
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

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, token_secret)

api = tweepy.API(auth)

# hardcode for now, want to get this data from form on frontend (post route)
search_term = 'python'
number_of_tweets = 50

# polarity_list is a list of sentiment of different tweets, numbers_list is
# just a corresponding list of numbers 1 through number_of_tweets, for graphing
# purposes (which seems goofy, why not just make a range)
polarity_list = []
numbers_list = []
number = 1

for tweet in tweepy.Cursor(api.search, search_term, lang='en').items(number_of_tweets):
    try:
        analysis = TextBlob(tweet.text).sentiment
        polarity = analysis.polarity
        polarity_list.append(polarity)
        numbers_list.append(number)
        number += 1

    except tweepy.TweepError as e:
        print(e.reason)

# construct JSON response containing: number of tweets, polarity_list,
# date and time of analysis, average polarity?
# console.log it for now, then set up server layer
