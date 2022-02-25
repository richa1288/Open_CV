import cv2 as cv
import numpy as np


# Read image
img = cv.imread('C:/Users/acer/Desktop/Open_CV/photos/375686.jpg')
cv.imshow("Girl", img)
# imp= mask should be of same size as image
blank= np.zeros(img.shape[:2], dtype='uint8')
mask= cv.circle(blank, (img.shape[1]//2, img.shape[0]//2),100,255,-1)
cv.imshow('mask', mask)

masked_img= cv.bitwise_and(img, img, mask=mask)
cv.imshow('masked_img', masked_img)


cv.waitKey(0)