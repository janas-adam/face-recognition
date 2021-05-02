import numpy
import face_recognition
import cv2

video_capture = cv2.VideoCapture(0)

known_face_image = face_recognition.load_image_file("./img/known/steve_jobs.jpg")
known_face_encoding = face_recognition.face_encodings(known_face_image)[0]

known_face_encondings = [known_face_encoding]
known_face_names = ["Steve"]

while True:
    ret, frame = video_capture.read()

    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

        matches = face_recognition.compare_faces(known_face_encondings, face_encoding)

        name = "Unknown"

        face_distances = face_recognition.face_distance(known_face_encondings, face_encoding)

        best_match_index = numpy.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        cv2.rectangle(frame, (left, top), (right, bottom), (255, 255, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255, 255, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (0, 0, 0), 1)

    cv2.imshow('face_recognition', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()








