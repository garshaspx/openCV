
from ultralytics import YOLO

model = YOLO()

print("start")

model.train(data="C:\\Users\\garshasp\\Desktop\\data.yaml", epochs=32)


print("finished")