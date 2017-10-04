import cv2
import numpy as np

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

while ret:
    ret, frame = cap.read()
    cv2.imshow('orig', frame)

    # laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    # cv2.imshow('laplacian', laplacian)
    #
    # sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    # sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    # cv2.imshow('sobelx', sobelx)
    # cv2.imshow('sobely', sobely)

    edges = cv2.Canny(frame, 150, 200)
    cv2.imshow('Canny edges', edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
