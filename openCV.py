#find most similar from a library
#and save info in exel
#
#
#
#
#
import cv2
import os
import numpy as np
import pandas as pd
#import time
from datetime import datetime


#print(time.localtime())

address = "C:\\Users\\garshasp\\pictures"
sift = cv2.xfeatures2d.SIFT_create()

# extracting features
for i in os.listdir(address):
    if i[-3:].lower() == "jpg" or i[-3:].lower() == "png":
        image = cv2.imread(address+"\\"+i)
        image = cv2.convertScaleAbs(image)
        BW_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        keypoints, descriptors = sift.detectAndCompute(BW_image, None)
        with open(address+"\\"+"features\\"+i[0:-4]+".txt", "w") as file:
            for j in descriptors:
                des_numpy = ' '.join(str(value) for value in j)
                file.write(des_numpy + '\n')
        print(f"image {i} completed")




# data center func
excel_address = "C:\\Users\\garshasp\\Documents\\openCV_datacenter.xlsx"
df = pd.read_excel(excel_address)

def save(img):
    
    now = datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    
    df[len(df.index)] = {"time":time, "image":img}
    
    print(df)
    with pd.ExcelWriter(excel_address, engine="auto") as excel:
        df.to_excel(excel, sheet_name="image_info")















    
    
#matching features  
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
cam = cv2.VideoCapture(0)
highest_match = [0, 0]

while True:
    
    id, image = cam.read()
    BW_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    key, des = sift.detectAndCompute(BW_image, None)



    highest_match[0] = 0
    for i in os.listdir(address+"\\"+"features"):
        info = np.loadtxt(address+"\\"+"features"+"\\"+i)
        info = info.astype(np.float32)
        #print(i, "  checked")
        bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
        matches = bf.match(info, des)
        matches = sorted(matches, key=lambda x: x.distance)
        if len(matches) > highest_match[0]:
            highest_match[0] = len(matches)
            highest_match[1] = i
            #print("highest chatged to ", i)
    save(highest_match[1][:-4])

    image_hm = cv2.imread(address+"\\"+highest_match[1][:-4]+".jpg")
    Hori = np.concatenate((image, image_hm), axis=1)
    
    cv2.imshow("two image", Hori)
    cv2.waitKey(1)