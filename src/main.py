import os
import io
from tensor.image_classifier import ImageClassifier

def main():
   filepath = os.getcwd() + "/tensor/retrained_labels.txt"
   file = open(filepath, 'r')
   breeds = [ x.strip('\n').split(' ', 1) for x in file.readlines() ]
   print(breeds)

if __name__ == '__main__':
    main()