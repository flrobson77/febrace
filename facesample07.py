import face_recognition
from PIL import Image

image = face_recognition.load_image_file('./images/robrodtar.jpg')
face_locations = face_recognition.face_locations(image)

#Identificando a quantidade de faces encontradas na imagem
if len(face_locations) == 1:
    print("Nesta imagem foi encontrada {} face.".format(len(face_locations)))
else:
    print("Nesta imagem foram encontradas {} faces.".format(len(face_locations)))

pil_image_original = Image.fromarray(image)
pil_image_original.show()

#(Array) Coordenadas de rostos encontrados
for face_location in face_locations:
    #Mostra a posição de cada face
    top, right, bottom, left = face_location
    print("Posição da face localizada Topo:{}, Esquerda:{}, Fundo:{}, Direita:{}".format(top, left, bottom, right))

    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
