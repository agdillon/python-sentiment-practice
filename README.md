# python-sentiment-practice
My Unfamiliar Environments exercise: a basic full-stack Twitter sentiment analysis app, partially based on the tutorial here: https://medium.freecodecamp.org/basic-data-analysis-on-twitter-with-python-251c2a85062e  Backend is Python 3.7/Flask and uses Tweepy and TextBlob for NLP.

Note: The latest release version 3.6.0 of Tweepy is incompatible with Python 3.7 due to its use of async as a parameter name (async is now a reserved word).  This is fixed in the code at https://github.com/tweepy/tweepy/, so this version of the package needs to be used.
