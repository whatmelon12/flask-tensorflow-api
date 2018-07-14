import io
import numpy as np
import cv2 

class Util:
    """
    Util class containing miscellanius functions to handle validation and data processing.
    """
    ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])

    @classmethod
    def allowed_file(cls, fileName):
        """
        This function validates the extension of an input file to a list of allowed extensions.
        Allowed extensions are .jpg and .jpeg.
        """
        return '.' in fileName and fileName.rsplit('.', 1)[1].lower() in cls.ALLOWED_EXTENSIONS
    
    @staticmethod
    def get_file_np_array(file):
        """
        Converts a buffer from a file in np array.
        """
        return np.asarray(bytearray(file.read()))
    
    @staticmethod
    def decode_to_opencv(file):
        """
        Decodes Flask's filestorage object (that is internally an image) into an OpenCV image.
        """
        in_memory = io.BytesIO()
        file.save(in_memory)
        data = np.fromstring(in_memory.getvalue(), dtype=np.uint8)
        color_image_flag = 1
        img = cv2.imdecode(data, color_image_flag)
        return img