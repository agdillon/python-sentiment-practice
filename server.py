from flask import Flask, request, jsonify
app = Flask(__name__)

import os
is_prod = os.getenv('IS_HEROKU')

if is_prod:
    port = os.getenv('PORT')
else:
    port = 5000

import analysis

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

@app.route('/', methods=['POST'])
def submit():
    json_data = request.get_json(force=True)
    search_term = json_data['search_term']
    number_of_tweets = int(json_data['number_of_tweets'])
    # error handling might be nice
    return jsonify(analysis.analyze_tweets(search_term, number_of_tweets))
