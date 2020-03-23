import face_recognition
import os
from subprocess import call
from PIL import Image, ImageDraw

#Carregando banco de imagens
image_joel = face_recognition.load_image_file('./images/joel.jpg')
image_robson = face_recognition.load_image_file('./images/robson.jpg')
image_rodrigo = face_recognition.load_image_file('./images/rodrigo.jpg')
image_tarcisio = face_recognition.load_image_file('./images/tarcisio.jpg')

#Identificando as imagens do banco que o programa conhece
joel_face_encoding = face_recognition.face_encodings(image_joel)[0]
robson_face_encoding = face_recognition.face_encodings(image_robson)[0]
rodrigo_face_encoding = face_recognition.face_encodings(image_rodrigo)[0]
tarcisio_face_encoding = face_recognition.face_encodings(image_tarcisio)[0]

know_face_encodings = [
    joel_face_encoding,
    robson_face_encoding,
    rodrigo_face_encoding,
    tarcisio_face_encoding
]

know_face_names = [
    "Joel",
    "Robson",
    "Rodrigo",
    "Tarcisio"
]


#Carregando Imagem de Teste
test_image = face_recognition.load_image_file('./images/robsoneosegundo.jpg')

#Encontrando faces em imagem de teste
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

#Gerando nova imagem
pil_image = Image.fromarray(test_image)

#Criar instancia ImageDraw
draw = ImageDraw.Draw(pil_image)

#Coordenadas dos rostos encontrados
for face_location in face_locations:
    #Mostra a posição de cada face
    top, right, bottom, left = face_location
    print("Posição da face localizada Topo:{}, Esquerda:{}, Fundo:{}, Direita:{}".format(top, left, bottom, right))

#Estrutura de repetição identificando as faces conhecidas
for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(know_face_encodings, face_encoding)
    print (matches)
    print (face_encoding)
    name = "Desconhecido"
    
    if True in matches:
        first_match_index = matches.index(True)
        print (first_match_index)
        name = know_face_names[first_match_index]

    print (name)

    #Desenha um retangulo em torno da face
    draw.rectangle(((left, top), (right, bottom)), outline=(0,255,255))

    #Coloca uma etiqueta com nome em baixo da face
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 20), (right, bottom)), fill=(0,255,255), outline=(0,255,255))
    draw.text((left + 10, bottom - text_height - 10), name, fill=(0,0,0,1))
    
    #Sintetiza por meio da voz as faces encontradas
    call(["espeak",name])

del draw

#Exiba a imagem com as faces reconhecidas
pil_image.show()
pil_image.save('./images/nvimagem/identify010.jpg')
