from flask import Flask
import logging

app = Flask(__name__)
logging.basicConfig(filename='server_side.log', level=logging.INFO)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
