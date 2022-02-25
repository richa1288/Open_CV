import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#histogram allows to visualize the distribution of pixel intensity in an image


# Read image
img = cv.imread('C:/Users/acer/Desktop/Open_CV/photos/375686.jpg')
cv.imshow("Girl", img)
blank = np.zeros(img.shape[:2], dtype='uint8')

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(gray,gray,mask=mask)
cv.imshow('Mask', masked)
#histogram
gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256] )
# plt.figure()
# plt.title('gray histogram')
# plt.xlabel('Bins')
# plt.ylabel('no. of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])




cv.waitKey(0)



