from ultralytics import YOLO
import cv2
model = YOLO("yolov8m.pt")


cam = cv2.VideoCapture(0)

address = "cat_dog1.jpg"
while True:
    
    id, image = cam.read()
    results = model.predict(image)
    result = results[0]


    #image = cv2.imread(address)

    for box in result.boxes:
        class_id = result.names[box.cls[0].item()]
        cords = box.xyxy[0].tolist()
        cords = [round(x) for x in cords]
        conf = round(box.conf[0].item(), 2)
    
    
        cv2.rectangle(image, (cords[0], cords[1]), (cords[2], cords[3]), 255, 2)
    
        
        print("Object type:", class_id)
        print("Coordinates:", cords)
        print("Probability:", conf)
        print("---")



    print(result.names)
    """
    from PIL import Image
    Image.fromarray(result.plot()[:,:,::-1])"""



    cv2.imshow("test", image)
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        break
