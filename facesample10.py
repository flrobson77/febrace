import face_recognition
import cv2

# Arquivo de vídeo
input_movie = cv2.VideoCapture("./video/robsoneoterceiro.mp4")
#length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))

# Saída de vídeo
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#output_movie = cv2.VideoWriter('output.avi', fourcc, 30, (640, 360))

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

# Inicializando as variáveis
face_locations = []
face_encodings = []
face_names = []
#frame_number = 0
process_this_frame = True


#Analisando os quadros do vídeo
while True:
    # Captura o quadro de vídeo
    ret, frame = input_movie.read()

    #Redimensiona o quadro para melhorar a perfomance
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Converte a imagem BGR do openCV para RGB do face_recognition
    rgb_frame = frame[:, :, ::-1]

    # processa quadros intercalados para economizar tempo
    if process_this_frame:
        #Obtem todas as faces e as respectivas codificações
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        face_names = []

        #Estrutura de repetição identificando as faces conhecidas
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(know_face_encodings, face_encoding)

            name = "Desconhecido"

            if True in matches:
                first_match_index = matches.index(True)
                name = know_face_names[first_match_index]

                face_names.append(name)

    process_this_frame = not process_this_frame

    for(top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        left *= 4
        bottom *= 4
        left *= 4
    
        # Desenha retangulo sobre a face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Desenha a etiqueda com o nome abaixo da face
        cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    #Mostra a imagem resultante
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# All done!
input_movie.release()
cv2.destroyAllWindows()
