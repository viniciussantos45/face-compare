
import cv2
import os
from deepface import DeepFace
from lib import getImages

xml_haar_cascade = 'haarcascade_frontalface_alt2.xml'

# Lista paths de imagens de faces para servir como base de comparação
imgs_for_get_faces = getImages("./photos_for_get_faces")

# Carregar classificador
faceClassifier = cv2.CascadeClassifier(xml_haar_cascade)

facesBase = []
# Carrega imagem
for img in imgs_for_get_faces:
    imgRGB = cv2.imread(img)
    imgGray = cv2.imread(img, 0)
    faces = faceClassifier.detectMultiScale(imgGray)

    count = 1
    for x, y, w, h in faces:
        os.makedirs("faces", exist_ok=True)

        cv2.imwrite(
            f'./faces/{count}-{os.path.basename(img)}', imgGray[y:y+h, x:x+w])
        count += 1


gray_faces = getImages("./faces")

photos = getImages("./photos")

# Carrega imagem
for img in photos:
    imgRGB = cv2.imread(img)
    imgGray = cv2.imread(img, 0)
    faces = faceClassifier.detectMultiScale(imgGray)

    for x, y, w, h in faces:
        for base_face_tester in gray_faces:

            os.makedirs("photos_to_save", exist_ok=True)
            file_name = f'./photos_to_save/{os.path.basename(img)}'

            if os.path.exists(file_name):
                continue

            os.makedirs("faces_testers", exist_ok=True)

            file_face_tester = f'./faces_testers/{os.path.basename(img)}'
            cv2.imwrite(file_face_tester, imgGray[y:y+h, x:x+w])

            result = DeepFace.verify(
                file_face_tester, base_face_tester, enforce_detection=False, model_name="SFace")

            # print(img)
            # print(result)

            if result['verified']:
                cv2.imwrite(file_name, imgRGB)

os.rmdir("./faces")
os.rmdir("./faces_testers")
