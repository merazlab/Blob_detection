import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
img_clr = cv2.imread("./dataset/test1.jpg", 1)
img = cv2.cvtColor(img_clr, cv2.COLOR_BGR2GRAY)

# Denoising the image
img = cv2.fastNlMeansDenoising(img, None, 10, 10, 5)


# Define blob detector
parm = cv2.SimpleBlobDetector_Params()

# Blob detector parameter
parm.filterByArea = True
parm.minArea = 50
parm.maxArea = 10000

parm.filterByCircularity = True
parm.minCircularity = 0.2
parm.maxCircularity = 1

parm.filterByConvexity = True
parm.minConvexity = 0.1
parm.maxConvexity = 1

parm.filterByInertia = True
parm.minInertiaRatio = 0
parm.maxInertiaRatio = 1

parm.minThreshold = 0
parm.maxThreshold = 150

parm.filterByColor = False  
parm.blobColor = 0

parm.minDistBetweenBlobs = 0

# Initialise blob parameter
detector = cv2.SimpleBlobDetector_create(parm)

# Blob detection 
keypoints = detector.detect(img)


predicted_blobs = cv2.drawKeypoints(img, keypoints, np.array([]), (255, 0, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
print("Total no of blobs detected-{}".format(len(keypoints)))

Hori = np.concatenate((img_clr, predicted_blobs), axis=1)

cv2.imshow('HORIZONTAL', Hori)
cv2.imwrite("./output/output1.jpg", Hori)


cv2.waitKey(0)
cv2.destroyAllWindows()
