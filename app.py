import logging
from flask import Flask, render_template, request, jsonify, make_response
from summary import *

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        url = request.form.get('url')
        language = request.form.get('language')

        summary = summarize_article(url, language)

        # return jsonify(summarized_text=summary)

        response = make_response(jsonify(summarized_text=summary))
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response

    except Exception as e:
        logging.exception("Error while summarizing the article:")
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)
