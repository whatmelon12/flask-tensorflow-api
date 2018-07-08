import os
import tensorflow as tf
import numpy as np
import cv2

class ImageClassifier:

    def __init__(self, image):
        self.image = image
        self.RETRAINED_LABELS_TXT_FILE_LOC = os.getcwd() + "/tensor/" + "retrained_labels.txt"
        self.RETRAINED_GRAPH_PB_FILE_LOC = os.getcwd() + "/tensor/" + "retrained_graph.pb"
        self.TEST_IMAGES_DIR = os.getcwd() + "/tensor/test_images"

    def getImageScore(self):                
        breeds = []

        # for currentLine in tf.gfile.GFile(self.RETRAINED_LABELS_TXT_FILE_LOC):
        #     breed = currentLine.rstrip()
        #     breeds.append(breed)
        with open(self.RETRAINED_LABELS_TXT_FILE_LOC, 'r') as fbreed:
            breeds = [ x.strip('\n').split(' ', 1) for x in fbreed.readlines() ]
            
        with tf.gfile.FastGFile(self.RETRAINED_GRAPH_PB_FILE_LOC, 'rb') as retrainedGraphFile:
            graphDef = tf.GraphDef()
            graphDef.ParseFromString(retrainedGraphFile.read())
            tf.import_graph_def(graphDef, name='')
        
        with tf.Session() as sess:             
            finalTensor = sess.graph.get_tensor_by_name('final_result:0')

            tfImage =  np.array(self.image)[:, :, 0:3]

            scores = sess.run(finalTensor, {'DecodeJpeg:0': tfImage})
            breedIndexArray = scores[0].argsort()[-len(scores[0]):][::-1][:5]
            result = [ { 'breed': { 'id': breeds[index][0], 'name': breeds[index][1] }, 'score': scores[0][index] * 100 } for index in breedIndexArray ]
            
            return result