from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Helllo, Link Shortener!!!'


if __name__ == '__main__':
    app.run(debug=True)