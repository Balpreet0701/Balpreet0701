#code to detect faces and smile
import cv2
import numpy as np
from time import sleep      #for forceful delay

fd=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
sd=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')
vid = cv2.VideoCapture(0)
notcaptured=True

while notcaptured:
    
    #processing code
    flag,img=vid.read()
    
    if flag:
        img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        #cascade classifier se info laake multiscale me daal diya
        faces=fd.detectMultiScale(img_gray,scaleFactor=1.1,minNeighbors=5,minSize=(50,50)) 
        
        np.random.seed(50)
        colors=np.random.randint(0,255,(len(faces),3)).tolist()
        #colors=[np.random.randint(0,255,3).tolist()  for i in faces]
        i=0
        #min neighbor and scale factor less rkhna hai vrna agar perfect face aaega tabhi detect krega
        
        
        for x,y,w,h in faces: 
            face=img_gray[y:y+h,x:x+w].copy()
            
            smiles=sd.detectMultiScale(face,scaleFactor=1.1,minNeighbors=5,minSize=(50,50))
            
            if len(smiles)==1:
                cv2.imwrite('myselfie.png',img) 
                notcaptured=False
                break               
        
            cv2.rectangle(img, pt1=(x,y), pt2=(x+w,y+h),color=colors[i],thickness=2)
            i+=1
            
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