def analyze_tweets(search_term, number_of_tweets):
    import os
    is_prod = os.environ.get('IS_HEROKU', None)

    if is_prod:
        api_key = os.environ.api_key
        api_secret = os.environ.api_secret
        access_token = os.environ.access_token
        token_secret = os.environ.token_secret

    else:
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

    # polarity_list is a list of sentiment polarity of each different tweet
    polarity_list = []

    for tweet in tweepy.Cursor(api.search, search_term, lang='en').items(number_of_tweets):
        try:
            analysis = TextBlob(tweet.text).sentiment
            polarity = analysis.polarity
            polarity_list.append(polarity)

        except tweepy.TweepError as e:
            # should send this error back as response
            print(e.reason)

    timestamp = datetime.now().strftime('%c')

    response_dictionary = {}
    response_dictionary['search_term'] = search_term
    response_dictionary['number_of_tweets'] = number_of_tweets
    response_dictionary['polarity_list'] = polarity_list
    response_dictionary['timestamp'] = timestamp

    return response_dictionary
