import cv2
import cvzone

cap= cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('frame.mp4',fourcc,20,(640,480))

print('1. Cooling Glass\n2. Star Glass\n3. Native\n4. Pirate\n5. beard\n6.Magician')
ch=[1,2,3,4,5,6]
choice=int(input('Enter your choice: '))
img_loc="D:\Coding\python\snap"
if choice==1:
    img_loc+='\glass.png'
elif choice==2:
    img_loc+='\star.png'
elif choice==3:
    img_loc+='\\native.png'
elif choice==4:
    img_loc+='\pirate.png'
elif choice==5:
    img_loc+='\\beard.png'
elif choice==6:
    img_loc+='\cool.png'
while choice not in ch:
    print('please enter a valid choice')
    choice=int(input('Enter your choice: '))

cascade=cv2.CascadeClassifier(r"D:\Coding\python\snap\haarcascade_frontalface_default.xml")
f=cv2.imread(img_loc,cv2.IMREAD_UNCHANGED)

while True:
    _,frame=cap.read()
    gray_scale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=cascade.detectMultiScale(gray_scale)
    for (x,y,w,h) in faces:
        #cv2.rectangle(frame,(x,y),(x+w , y+h), (0,255,0),2)
        if choice== 1 or choice==2:
            rz=cv2.resize(f,(w,h))
            frame=cvzone.overlayPNG(frame,rz, [x-2, y-2])
        else:
            rz=cv2.resize(f,(int(w*1.5),int(h*1.5)))
            frame= cvzone.overlayPNG(frame, rz, [x-45,y-75])
    
    cv2.imshow('snap chat',frame)

    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyAllWindows()