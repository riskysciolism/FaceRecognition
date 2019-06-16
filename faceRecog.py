import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascades_cuda/haarcascade_frontalface_default.xml')
# face_cascade = cv2.CascadeClassifier('lbpcascades/lbpcascade_frontalface_improved.xml')
# face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)


while True:
    # capture frame by frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4)

    for (x, y, w, h) in faces:
        print(x, y)
        roi_gray = gray[y:y+h, x:x+w]
        img_item = 'test.png'
        #cv2.imwrite(img_item, roi_gray)

        color = (255, 0, 0)
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

    # open window and show current frame
    cv2.imshow('frame', frame)

    # exit loop
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# clean up
cap.release()
cv2.destroyAllWindows()

