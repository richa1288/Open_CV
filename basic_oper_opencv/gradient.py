import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#histogram allows to visualize the distribution of pixel intensity in an image


# Read image
img = cv.imread('C:/Users/acer/Desktop/Open_CV/photos/375686.jpg')
cv.imshow("Girl", img)


gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Laplacian
# cv2.Laplacian(frame,cv2.CV_64F)
#second parameter is the depth of the destination image
lap=cv.Laplacian(gray,cv.CV_64F)
#lap=np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

cv.waitKey(0)

#sobel