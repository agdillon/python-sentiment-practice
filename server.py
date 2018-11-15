from flask import Flask, url_for, request, jsonify
app = Flask(__name__)

import analysis

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

@app.route('/', methods=['POST'])
def submit():
    json_data = request.get_json(force=True)
    search_term = json_data['search_term']
    # error handling might be nice
    return jsonify(analysis.analyze_tweets(search_term, 100))
