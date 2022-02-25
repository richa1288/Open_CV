import cv2
import numpy as np

# Read image
img = cv2.imread('C:/Users/acer/Desktop/Open_CV/photos/375686.jpg')
cv2.imshow("Girl", img)
#translate (image, x pixels, y pixel)
def translate(img, x, y):
     transMat = np.float32([[1,0,x],[0,1,y]])
     dimensions = (img.shape[1], img.shape[0])
     return cv2.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, 100)
cv2.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv2.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv2.imshow('Rotated', rotated)

rotated_rotated = rotate(img, -90)
cv2.imshow('Rotated Rotated', rotated_rotated)

# Resizing
resized = cv2.resize(img, (500,500), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resized', resized)

# Flipping
#0 vertical 
#-1 reversed mirroe image
flip = cv2.flip(img, -1)
cv2.imshow('Flip', flip)

# Cropping
cropped = resized[50:200, 200:400]
cv2.imshow('Cropped', cropped)
cv2.waitKey(0)