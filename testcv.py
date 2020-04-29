import cv2

#Captura o arquivo de vídeo
cap = cv2.VideoCapture("./video/robsoneoterceiro.mp4")


#Exibir o video
while True:

    ret, frame = cap.read()
    sframe = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    
    cv2.imshow("Minha mensagem", sframe)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
