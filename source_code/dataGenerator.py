import cv2
import sys
facedetector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)


id = str(sys.argv[1])
print('Inside The Generator.py : The passed name is : '+id)
count=0;
while True:
    ret, img = cap.read()

    # Invert image to look like mirror
    img = cv2.flip(img,1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = facedetector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        count=count+1;
        cv2.imwrite("dataSet/User."+str(id)+"."+str(count).zfill(2)+".jpg",gray[y:y+h,x:x+h])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow('Say Cheese !', img)
    cv2.waitKey(100)
    if(count>20):
        break
    print("Yo! Data Collected : " + "dataSet/User."+str(id)+"."+str(count)+".jpg")
cap.release()
cv2.destroyAllWindows()
