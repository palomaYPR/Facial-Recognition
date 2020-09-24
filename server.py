
# Class that contains the server, who will receive the photograph to later train the machine
# Class that performs the search of the face in the data-set,
# checking whether or not it exists in it.

import cv2 as cv
from PIL import Image
import socket, pickle
import pymysql

# Declaramos las variables
ipServidor = "localhost"
puertoServidor = 9797
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

# Configuramos los datos para conectarnos con el servidor
# socket.AF_INET para indicar que utilizaremos Ipv4
# socket.SOCK_STREAM para utilizar TCP/IP (no UDP)
# Estos protocolos deben ser los mimso que en el servidor

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((ipServidor, puertoServidor))
print('Conectado con el servidor ---> %s:%s' %(ipServidor, puertoServidor))


def send_data(a,b,c,d,e,f):

    data = str(f'ID: {a} -- No. Control: {b} -- Nombre(s): {c} -- Apellido Paterno: {d} -- Apellido Materno: {e} -- Carrera: {f}')
    server.send(data.encode())


def get_information(id):
        ids = id
        db = pymysql.connect(host='localhost', user='root', passwd='sistemas', db='accesoITSCH')
        cursor = db.cursor()
        query = 'SELECT * FROM alumnos WHERE id = %s' %ids
        cursor.execute(query)
        res = cursor.fetchone()
        clave = res[0]
        no_Ctrl = res[1]
        nom = res[2]
        apeP = res[3]
        apeM = res[4]
        carr = res[5]
        send_data(clave,no_Ctrl,nom,apeP,apeM,carr)


def face_Detector(path):
    img = cv.imread(path)
    rec = cv.face.LBPHFaceRecognizer_create()
    rec.read("./images/trainingData.yml")
    id = 0
    font = cv.FONT_HERSHEY_COMPLEX_SMALL

    while 1:
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.5, 5)
        for (x, y, w, h) in faces:
            cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            id, conf = rec.predict(gray[y:y + h, x:x + w])
            if id == 2:
                get_information(id)
            elif id == 1:
                get_information(id)
            elif id == 3:
                get_information(id)
            elif id == 4:
                get_information(id)
            elif id == 5:
                get_information(id)
            elif id == 6:
                get_information(id)
            elif id == 7:
                get_information(id)
            elif id == 8:
                get_information(id)
            elif id == 9:
                get_information(id)
            elif id == 10:
                get_information(id)
            elif id == 11:
                get_information(id)
            elif id == 12:
                get_information(id)
            elif id == 13:
                get_information(id)
            elif id == 14:
                get_information(id)
            elif id == 15:
                get_information(id)
            elif id == 16:
                get_information(id)
            elif id == 17:
                get_information(id)

            else:
                print('NULL')

            cv.putText(img, str(id), (x, y + h), font, 2, 255)
            #cv.imshow('La cena', img)
        break


def contains_face(path):
    image = cv.imread(path)  # Recibida
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for i in faces:
        if i.any() == 1:
            print('-- FOUND --')
            for (x, y, w, h) in faces:
                cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                #cv.imshow('DETECTOR', image)
                face_Detector(path)
                break
        else:
            data = '-- NO FACE --'
            server.send(data.encode())
            break

    cv.waitKey(0)
width = 800
height = 600

while True:
    img = server.recv(1024)  # El número indica el número máximo de bytes
    imagen = Image.open(img)
    #im1 = imagen.resize((width, height), Image.BILINEAR)
    #im1.save('recibido.jpg')
    imagen.save('recibido.jpg')
    path = 'recibido.jpg'
    contains_face(path)
    break
