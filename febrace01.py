#Biblioteca de reconhecimento de face
import face_recognition

#Carregando imagem
image = face_recognition.load_image_file('./images/robson.jpg')

#Identificando a posição da ou das faces
face_locations = face_recognition.face_locations(image)

#Exibe a posicao da face (topo, esquerda, fundo e direita)
print(face_locations)
