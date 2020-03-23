import face_recognition
#carregar a imagem
image = face_recognition.load_image_file('./images/robson.jpg')

#metodo que identifica a(s) face(s)
face_locations = face_recognition.face_locations(image)

#metodo que codifica as faces
face_encodings = face_recognition.face_encodings(image)

#metodo que identifica partes da face
face_landmarks = face_recognition.face_landmarks(image)

print("Identifica rosto na imagem analisada")
print(face_locations)

print("Codifica rosto na imagem encontrada")
print(face_encodings)

print("Exibe os pontos das Partes da Face")
print(face_landmarks)
