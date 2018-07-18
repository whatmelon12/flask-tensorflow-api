# Welcome to Dog Breed - Flask Tensor Flow API!

This project implements a RESTful API using **Flask**, a python web framework, to analize an input image using a **Tensor Flow** graph, and return its score based on the **120 dog breeds** that were used to train the last layer of the [**Inception Model V3**](https://github.com/tensorflow/models/tree/master/research/inception) provided by Google.

## Dependencies

The two main dependencies of the project are the [Tensor Flow](https://www.tensorflow.org/) library, and [OpenCV](https://opencv.org/) a library to handle images.

To install all dependencies of this projects run the following command:
    
    pip install -r requirements.txt

Python 3.6.6 is required to run this project.

## Run the project

Execute the `app.py` file from the console to start the Flask API.

|Endpoint Path|Method|Body Type|Returns
|--|--|--|--|
|api/dogbreeds|GET|None|List of available dog breeds
|api/uploadtest|POST|Multipart Form (image)|Analysis result

> **Note:** A live version of this project is available at [https://breed-classifier.herokuapp.com/](https://breed-classifier.herokuapp.com/)