import face_recognition
#carregar a imagem
image = face_recognition.load_image_file('./images/robson.jpg')

#metodo que identifica a(s) face(s)
face_locations = face_recognition.face_locations(image)

#metodo que identifica partes da face
face_landmarks = face_recognition.face_landmarks(image)


print("Posicao de Partes da Face")
print(face_locations)

print("Posicao de Partes da Face")
print(face_landmarks)
