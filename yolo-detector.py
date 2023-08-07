import cv2
import sqlite3
from datetime import datetime
from ultralytics import YOLO

def time():
    now = datetime.now()
    return now.strftime("%Y_%m_%d_%H_%M_%S")
    

model = YOLO('C:\\Users\\garshasp\\Documents\\yolov8m.pt')
threshold = 0.7
cap = cv2.VideoCapture(0)


try:
    connection = sqlite3.connect('C:\\Users\\garshasp\\Documents\\data_center.db')
except:
    print("db already exists")

start_time = time()
connection.execute(f''' CREATE TABLE \"{start_time}\"
        (code INT PRIMARY KEY     NOT NULL,
        name           TEXT    NOT NULL,
        conf            INT     NOT NULL,
        cord        INT,
        time        TEXT);
        ''')


while True:
    _, frame = cap.read()
    view = frame
    results = model.track(view, persist=True, conf=threshold) #  save_txt=True save data in txt
    result = results[0]
    class_id_dict = {}
    for box in result.boxes:
        
        class_id = result.names[box.cls[0].item()]
        cords = box.xyxy[0].tolist()
        cords = [round(x) for x in cords]
        conf = round(box.conf[0].item(), 2)
        id_item = box.cls[0].item()
        
        if conf >= threshold:
            
            view = results[0].plot()
            try:    
                idd = box.id[0].item()
                connection.execute(f"INSERT INTO \"{start_time}\" VALUES ({idd}, \"{class_id}\", {conf}, \"{cords}\", \"{time()}\")")
                connection.commit()
                cv2.imwrite(f"C:\\Users\\garshasp\\Documents\\data_machine\\train\\images\\{time()}_{class_id}.jpg", frame)
                open(f"C:\\Users\\garshasp\\Documents\\data_machine\\train\\labels\\{time()}_{class_id}.txt", "w+").write(f"{int(id_item)} {((cords[0]+cords[2])/2/frame.shape[1])} {((cords[1]+cords[3])/2/frame.shape[0])} {(cords[2]-cords[0])/frame.shape[1]} {(cords[3]-cords[1])/frame.shape[0]}")#x center y center width hight
            except:
                print("id wasnt given, or already exists")
                
    cv2.imshow("item Tracker", view)        
    
    if cv2.waitKey(1) == 27 :
        cv2.destroyAllWindows()
        break