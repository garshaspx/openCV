import face_recognition
import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)

root_image = face_recognition.load_image_file("C:\\Users\\garshasp\\Pictures\\WIN_20230710_12_47_28_Pro.jpg")
root_encoding = face_recognition.face_encodings(root_image)[0]
root_image2 = face_recognition.load_image_file("C:\\Users\\garshasp\\Pictures\\photo_2023-07-10_14-01-14.jpg")
root_encoding2 = face_recognition.face_encodings(root_image2)[0]

known_face_encodings = [root_encoding, root_encoding2]
known_face_names = ["garshasp", "ali"]

while True:
    
    ret, frame = video_capture.read()
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    name = "Unknown"

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)
    cv2.imshow('Video', frame)
    cv2.waitKey(1)