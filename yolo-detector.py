import cv2
import sqlite3
from datetime import datetime
from ultralytics import YOLO




model = YOLO('C:\\Users\\garshasp\\Documents\\best_card_metro_8m.pt')
threshold = 0.7
cap = cv2.VideoCapture(0)



try:
    connection = sqlite3.connect('C:\\Users\\garshasp\\Documents\\data_center.db')
except:
    pass
try:
    connection.execute(''' CREATE TABLE hotel
            (code INT PRIMARY KEY     NOT NULL,
            name           TEXT    NOT NULL,
            conf            INT     NOT NULL,
            cord        INT,
            time        TEXT);
            ''')
except:
    pass



def time():
    now = datetime.now()
    time = now.strftime("%Y_%m_%d_%H_%M_%S")
    return time




while True:

    id, frame = cap.read()
    results = model.track(frame, persist=True, conf=threshold) #  save_txt=True save data in txt
    result = results[0]

    for box in result.boxes:
        print("gffffffffffffff")
        print(box)
        print("gffffffffffffff")
        class_id = result.names[box.cls[0].item()]
        cords = box.xyxy[0].tolist()
        cords = [round(x) for x in cords]
        conf = round(box.conf[0].item(), 2)
        

            
        if conf >= threshold:
            frame = results[0].plot()
            try:
                idd = box.id[0].item()
            except:
                pass
            try:
                connection.execute(f"INSERT INTO hotel VALUES ({idd}, \"{class_id}\", {conf}, \"{cords}\", \"{time()}\")")
                connection.commit()
            except:
                pass
        print("Object type:", class_id)
        print("Coordinates:", cords)
        print("Probability:", conf)
        print("id : ", idd)
        

        
        
        
    cv2.imshow("item Tracker", frame)        
    
    if cv2.waitKey(1) == 27 :
        cv2.destroyAllWindows()
        break



