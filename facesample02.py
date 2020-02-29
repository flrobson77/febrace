import face_recognition

image = face_recognition.load_image_file('./images/robrodtar.jpg')
face_locations = face_recognition.face_locations(image)

#(Array) Coordenadas de rostos encontrados

faces = len(face_locations)

print (faces)
