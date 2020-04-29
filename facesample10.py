import face_recognition
import cv2

print ("### Rodando ###")

#Banco de imagens
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

print ("### Carregando Vídeo ###")

# Arquivo de vídeo
cap = cv2.VideoCapture("./video/robsoneoterceiro.mp4")

# Inicializando as variáveis
face_locations = []
face_encodings = []
frame_number = 0
process_this_frame = True

#Analisando os quadros do vídeo
while True:
    # Captura o quadro de vídeo
    ret, frame = cap.read()

    #Redimensiona o quadro para melhorar a perfomance
    frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.3)

    # Converte a imagem BGR do openCV para RGB do face_recognition
    rgb_frame = frame[:, :, ::-1]

    # processa quadros intercalados para economizar tempo
    if process_this_frame:
        #Obtem todas as faces e as respectivas codificações
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    process_this_frame = not process_this_frame

    face_names = []

    #Estrutura de repetição identificando as faces conhecidas
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(know_face_encodings, face_encoding)

        name = "Unknow"
                           
        if True in matches:
            first_match_index = matches.index(True)
            name = know_face_names[first_match_index]
            #print ("### Achou!!! ###") 
            #print (name)
            face_names.append(name)
        else:
            face_names.append(name)

        for(top, right, bottom, left), name in zip(face_locations, face_names):
                        
            color = (255,255,255)
            texto = (0,0,0)
            font = cv2.FONT_HERSHEY_SIMPLEX
        
            # Desenha retangulo sobre a face
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        
            # Desenha a etiqueda com o nome abaixo da face
            cv2.rectangle(frame, (left, bottom - 20), (right, bottom), color, cv2.FILLED)
           
            # Texto da imagem
            cv2.putText(frame, name, (left + 5, bottom - 5), font, 0.5, texto, 2)

        #Mostra a imagem resultante
        cv2.imshow('EVE-ng', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print ("### Acabou !!! ###")