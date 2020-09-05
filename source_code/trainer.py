import os
import cv2
import numpy as np
from PIL import Image

recognizer=cv2.face.createLBPHFaceRecognizer()
path = 'dataSet'

def getImageWithID(path):
    imagePaths = (os.path.join(path,f) for f in os.listdir(path) if f!=".DS_Store")
    faces=[]
    IDs=[]
    file = open('new.txt', 'w')
    file.close()
    file1 = open('new.txt', 'w')
    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L')
        faceNp = np.array(faceImg,'uint8')
        ID=0
        #ID = int(str(ord((imagePath.split('.')[1])[0])))
        name=(imagePath.split('.')[1])
        for c in name:
            ID+= int(ord(c))
        if(ID not in IDs):
            print(str(imagePath.split('.')[1])+" : "+str(ID))
            file1.write(str(name)+" "+str(ID)+"\n")
        #ID = int(str(ord((imagePath.split('.')[1])[0])) + str(imagePath.split('.')[2]))
        #ID = int(str("".join(str(ord(f)) for f in imagePath.split('.')[1]))+str(imagePath.split('.')[2]))
        #print(ID)
        faces.append(faceNp)
        IDs.append(ID)
        cv2.imshow("training",faceNp)
        cv2.waitKey(10)
    try:
        os.remove('users.txt')
    except:
        print('Well, the file wasn\'t found !')
    finally:
        os.rename('new.txt', 'users.txt')
    file1.close()
    return np.array(IDs), faces

Ids,faces = getImageWithID(path)
recognizer.train(faces, Ids)
recognizer.save('recognizer/trainingData.yml')
cv2.destroyAllWindows()