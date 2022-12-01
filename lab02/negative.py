import numpy as np
import cv2

img = cv2.imread('flowers.jpg', 0)

img_neg = 255-img                                  # s = L - 1 - r

cv2.namedWindow('flower', cv2.WINDOW_NORMAL)
cv2.imshow('flower', img)

cv2.namedWindow('flower_neg', cv2.WINDOW_NORMAL)
cv2.imshow('flower_neg', img_neg)

cv2.waitKey(0)
cv2.destroyAllWindows()