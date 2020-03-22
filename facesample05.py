import face_recognition

image = face_recognition.load_image_file('./images/robson.jpg')
face_locations = face_recognition.face_locations(image)
face_landmarks = face_recognition.face_landmarks(image)

#Identificando a quantidade de faces encontradas na imagem
if len(face_locations) == 1:
    print("Nesta imagem foi encontrada {} face.".format(len(face_locations)))
else:
    print("Nesta imagem foram encontradas {} faces.".format(len(face_locations)))


#(Array) Coordenadas de rostos encontrados
for face_location in face_locations:
    #Mostra a posição de cada face
    top, right, bottom, left = face_location
    print("Posição da face localizada Topo:{}, Esquerda:{}, Fundo:{}, Direita:{}".format(top, left, bottom, right))

for face_landmark in face_landmarks:
    #Mostrar a posicao de partes da face


print(face_locations)
print(face_landmarks)
