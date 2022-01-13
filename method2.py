import cv2
import numpy as np
import matplotlib.pyplot as plt

# load image
img_clr = cv2.imread("./dataset/test1.jpg", 1)
img = cv2.cvtColor(img_clr, cv2.COLOR_BGR2GRAY)

ret1, thresh = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

blur = cv2.GaussianBlur(thresh, (11,11), 0)
canny = cv2.Canny(blur, 30, 150, 3)
dilated = cv2.dilate(canny, (1,1), iterations = 2)
contour, _ = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

rgb = cv2.cvtColor(img_clr, cv2.COLOR_BGR2RGB)
cv2.drawContours(rgb, contour, -1, (255,0, 0), 1)

print("Total no of blobs detected-{}".format(len(contour)))

Hori = np.concatenate((img_clr, rgb), axis=1)

cv2.imshow('HORIZONTAL', Hori)
cv2.imwrite("./output/output2.jpg", Hori)
cv2.waitKey(0)
cv2.destroyAllWindows()

