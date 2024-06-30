import numpy as np 
import cv2
import imutils
import datetime
gun_cascade = cv2.CascadeClassifier('cascade.xml')
camera = cv2.VideoCapture(0)
firstFrame = None
gun_exist = None
while True:
    ret,frame = camera.read()
    frame = imutils.resize(frame,width = 500)
    gray = cv2.cvtColor(frame,'cv2.colour_BGR2GRAY')
    gun = gun_cascade.detectMultiscale(gray,
                                       1.3,5,
                                       minsize=(100,100))
    if len(gun) > 0:
        gun_exist = True
    for(x,y,w,h) in gun:
        frame = cv2.rectangle(frame,
                              (x,y),
                              (x+w,y+h),
                              (255,0,0),2)                                       
        roi_gray = gray[y : y + h, x : x + w]
        roi_colour = frame[y : y + h, x : x + w]
    if firstFrame is None:
        firstFram = gray
        continue
    cv2.iamshow("Seceurity feed",frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
if gun_exist:
    print('Gun is detected')
else:
    print('Gun didnt detected')
camera.release()
cv2.distroyAllWindows()

      
