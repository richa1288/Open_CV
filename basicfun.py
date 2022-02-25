import cv2


# Read image
img = cv2.imread('C:/Users/acer/Desktop/Open_CV/photos/375686.jpg')
cv2.imshow("Girl", img)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

# Convert to Blur
blur = cv2.GaussianBlur(img, (7,7), cv2.BORDER_DEFAULT)
cv2.imshow('Blur', blur)

# Edge Cascade
# to find edges
canny = cv2.Canny(blur, 125, 175)
cv2.imshow('Canny Edges', canny)

# Dilating the image

dilated = cv2.dilate(canny, (7,7), iterations=3)
cv2.imshow('Dilated', dilated)

# Eroding
eroded = cv2.erode(dilated, (7,7), iterations=3)
cv2.imshow('Eroded', eroded)

# Resize
resized = cv2.resize(img, (500,500), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resized', resized)

# Cropping
cropped = resized[50:200, 200:400]
cv2.imshow('Cropped', cropped)

cv2.waitKey(0)
