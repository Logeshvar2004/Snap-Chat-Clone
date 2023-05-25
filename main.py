import cv2
import cvzone

cap= cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('frame.mp4',fourcc,20,(640,480))

img_loc="C:\\Users\\aclog\\Desktop\\Coding\\python\\snap\\sunglass.png"
cascade=cv2.CascadeClassifier(r"C:\Users\aclog\Desktop\Coding\python\snap\haarcascade_frontalface_default.xml")
f=cv2.imread(img_loc,cv2.IMREAD_UNCHANGED)
choice=input('save video(y/n):')
while True:
    _,frame=cap.read()
    gray_scale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=cascade.detectMultiScale(gray_scale)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w , y+h), (0,255,0),2)
        rz=cv2.resize(f,(w,h))
        frame=cvzone.overlayPNG(frame,rz, [x-2, y-2])
    
    cv2.imshow('snap chat',frame)

    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyAllWindows()