import face_recognition
from PIL import Image, ImageDraw


image_of_keanu = face_recognition.load_image_file('./img/known/keanu_reeves.jpg')
keanu_encoding = face_recognition.face_encodings(image_of_keanu)[0]

image_of_steve = face_recognition.load_image_file('./img/known/steve_jobs.jpg')
steve_encoding = face_recognition.face_encodings(image_of_steve)[0]

# Create array of encodings and names
known_face_encodings = [
    keanu_encoding,
    steve_encoding
]

known_face_names = [
    "Keanu Reeves",
    "Steve Jobs"
]

test_image = face_recognition.load_image_file('./img/groups/keanu_steve.jpg')

# Find faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Convert to PIL format
pil_image = Image.fromarray(test_image)

# Create a ImageDraw instance
draw = ImageDraw.Draw(pil_image)

for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unkown Person"

    # If match
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Draw Box
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 0))

    # Draw label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 0), outline=(0, 0, 0))

    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255))

del draw

# Display image
pil_image.show()

# Save Image
pil_image.save('./img/indentified_faces/identify.jpg')



