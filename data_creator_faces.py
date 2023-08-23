#
# 
# 
# 
# 
# 
# 
#

import face_recognition
import cv2
import numpy
import os
import uuid




home = os.getcwd() + "\\"


try:
    os.mkdir(home+"ML_train")
except:
    pass
try:
    os.mkdir(home+"ML_train\\train")
except:
    pass
try:   
    os.mkdir(home+"ML_train\\train\\images")
except:
    pass
try:
    os.mkdir(home+"ML_train\\train\\labels")
except:
    pass
try:
    os.mkdir(home+"ML_train\\valid")
except:
    pass
try:
    os.mkdir(home+"ML_train\\valid\\images")
except:
    pass
try:
    os.mkdir(home+"ML_train\\valid\\labels")
except:
    pass




cam = cv2.VideoCapture("C:\\Users\\amirhosein h\\Desktop\\amir4.mp4")
root_image = face_recognition.load_image_file("C:\\Users\\amirhosein h\\Desktop\\amir4.jpg")
root_encoding = face_recognition.face_encodings(root_image)[0]


known_face_encodings = [root_encoding]
known_face_names = ["amir4"]


i, j = 0, 0

while True:
    
    i += 1
    j += 1
    _, frame = cam.read()
    vieww = frame.copy()

    
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    name = "Unknown"

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

        Uid = str(uuid.uuid4())
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = numpy.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)

        # frame.shape[0] | .frame.shape[1] ____
        if i == 6:
            cv2.imwrite(f"{home}ML_train\\valid\\images\\{Uid+name}.jpg", vieww)#     left cord0, right cord1, top cord 2, botton cord 3
            open(f"{home}ML_train\\valid\\labels\\{Uid+name}.txt", "w+").write(f"4 {((left+right)/2)/frame.shape[1]} {((top+bottom)/2)/frame.shape[0]} {(right-left)/frame.shape[1]} {(bottom-top)/frame.shape[0]}")#x center y center width hight
            i = 0
            print(f"{j}/700", "--valid saved", (left, top), (right, bottom))
        else:
            cv2.imwrite(f"{home}ML_train\\train\\images\\{Uid+name}.jpg", vieww)#     left cord0, right cord1, top cord 2, botton cord 3
            open(f"{home}ML_train\\train\\labels\\{Uid+name}.txt", "w+").write(f"4 {((left+right)/2)/frame.shape[1]} {((top+bottom)/2)/frame.shape[0]} {(right-left)/frame.shape[1]} {(bottom-top)/frame.shape[0]}")#x center y center width hight
            print(f"{j}/700", "train saved", (left, top), (right, bottom))
    cv2.imshow('Video', frame)    
    if cv2.waitKey(1) == 27 :
        cv2.destroyAllWindows()
        break
