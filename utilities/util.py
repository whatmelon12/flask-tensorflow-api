import io
import numpy as np
import cv2 

class Util:
    ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])

    @classmethod
    def allowed_file(cls, fileName):
        return '.' in fileName and fileName.rsplit('.', 1)[1].lower() in cls.ALLOWED_EXTENSIONS
    
    @staticmethod
    def get_file_np_array(file):
        '''Converts a buffer from a file in np.array
        '''
        return np.asarray(bytearray(file.read()))
    
    @staticmethod
    def decode_to_opencv(file):
        in_memory = io.BytesIO()
        file.save(in_memory)
        data = np.fromstring(in_memory.getvalue(), dtype=np.uint8)
        color_image_flag = 1
        img = cv2.imdecode(data, color_image_flag)
        return img