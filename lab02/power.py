#Demonstrates power transformation also known as gamma transformation

import numpy as np
import cv2

"""
    s = c * (r^y)
"""

img = cv2.imread('flowers.jpg', 0)
gamma = 2.2

img_pow = 255 * (img / 255)**gamma
img_pow = np.array(img_pow, dtype = np.uint8) # convert float to uint8

cv2.namedWindow('flower', cv2.WINDOW_NORMAL)
cv2.imshow('flower', img)

cv2.namedWindow('flower_pow', cv2.WINDOW_NORMAL)
cv2.imshow('flower_pow', img_pow)

cv2.waitKey(0)
cv2.destroyAllWindows()