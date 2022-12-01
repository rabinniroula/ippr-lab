import numpy as np
import cv2

cv2.namedWindow('flower', cv2.WINDOW_NORMAL)
img = cv2.imread('flowers.jpg', 1)
cv2.imshow('flower', img)
cv2.waitKey(0)
cv2.destroyAllWindows()