from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from utilities.util import Util
from tensor.image_classifier import ImageClassifier

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    """
    '/' Index route of Flask API.
    """
    return "Hello World TensorFlow Flask API - Dog Breeds Classifier! v1.0"

@app.route('/api/uploadtest', methods=['POST'])
def test_image():
    """
    '/api/uploadtest' POST endpoint to send image and Multipart data form request content
    for the TensorFlow graph to analize.
    """
    if 'image' not in request.files:
        return jsonify({'error': 'Image file not sent'}), 400

    file = request.files['image']

    if file and Util.allowed_file(file.filename):

        classifier = ImageClassifier(Util.decode_to_opencv(file))
        return jsonify(classifier.getImageScore())

    return jsonify({ 'error': 'Unsupported file extension' }), 400

@app.route('/api/dogbreeds', methods=['GET'])
def getDogBreeds():
    """
    '/api/dogbreeds' GET endpoint to obtain a list of all recognizable dog breeds by the TensorFlow 
    agent.
    """
    classifier = ImageClassifier(None)
    return jsonify(classifier.getImageClasses())


if __name__ == '__main__':
    app.run(debug=True)