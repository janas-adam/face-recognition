import face_recognition

image = face_recognition.load_image_file('./img/known/keanu_reeves.jpg')

image_encoding = face_recognition.face_encodings(image)[0]

unknown = face_recognition.load_image_file('./img/unknown/keanu.jpg')

unknown_encoding = face_recognition.face_encodings(unknown)[0]

# Compare faces

results = face_recognition.compare_faces([image_encoding], unknown_encoding)

if results[0]:
    print('its keanu reeves')
else:
    print('this is not keanu')

