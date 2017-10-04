import cv2
import numpy as np

img = cv2.imread("img.jpg", cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (255,255,255), 10)
cv2.rectangle(img, (550,550), (800,900), (0,255,0), 5)
cv2.circle(img, (img.shape[1]//2,img.shape[0]//3), 50, (255,0,0), -1)
pts = np.array([[20,80],[60,40],[110,100],[90,200],[40,90]], np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,0,255), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV Teting FU', (img.shape[1]//3,img.shape[0]//3), font, 2, (0,255,255), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows
