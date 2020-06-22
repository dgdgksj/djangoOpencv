from django.conf import settings
import numpy as np
import cv2


def opencv_canny(path):
    img = cv2.imread(path, 1)

    if (type(img) is np.ndarray):
        print(img.shape)

        baseUrl = settings.MEDIA_ROOT_URL + settings.MEDIA_URL
        face_cascade = cv2.CascadeClassifier(baseUrl + 'haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier(baseUrl + 'haarcascade_eye.xml')

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edge=cv2.Canny(img,50,200)
        edge = cv2.resize(edge, dsize=(800, 680), interpolation=cv2.INTER_AREA)

        cv2.imwrite(path, edge)

    else:
        print('someting error')
        print(path)