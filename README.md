# python-sentiment-practice
My Unfamiliar Environments exercise: a basic Twitter sentiment analysis app in Python, partially based on the tutorial here: https://medium.freecodecamp.org/basic-data-analysis-on-twitter-with-python-251c2a85062e

Written in Python 3.7.  Packages needed: tweepy, textblob, flask

Note: As of Nov 14 2018 there is a bug in the tweepy package due to its use of async as a parameter name (async is now a reserved word in Python 3.7).  Therefore I took the advice at this issue page and replaced all instances of async in tweepy's streaming.py with async_: https://github.com/tweepy/tweepy/issues/1017
