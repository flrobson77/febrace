import face_recognition
import cv2

# This is a demo of running face recognition on a video file and saving the results to a new video file.
#
# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Open the input movie file
input_movie = cv2.VideoCapture("./video/robsoneoterceiro.mp4")
length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))

# Create an output movie file (make sure resolution/frame rate matches input video!)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_movie = cv2.VideoWriter('output.mp4', fourcc, 30, (640, 360))

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

# Initialize some variables
face_locations = []
face_encodings = []
#face_names = []
frame_number = 0

while True:
    # Grab a single frame of video
    ret, frame = input_movie.read()
    frame_number += 1

    # Quit when the input video file ends
    if not ret:
        break

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)


    #Estrutura de repetição identificando as faces conhecidas
    for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(know_face_encodings, face_encoding, tolerance=0.50)

        name = "Unknown Person"

        if True in matches:
            first_match_index = matches.index(True)
            name = know_face_names[first_match_index]
    
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
 
    print("Writing frame {} / {}".format(frame_number, length))
    output_movie.write(frame)

# All done!
input_movie.release()
cv2.destroyAllWindows()


#    #Draw BoX
#    #draw.rectangle(((left, top), (right, bottom)), outline=(0,0,0))
#
#    #Draw label
#    #text_width, text_height = draw.textsize(name)
#    #draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0,0,0), outline=(0,0,0))
#    #draw.text((left + 6, bottom - text_height - 5), name, fill=(255,255,255,255))
#
#del draw


#    for face_encoding in face_encodings:
#        # See if the face is a match for the known face(s)
#        match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.50)
#
#        # If you had more than 2 faces, you could make this logic a lot prettier
#        # but I kept it simple for the demo
#        #name = None
#    #    if match[0]:
#    #        name = "Lin-Manuel Miranda"
#    #    elif match[1]:
#    #        name = "Alex Lacamoire"
#
#    #   face_names.append(name)
#
#   # Label the results
#    #for (top, right, bottom, left), name in zip(face_locations, face_names):
#    #    if not name:
#    #        continue
#
