from flask import Flask, request, abort, jsonify
from utilities.util import Util
from tensor.image_classifier import ImageClassifier

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World Flask API!"

@app.route('/api/test/post', methods=['POST'])
def api_post():
    if not request.json:
        abort(400)
    return jsonify({'response': request.json})

@app.route('/api/uploadtest', methods=['POST'])
def test_image():
    if 'image' not in request.files:
        return jsonify({'error': 'Image file not sent'}), 400

    file = request.files['image']

    if file and Util.allowed_file(file.filename):

        classifier = ImageClassifier(Util.decode_to_opencv(file))
        return jsonify(classifier.getImageScore())

    return jsonify({ 'error': 'Unsupported file extension' }), 400

@app.route('/api/dogbreeds', methods=['GET'])
def getDogBreeds():
    classifier = ImageClassifier(None)
    return jsonify(classifier.getImageClasses())


if __name__ == '__main__':
    app.run(debug=True)