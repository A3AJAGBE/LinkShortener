from flask import Flask, render_template, request
import os
import requests
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

BITLY_KEY = os.environ.get('BITLY_KEY')
BITLY_ENDPOINT = os.environ.get('BITLY_ENDPOINT')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form['long_url']

        HEADERS = {
            "Authorization": f"Bearer {BITLY_KEY}"
        }

        PARAMETERS = {
            "long_url": long_url
        }

        response = requests.post(BITLY_ENDPOINT, json=PARAMETERS, headers=HEADERS)
        data = response.json()
        short_link = data['link']
    return render_template('index.html', short_url=short_link)


if __name__ == '__main__':
    app.run(debug=True)