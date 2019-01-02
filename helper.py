import cv2
import numpy as np
import matplotlib.image as mpimg

class Helper(object):
    @staticmethod
    def read_img(input_image):
        img = mpimg.imread(input_image)
        res = cv2.resize(img, dsize=(28, 28), interpolation=cv2.INTER_CUBIC)
        res = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
        return res.reshape(1, 28, 28, 1)
