import face_recognition
import os
from PIL import Image

image = face_recognition.load_image_file('./images/robrodtar.jpg')
face_locations = face_recognition.face_locations(image)

#(Array) Coordenadas de rostos encontrados
print ("Foram encontraas ", format(len(face_locations)), "face(s) nessa imagem")

for face_location in face_locations:
    top, right, bottom, left = face_location
    
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()

espeak.synth (format(len(face_locations)))
espeak.synth ("faces")
espeak.synth ("encontradas")
