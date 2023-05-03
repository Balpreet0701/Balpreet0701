
#self practice same rectangle me different colours aa rhe as disco
#code to detect faces and showing rectangle of different colours

import cv2
from time import sleep      #for forceful delay
from random import randint
fd=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
vid = cv2.VideoCapture(0)
while True:
    #processing code
    flag,img=vid.read()
    if flag:
        img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces=fd.detectMultiScale(img_gray,1.1,5)
        
        for x,y,w,h in faces:          
        
            cv2.rectangle(img, pt1=(x,y), pt2=(x+w,y+h),color=randint(0,255),thickness=8)
            
        
        cv2.imshow('Preview',img)
        key=cv2.waitKey(1)
        if(key==ord('q')):
            break
    else:
        print('No Frames')
        break
    sleep(0.1)
vid.release()
cv2.destroyAllWindows()