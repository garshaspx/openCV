import cv2
from ultralytics import YOLO


model = YOLO('C:\\Users\\garshasp\\Documents\\best_card_metro_8m.pt')
threshold = 0.8
cap = cv2.VideoCapture(0)


while True:
    success, frame = cap.read()

    if success:
        
        results = model.track(frame, persist=True, conf=threshold) # , save_txt=True,
        
        result = results[0]

        for box in result.boxes:
            class_id = result.names[box.cls[0].item()]
            cords = box.xyxy[0].tolist()
            cords = [round(x) for x in cords]
            conf = round(box.conf[0].item(), 2)


            
            if conf >= threshold:
                frame = results[0].plot()
                
                print("Object type:", class_id)
                print("Coordinates:", cords)
                print("Probability:", conf)
        
        cv2.imshow("YOLOv8 Tracking", frame)
        cv2.waitKey(10)
        
        if cv2.waitKey(1) == 27 :
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()










 
import sqlite3
# create connection by using object
# to connect with hotel_data database
connection = sqlite3.connect('C:\\Users\\garshasp\\Documents\\hotel_data.db')
 
# query to create a table named FOOD1
try:
    connection.execute(''' CREATE TABLE hotel
            (FIND INT PRIMARY KEY     NOT NULL,
            FNAME           TEXT    NOT NULL,
            COST            INT     NOT NULL,
            WEIGHT        INT);
            ''')
except:
    pass
# insert query to insert food  details in
# the above table
connection.execute("INSERT INTO hotel VALUES (13, 'casdkes',800,10 )")
connection.execute("INSERT INTO hotel VALUES (22, 'biscaasduits',100,20 )")
connection.execute("INSERT INTO hotel VALUES (43, 'chocasdos',1000,30 )")
connection.commit()

print("All data in food table\n")
 
# create a cousor object for select query
cursor = connection.execute("SELECT * from hotel ")
 
# display all data from hotel table
for row in cursor:
    print(row)