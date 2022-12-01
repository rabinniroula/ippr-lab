import numpy as np
import cv2

"""
    s = c * log(1 + r)
    c = 255 / (log(1 + max_value))
"""

img = cv2.imread('flowers.jpg', 0)

max_pixel = np.max(img)
c = 255 / np.log(1 + max_pixel)
img_log = c * np.log(img + 1)
img_log = np.array(img_log, dtype = np.uint8) # convert float to uint8

cv2.namedWindow('flower', cv2.WINDOW_NORMAL)
cv2.imshow('flower', img)

cv2.namedWindow('flower_neg', cv2.WINDOW_NORMAL)
cv2.imshow('flower_neg', img_log)

cv2.waitKey(0)
cv2.destroyAllWindows()