import cv2

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)

cv2.imshow('faces-detected', img)
cv2.waitKey()

cv2.imwrite('test.jpg', img)