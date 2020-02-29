from PIL import Image
import face_recognition
import sys

imgs = sys.argv[1:]
print (imgs)

image = face_recognition.load_image_file('imgs')
face_locations = face_recognition.face_locations(image)

print (face_locations)

#(Array) Coordenadas de rostos encontrados
#print ("Quantas pessoas existem na imagem? ", len(face_locations))

#for face_location in face_locations:
#    top, right, bottom, left = face_location
#    
#    face_image = image[top:bottom, left:right]
#    pil_image = Image.fromarray(face_image)
#    pil_image.show()
