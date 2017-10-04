import cv2
import numpy as np

img = cv2.imread("img.jpg", cv2.IMREAD_COLOR)
#IMREAD_COLOR=1
#IMREAD_GRAYSCALE=0
#IMREAD_UNCHANGED=-1
# cv2.imshow("orig_image", img)

pylogo = cv2.imread('mainlogo.png', cv2.IMREAD_COLOR)
# cv2.imshow("pylogo", pylogo)
rows, cols, channels = pylogo.shape
roi = img[0:rows, 0:cols]

pylogo2gray = cv2.cvtColor(pylogo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(pylogo2gray, 220, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow("mask", mask)

mask_inv = cv2.bitwise_not(mask)
img_bg = cv2.bitwise_and(roi, roi, mask=mask_inv) #background
pylogo_fg = cv2.bitwise_and(pylogo, pylogo, mask=mask) # foreground

dst = cv2.add(img_bg, pylogo_fg)
img[0:rows, 0:cols] = dst
cv2.imshow('img', img)
# press any key to exit
cv2.waitKey(0)
cv2.destroyAllWindows()
