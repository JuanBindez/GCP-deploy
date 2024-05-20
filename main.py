import os

from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS


load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['DEBUG'] = os.environ.get('FLASK_DEBUG')

@app.route('/')
def hello():
    return "olá, seu deploy esta OK!"

if __name__ == "__main__":
    app.run()