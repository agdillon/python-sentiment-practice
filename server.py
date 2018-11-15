from flask import Flask
app = Flask(__name__)

import analysis

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

# @app.route('/', methods=['POST'])
# going to be used for ajax only, so just send back json
# request.form.search_term
# analysis.analyze_tweets('0', 0)
