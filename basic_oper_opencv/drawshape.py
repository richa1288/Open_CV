#draw and write in image

import cv2
import numpy as np

#to create blank image
#np.zeros(height,width, number of color channels)
blank = np.zeros((500,500,3), dtype='uint8')
cv2.imshow('Blank', blank)
# img = cv2.imread('C:/Users/acer/Desktop/Open_CV/photos/375686.jpg')
# cv2.imshow("Girl", img)

#1. paint the image with certain colour
# green color 0,255,0
# blank[:]=0,255,0
# cv2.imshow('Green', blank)
# 2. to change certain portion of image
# give dimension to blank
blank[200:300,300:400]=0,255,0
cv2.imshow('Green', blank)
# 3. Draw a rectangle
#cv2.rectangle(imageObjectName, (‘top_left_vertex_coordinates’), (‘lower_right_vertex_coordinates’), (‘stroke_color_in_bgr’), ‘stroke_thickness’)
cv2.rectangle(blank, (30, 30), (300, 200), (0, 255, 0), 5)
cv2.imshow('Rectangle', blank)
# 4. Draw A circle
#cv2.circle(imageObjectName, (‘center_coordinates’), (‘circle_radius’), (‘color_in_bgr’), ‘stroke_thickness’)


cv2.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv2.imshow('Circle', blank)

#5. Draw a line
#cv2.line(imageObjectName, (‘start_coordinates’), (‘end_coordinates’), (‘color_in_bgr’), ‘line_thickness’)
cv2.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv2.imshow('Line', blank)
# 5. Write text
cv2.putText(blank, 'Hello, my name is Richa!!!', (0,225), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv2.imshow('Text', blank)



cv2.waitKey(0)


