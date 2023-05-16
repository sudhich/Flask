from flask import Flask
import logging as logger
logger.basicConfig(level=logger.DEBUG)

app = Flask(__name__)

if __name__ == '__main__':
    logger.debug("Starting the application")
    from api import *
    app.run(debug=True)
