import cv2
img = cv2.imread('C:/Users/acer/Desktop/Open_CV/photos/375686.jpg')
cv2.imshow("Girl", img)
#rescale= change of height and width
def rescaleFrame(frame, scale=0.2):
    width=int(frame.shape[1]*scale)
    Height=int(frame.shape[0]*scale)
    dimensions= (width, Height)

    return cv2.resize(frame,dimensions)
resized_image=rescaleFrame(img)
cv2.imshow('samridhi', resized_image)
cv2.waitKey(0)
    # Read video
# capture=cv2.VideoCapture('C:/Users/acer/Desktop/Open_CV/videos/sam.mp4')
# while True:
#     isTrue, frame= capture.read()
#     frame_resize= rescaleFrame(frame, scale=0.75)

#     cv2.imshow('Video',frame)
#     cv2.imshow('video resized', frame_resize)

#     if cv2.waitKey(20)  & 0xFF==ord('d'):
#         break
# capture.release()
# cv2.destroyAllWindows()
    