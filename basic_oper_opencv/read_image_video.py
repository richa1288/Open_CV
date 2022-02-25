#from sympy import python


#pip install caer
#pip install opencv-contrib-python
# open cv is a library for computer vision primarily for deriving insights from media files.
# Reading of image
import cv2 
img = cv2.imread('C:/Users/acer/Desktop/Open_CV/photos/375686.jpg')
cv2.imshow("Girl", img)

cv2.waitKey(0)

# Read video
capture=cv2.VideoCapture('C:/Users/acer/Desktop/Open_CV/videos/sam.mp4')
while True:
    isTrue, frame= capture.read()
    cv2.imshow('Video',frame)

    if cv2.waitKey(20)  & 0xFF==ord('d'):
        break
capture.release()
cv2.destroyAllWindows()
    