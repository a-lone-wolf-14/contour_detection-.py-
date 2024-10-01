import cv2

def contour(path):
    img=cv2.imread(path)
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_gaussian_blur=cv2.GaussianBlur(img_gray,(5,5),3)
    img_canny=cv2.Canny(img_gaussian_blur,100,100)
    img_contour=img.copy()

    contours,hierarchy=cv2.findContours(img_canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area=cv2.contourArea(cnt)
        print(area)

        cv2.drawContours(img_contour,cnt,-1,(255,0,0),3)

        peri=cv2.arcLength(cnt,True)
        print(peri)

        point=cv2.approxPolyDP(cnt,0.03*peri,True)
        print(len(point))
        print('----')

        x,y,w,h=cv2.boundingRect(point)
        cv2.rectangle(img_contour,(x,y),(x+w,y+h),(0,0,255),3)

        if len(point)==3:
            cv2.putText(img_contour,"TRIANGLE",(x+w//2,y+h//2),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),3)
        if len(point)==4:
            asp=w/h
            if asp==1:
                cv2.putText(img_contour, "SQUARE", (x + w // 2, y + h // 2), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)
            else:
                cv2.putText(img_contour, "RECTANGLE", (x + w // 2, y + h // 2), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)
        if len(point)>4:
            cv2.putText(img_contour, "CIRCLE", (x + w // 2, y + h // 2), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)

    cv2.imshow("Contour Detection",img_contour)
    cv2.waitKey(0)

contour(r'C:\Users\Suyash R\Documents\OpenCV\resources\sample6.jpeg')