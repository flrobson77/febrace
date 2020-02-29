import face_recognition
from espeak import espeak
from PIL import Image

image = face_recognition.load_image_file('./images/robrodtar.jpg')
face_locations = face_recognition.face_locations(image)

#(Array) Coordenadas de rostos encontrados

print ("Quantas pessoas existem na imagem? ", len(face_locations))
espeak.synth ("Existem ", len(face_locations) , "pessoas" )

for face_location in face_locations:
    top, right, bottom, left = face_location
    
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
