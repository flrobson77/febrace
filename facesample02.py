import face_recognition

image = face_recognition.load_image_file('./images/ifalunos.jpg')
face_locations = face_recognition.face_locations(image)

#(Array) Coordenadas de rostos encontrados

print ("Foram encontraas ", format(len(face_locations)), "face(s) nessa imagem")