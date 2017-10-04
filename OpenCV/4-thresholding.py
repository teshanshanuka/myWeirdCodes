# http://docs.opencv.org/trunk/d7/d4d/tutorial_py_thresholding.html

import cv2
import numpy as np

img = cv2.imread("img.jpg", cv2.IMREAD_COLOR)

ret, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, greythreshold = cv2.threshold(grayscaled, 100, 255, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

ret, otsu = cv2.threshold(grayscaled, 100, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('orig', img)
# cv2.imshow('thesh',threshold)
# cv2.imshow('grey',greythreshold)
cv2.imshow('gaus',gaus)
# cv2.imshow('otsu',otsu)


cv2.waitKey(0)
cv2.destroyAllWindows()
