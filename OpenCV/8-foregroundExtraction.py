import cv2
import numpy as np
# import matplotlib.pyplot as plt

img = cv2.imread('p1.jpg')
drawImg = np.copy(img)
ix, iy = -1, -1
drawing = False
rect = [0,0,0,0]

def drawRect(event,x,y,flags,param):
    global ix,iy,drawing,rect
    if event == cv2.EVENT_LBUTTONUP:
        if drawing:
            cv2.rectangle(drawImg, (ix, iy), (x, y), (0,255,255), 2)
            rect = [ix, iy, x, y]
            drawing = False
        else:
            ix,iy = x,y
            drawing = True

cv2.namedWindow('orig')
cv2.setMouseCallback('orig',drawRect)

print('press c to continue with the last selection...')
while(1):
    cv2.imshow('orig',drawImg)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        raise SystemExit
    if k == ord('c'):
        break

mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1,65), np.float64)
fgdModel = np.zeros((1,65), np.float64)

cv2.grabCut(img, mask, tuple(rect), bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0), 0, 1).astype(np.uint8)
img = img*mask2[:,:,np.newaxis]

#http://docs.opencv.org/trunk/d8/d83/tutorial_py_grabcut.html
# Unfinished code
# def drawCircle(event,x,y,flags,param):
#     global ix,iy,drawing,rect
#     if event == cv2.EVENT_LBUTTONUP:
#         if drawing:
#             cv2.rectangle(drawImg, (ix, iy), (x, y), (0,255,255), 2)
#             rect = [ix, iy, x, y]
#             drawing = False
#         else:
#             ix,iy = x,y
#             drawing = True
#
# cv2.setMouseCallback('orig',drawCircle)
#
# print('Draw foreground. Press f to continue')
# while(1):
#     cv2.imshow('orig',img)
#     k = cv2.waitKey(20) & 0xFF
#     if k == 27:
#         raise SystemExit
#     if k == ord('c'):
#         break


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.colorbar()
# plt.grid()
# plt.show()
