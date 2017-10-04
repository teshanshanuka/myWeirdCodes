print("Incomplete")

import cv2
import numpy as np

I = cv2.imread('img.jpg', 0)
unique, counts = np.unique(I, return_counts = True)
hst = dict(zip(unique, counts))

cdf = np.cumsum(counts)/I.size

hsteq = np.round(cdf*255)
idx = np.array([int(np.where(unique==i)[0]) for i in hsteq])

I_eq = np.array()

cv2.imshow('img', I)
# press any key to exit
cv2.waitKey(0)
cv2.destroyAllWindows()
