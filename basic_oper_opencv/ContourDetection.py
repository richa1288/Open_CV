import cv2
import numpy as np
import matplotlib as plt

# Read image
img = cv2.imread('C:/Users/acer/Desktop/Open_CV/photos/375686.jpg')
cv2.imshow("Girl", img)
blank= np.zeros((360,203,3), dtype='uint8')
print(img.shape)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

ret, thresh=cv2.threshold(gray,127,2500, cv2.THRESH_BINARY)
contours, hierarchies = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv2.drawContours(blank, contours, -1, (0,0,255), 1)
cv2.imshow('Contours Drawn', blank)


# blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)
# cv2.imshow('Blur', blur)

# canny = cv2.Canny(blur, 125, 175)
# cv2.imshow('Canny Edges', canny)

cv2.waitKey(0)