
from ultralytics import YOLO

model = YOLO("C:\\Users\\garshasp\Documents\\yolov8x.pt")

print("start")

model.train(data="C:\\Users\\garshasp\\Desktop\\data.yaml", epochs=30)


print("finished")