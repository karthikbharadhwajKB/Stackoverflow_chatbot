from flask import Flask
from dotenv import load_dotenv

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/drinks')
def get_drinks():
    return {"drinks": ["coffee", "tea", "water"]}


if __name__ == '__main__':
    load_dotenv()
