import cv2
is_working = True
dev_port = 0
arr = []
while is_working:
    camera = cv2.VideoCapture(dev_port)
    if not camera.isOpened():
        is_working = False
        print("Port %s is not working." %dev_port)
    else:
        is_reading, img = camera.read()
        w = camera.get(3)
        h = camera.get(4)
        if is_reading:
            print("Port %s is working and reads images (%s x %s)" %(dev_port,h,w))
            arr.append(dev_port)
    dev_port +=1

print(arr)
input("")