from ultralytics import YOLO
import cv2

model = YOLO("C:\\Users\\garshasp\\Documents\\best_4_items.pt")


cam = cv2.VideoCapture(0)

list_item = []

while True:
    
    id, image = cam.read()
    results = model.predict(image)
    result = results[0]

    for box in result.boxes:

        class_id = result.names[box.cls[0].item()]
        cords = box.xyxy[0].tolist()
        cords = [round(x) for x in cords]
        conf = round(box.conf[0].item(), 2)
        
        if conf >= 0.6:
            cv2.rectangle(image, (cords[0], cords[1]), (cords[2], cords[3]), 255, 2)
            cv2.putText(image, f"{class_id} {int(conf*100)}", (cords[0], cords[1]-10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)   
            
            list_item.append((class_id, conf))
            
            
        print("Object type:", class_id)
        print("Coordinates:", cords)
        print("Probability:", conf)
    cv2.imshow("test", image)    

    if cv2.waitKey(10) == 27:
        cv2.destroyAllWindows()
        break
    
    
for i in list_item:
    print(i)
    
    
    
    

    