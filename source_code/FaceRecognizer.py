import cv2
from htmlWriter import create

facedetector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
rec = cv2.face.createLBPHFaceRecognizer()
rec.load('recognizer/trainingData.yml')
id = 0
prev = 0
X = {}
file = open('users.txt', 'r+')
for l in file.readlines():
    l.rstrip('\n')
    name, ID = l.split()
    ID = int(ID)
    X[ID] = name
for key, value in X.items():
    print("KEY : "+str(key)+" | "+"VALUE : "+value)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL

while True:
    ret, img = cap.read()

    # Invert image to look like mirror
    img = cv2.flip(img, 1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = facedetector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        id = rec.predict(gray[y:y + h, x:x + w])
        print(rec.predict(gray[y:y + h, x:x + w]))
        name_id = X[id]
        if(prev != id):
            create(name_id)
            f = open("reco_name.txt", "w")
            f.write(name_id)
            f.close()
            cap.release()
            cv2.destroyAllWindows()
            exit(0)
        cv2.putText(img, str(name_id), (x, y + h), font, 2.4, (255, 255, 255), 1)
    cv2.imshow('AI @ It\'s Best !', img)
    cv2.imwrite('user_name', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
