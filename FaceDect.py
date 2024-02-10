from cvzone.SerialModule import SerialObject
import serial
import cv2 as cv
import math

# Reading video, webcam can be used as 0, 1 and 2 will represent camera 1 and camera 2
capture = cv.VideoCapture(0)

haar_cascade = cv.CascadeClassifier("../haar_face.xml")

arduino = serial.Serial('COM5',9600)

while True:
    isTrue, frame = capture.read() # reads frame by frame -> return frame and bool if successful
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)
        
        face_center_x = x + w // 2
        servo_angle = int(face_center_x / frame.shape[1] * 180)
        arduino.write(f"{servo_angle},{servo_angle}\n".encode('utf-8'))

        # To send one data use arduino.write(bytes[servo_angle]), for arduino IDE use 
        # int angle = Serial.read() to get the data
        cv.putText(frame, str(servo_angle), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 2)
        cv.circle(frame, (face_center_x,math.floor(frame.shape[0]/2)), 10, (0,0,255), thickness=-1)

    
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'): # if letter d is pressed break
        break

arduino.close()
capture.release()
cv.destroyAllWindows() 