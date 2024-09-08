from flask import Flask
import logging


app = Flask(__name__)
logging.basicConfig(filename = 'logs/info.log', level = logging.INFO)
logging.basicConfig(filename = 'logs/debug.log', level = logging.DEBUG)
logging.basicConfig(filename = 'logs/error.log', level = logging.ERROR)


@app.route("/")
def hello_world():
    app.logger.info('Someone trying to access Hello World!')
    return "<p>Hello, world!</p>"
