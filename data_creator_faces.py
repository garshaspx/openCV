#
# 
# 
# 
# 
# 
# 
#

from face_recognition import load_image_file, face_encodings, compare_faces, face_distance
from cv2 import VideoCapture, FONT_HERSHEY_DUPLEX, destroyAllWindows, imshow, imwrite, waitKey, rectangle, putText
from numpy import argmin
from os import getcwd, mkdir
from uuid import uuid4




home = getcwd() + "\\"


try:
    mkdir(home+"ML_train")
except:
    pass
try:
    mkdir(home+"ML_train\\train")
except:
    pass
try:   
    mkdir(home+"ML_train\\train\\images")
except:
    pass
try:
    mkdir(home+"ML_train\\train\\labels")
except:
    pass
try:
    mkdir(home+"ML_train\\valid")
except:
    pass
try:
    mkdir(home+"ML_train\\valid\\images")
except:
    pass
try:
    mkdir(home+"ML_train\\valid\\labels")
except:
    pass




cam = VideoCapture("C:\\Users\\amirhosein h\\Desktop\\amir4.mp4")
root_image = load_image_file("C:\\Users\\amirhosein h\\Desktop\\amir4.jpg")
root_encoding = face_encodings(root_image)[0]


known_face_encodings = [root_encoding]
known_face_names = ["amir4"]


i, j = 0, 0

while True:
    
    i += 1
    j += 1
    _, frame = cam.read()
    vieww = frame.copy()

    
    face_locations = face_locations(frame)
    face_encodings = face_encodings(frame, face_locations)
    name = "Unknown"

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

        Uid = str(uuid4())
        matches = compare_faces(known_face_encodings, face_encoding)
        face_distances = face_distance(known_face_encodings, face_encoding)
        best_match_index = argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        
        rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        putText(frame, name, (left + 6, bottom - 6), FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)

        # frame.shape[0] | .frame.shape[1] ____
        if i == 6:
            imwrite(f"{home}ML_train\\valid\\images\\{Uid+name}.jpg", vieww)#     left cord0, right cord1, top cord 2, botton cord 3
            open(f"{home}ML_train\\valid\\labels\\{Uid+name}.txt", "w+").write(f"4 {((left+right)/2)/frame.shape[1]} {((top+bottom)/2)/frame.shape[0]} {(right-left)/frame.shape[1]} {(bottom-top)/frame.shape[0]}")#x center y center width hight
            i = 0
            print(f"{j}/700", "--valid saved", (left, top), (right, bottom))
        else:
            imwrite(f"{home}ML_train\\train\\images\\{Uid+name}.jpg", vieww)#     left cord0, right cord1, top cord 2, botton cord 3
            open(f"{home}ML_train\\train\\labels\\{Uid+name}.txt", "w+").write(f"4 {((left+right)/2)/frame.shape[1]} {((top+bottom)/2)/frame.shape[0]} {(right-left)/frame.shape[1]} {(bottom-top)/frame.shape[0]}")#x center y center width hight
            print(f"{j}/700", "train saved", (left, top), (right, bottom))
    imshow('Video', frame)    
    if waitKey(1) == 27 :
        destroyAllWindows()
        break
