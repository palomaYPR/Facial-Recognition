
# Class that trains the system with the collection of photographs to
# create a data set in .yml
import os
import numpy as np
import cv2 as cv
from PIL import Image

recognizer = cv.face.LBPHFaceRecognizer_create()
path = "./images"

def getImageWithID(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    IDs = []

    for imagePath in imagePaths:
        facesImg = Image.open(imagePath).convert('L')
        faceNP = np.array(facesImg, 'uint8')
        ID = int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(faceNP)
        IDs.append(ID)
        cv.imshow("Adding faces for training ", faceNP)
        print('Ready!')
        cv.waitKey(10)
    return np.array(IDs), faces

Ids, faces = getImageWithID(path)
recognizer.train(faces, Ids)
recognizer.save("images/trainingData.yml")
cv.destroyAllWindows()
