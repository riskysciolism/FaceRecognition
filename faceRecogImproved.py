import cv2
from VideoStream import VideoStream

face_cascade = cv2.CascadeClassifier('haarcascades_cuda/haarcascade_frontalface_default.xml')
# face_cascade = cv2.CascadeClassifier('lbpcascades/lbpcascade_frontalface_improved.xml')
# face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')

vs = VideoStream().start()

while True:
    frame = vs.read()

    frame = cv2.flip(frame, 1)
    # make frame gray, to perform face detection on it
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4)

    for (x, y, w, h) in faces:
        print(x, y)
        roi_gray = gray[y:y + h, x:x + w]
        img_item = 'test.png'
        # cv2.imwrite(img_item, roi_gray)

        color = (255, 0, 0)
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
    # cv2.imshow('frame', frame)

    # exit loop
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# clean up
cv2.destroyAllWindows()
vs.stop()
