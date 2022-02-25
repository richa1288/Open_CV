import cv2
import numpy as np
import matplotlib as plt



# Read image
img = cv2.imread('C:/Users/acer/Desktop/Open_CV/photos/gradient.png')
cv2.imshow("Girl", img)


_,thresh_binary=cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('thresh_binary', thresh_binary)
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow('Binary Threshold Inverted', thresh2)
cv2.imshow('Truncated Threshold', thresh3)
cv2.imshow('Set to 0', thresh4)
cv2.imshow('Set to 0 Inverted', thresh5)
cv2.waitKey(0)
cv2.destroyAllWindows