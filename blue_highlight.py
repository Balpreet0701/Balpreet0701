import cv2
import plotly
import plotly.express as px
import skimage
def imshowPx(im, cv = True, gray = False):
    fig = px.imshow(im[:,:,::-1] if cv else im, binary_string=gray)
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    plotly.io.show(fig) 


vid = cv2.VideoCapture(0)
while True:
    flag, img = vid.read()
    if flag:
        #img = skimage.data.astronaut() #RGB
        #Blue = BluePlane - Gray
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_p = cv2.subtract(img[:,:,-1], cv2.cvtColor(img, cv2.COLOR_RGB2GRAY))
        th, img_p2 = cv2.threshold(img_p, 60, 255, cv2.THRESH_BINARY)
        img_p3 = skimage.morphology.remove_small_objects(img_p2.astype(bool), 50)
        img_p4 = cv2.dilate(img_p3.astype('uint8'), cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10,10))).astype(bool)
        img_p5 = skimage.morphology.remove_small_holes(img_p4, 1000)
        rp = skimage.measure.regionprops(skimage.measure.label(img_p5))
        img_preview = img.copy()
        if len(rp) > 0:
            (y1, x1, y2, x2) = rp[0].bbox
            cv2.rectangle(img_preview,
                          pt1=(x1, y1), pt2=(x2,y2),
                          color = (255, 255, 0),
                          thickness=3)
        #Green = GreenPlane - Gray
        #Red = RedPlane - Gray
        #Cyan = Gray - RedPlane
        #Magenta = Gray - GreenPlane
        #Yellow = Gray - BluePlane
        img_preview = cv2.cvtColor(img_preview, cv2.COLOR_BGR2RGB)
        cv2.imshow('Preview', img_preview)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
cv2.destroyAllWindows()
cv2.waitKey(1)
vid.release()