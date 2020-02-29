import face_recognition
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
test_image = face_recognition.load_image_file('./images/robrodtar.jpg')

#Encontrando faces em imagem de teste
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

#(Array) Coordenadas de rostos encontrados
print ("Foram encontraas ", format(len(face_locations)), "face(s) nessa imagem")

#Converte imagem formato PIL
pil_image = Image.fromarray(test_image)

#Criar instancia ImageDraw
draw = ImageDraw.Draw(pil_image)

#Estrutura de repetição identificando as faces conhecidas
for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(know_face_encodings, face_encoding)

    name = "Unknown Person"

    if True in matches:
        first_match_index = matches.index(True)
        name = know_face_names[first_match_index]

    #Draw BoX
    draw.rectangle(((left, top), (right, bottom)), outline=(0,0,0))

    #Draw label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0,0,0), outline=(0,0,0))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255,255,255,255))

del draw

#Exiba a imagem
pil_image.show()
pil_image.save('./images/identify.jpg')