from flask import Flask, request, Response, jsonify
import logging
from io import BytesIO
from PIL import Image
import base64


app = Flask(__name__)
logging.basicConfig(filename = 'logs/all-logs.log')


@app.route("/")
def hello_world():
    app.logger.info('Someone trying to access Hello World!')
    return jsonify(message = "A HostedAPI to test your requests!")

@app.route('/image', methods = ["POST"])
def receive_image():
    if "image" not in request.files:
        return jsonify(
            error= "Please attach the image in the 'image' attribute of the request!"
        ), 400
    image_file = request.files["image"]
    image_bytes = BytesIO(image_file.read())
    image = Image.open(image_bytes)
    # do something with image

    # Sending image back as response
    img_response = base64.encodebytes(image_bytes.getvalue()).decode('ascii')
    
    # Return the image with additional json attributes
    return jsonify(
        processed_image = img_response,
        message = "Processed the image!"
    )

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify(error = "Request method disallowed on the api. Please check your request and try again!"), 405
