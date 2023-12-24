import streamlit as st
import cv2
import cvzone
import numpy as np

def get_image_location(choice):
    img_loc = "D:/Coding/python/snap"  # Update the path as needed
    if choice == 'Glass':
        img_loc += '/glass.png'
    elif choice == 'Star Glass':
        img_loc += '/star.png'
    elif choice == 'Native': 
        img_loc += '/native.png'
    elif choice == 'Pirate':
        img_loc += '/pirate.png'
    elif choice == 'Beard':
        img_loc += '/beard.png'
    elif choice == 'Cool':
        img_loc += '/cool.png'
    return img_loc

def overlay_image(frame, choice, face):
    img_loc = get_image_location(choice)
    f = cv2.imread(img_loc, cv2.IMREAD_UNCHANGED)

    if choice == 'Glass' or choice == 'Star Glass':
        rz = cv2.resize(f, (face[2], face[3]))
        frame = cvzone.overlayPNG(frame, rz, [face[0] - 2, face[1] - 2])
    else:
        rz = cv2.resize(f, (int(face[2] * 1.5), int(face[3] * 1.5)))
        frame = cvzone.overlayPNG(frame, rz, [face[0] - 45, face[1] - 75])

    return frame

def main():
    st.title("Snapchat Filters with Streamlit")
    frame_placeholder= st.empty()
    cap = cv2.VideoCapture(0)
    cascade = cv2.CascadeClassifier("D:/Coding/python/snap/haarcascade_frontalface_default.xml")

    stop_button_pressed= st.button("Capture")
    choice = st.selectbox("Select a filter", ['Glass', 'Star Glass', 'Native', 'Pirate', 'Beard', 'Cool'])

    while True:
        _, frame = cap.read()
        gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray_scale)

        for face in faces:
            frame = overlay_image(frame, choice, face)
        frame= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame, channels="RGB")        
               
        if cv2.waitKey(1)==ord('q') or stop_button_pressed:
            break
    
    cap.release()

if __name__ == "__main__":
    main()