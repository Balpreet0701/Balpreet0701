import cv2
vid = cv2.VideoCapture(0)
while True:

    flag,img=vid.read()
    if flag:
        #processing  code
        img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #COLOR is a constant which is always written in capitals,if something in camelcase then it is a function
        #print(type(img_gray))
        #break
        #to get black and white image 
        #THRESH_BINARY_INV is a function to inverse the colour that is black becomes white and white becomes black
        
        th,img_bw=cv2.threshold(img_gray,100,255,cv2.THRESH_BINARY_INV)
        cv2.imshow('Preview',img_bw)
        key=cv2.waitKey(1)
        if(key==ord('q')):
            break
    else:
        break
vid.release()
cv2.destroyAllWindows()