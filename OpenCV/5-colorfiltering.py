import cv2
import numpy as np

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

# lower_blue = np.array([100,120,90])
# upper_blue = np.array([140,255,255])

lower_blue = np.array([105,150,120])
upper_blue = np.array([125,220,255])

while ret:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    # cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)
    cv2.imshow('filtered', res)

    # kernel =  np.ones((15,15), np.float32)/225
    # smoothed = cv2.filter2D(res, -1, kernel)
    # cv2.imshow('smoothed', smoothed)

    # blurred = cv2.GaussianBlur(res, (15,15), 0)
    # cv2.imshow('blurred', blurred)
    #
    # medianed = cv2.medianBlur(res, 15)
    # cv2.imshow('medianed', medianed)
    #
    # bilateral = cv2.bilateralFilter(res, 15, 75, 75)
    # cv2.imshow('bilateral', bilateral)

    ### MORPHOLOGICAL TRANSFORMATIONS ###

    # kernel = np.ones((3,3), np.uint8)
    # erosion = cv2.erode(mask, kernel, iterations=1)
    # dilation = cv2.dilate(mask, kernel, iterations=1)
    # cv2.imshow('erosion', erosion)
    # cv2.imshow('dilation', dilation)
    #
    # opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    # closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    # cv2.imshow('opening', opening)
    # cv2.imshow('closing', closing)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
