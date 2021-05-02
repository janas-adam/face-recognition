import face_recognition
from PIL import Image


image = face_recognition.load_image_file('./img/groups/people.jpeg')

face_locations = face_recognition.face_locations(image)

for n, face_location in enumerate(face_locations, start=1):
    top, right, bottom, left = face_location

    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
    pil_image.save(f'./img/pulled_faces/face_{n}.jpg')

