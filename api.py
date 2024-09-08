from flask import Flask, request, Response
import logging
from io import BytesIO
from PIL import Image
import base64


app = Flask(__name__)
logging.basicConfig(filename = 'logs/all-logs.log')


@app.route("/")
def hello_world():
    app.logger.info('Someone trying to access Hello World!')
    return "<p>Hello, world!</p>"

@app.route('/image', methods = ["POST"])
def receive_image():
    image_file = request.files["image"]
    image_bytes = BytesIO(image_file.read())
    image = Image.open(image_bytes)
    # do something with image

    # Sending image back as response
    img_response = base64.encodebytes(image_bytes.getvalue()).decode('ascii')
    
    # Return the image with additional json attributes
    return {
        "processed_image" : img_response
    }
