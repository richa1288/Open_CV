import cv2 as cv


# Read image

img = cv.imread('C:/Users/acer/Desktop/Open_CV/photos/sidhi.jpg')
cv.imshow("Girl", img)

cv.waitKey(0)