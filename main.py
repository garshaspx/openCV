# amirhosein heidari
# 
# feature extacter
# item detector
# item tracker
# gui interface
# stores data
# uses machine learning to learn data of image
# 
#










import sys
import uuid
import cv2
import os
import tkinter
import sqlite3
import threading
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from ultralytics import YOLO
from datetime import datetime
from PIL import Image, ImageTk




# from cv2 import VideoCapture, cvtColor, imread, convertScaleAbs, COLOR_BGR2GRAY, NORM_L1, BFMatcher, FONT_HERSHEY_PLAIN, imshow, waitKey, destroyAllWindows, xfeatures2d, putText
# from os import getcwd, listdir, mkdir, path
# from numpy import concatenate, loadtxt, float32
# from tkinter import Tk, PhotoImage, Label, Button, Entry, StringVar
# from tkinter.filedialog import askdirectory, askopenfilename
# from tkinter.ttk import Treeview, Scrollbar, Combobox
# from tkinter.messagebox import showerror
# from getpass import getuser
# from pandas import ExcelWriter, DataFrame
# from datetime import datetime
# from PIL import Image, ImageTk








home = os.getcwd() + "\\"
try:
    os.mkdir(home+"ML_train")
except:
    pass
try:
    os.mkdir(home+"ML_train\\train")
except:
    pass
try:   
    os.mkdir(home+"ML_train\\train\\images")
except:
    pass
try:
    os.mkdir(home+"ML_train\\train\\labels")
except:
    pass
try:
    os.mkdir(home+"ML_train\\valid")
except:
    pass
try:
    os.mkdir(home+"ML_train\\valid\\images")
except:
    pass
try:
    os.mkdir(home+"ML_train\\valid\\labels")
except:
    pass




index = 0
arr = []
while True:
    cap = cv2.VideoCapture(index)
    if not cap.read()[0]:
        break
    else:
        arr.append(index)
    cap.release()
    index += 1



win = tkinter.Tk()
win.title("image processor")
win.geometry("400x290")
win.resizable(width=False, height=False)
win.iconphoto(False, tkinter.PhotoImage(file = home + '\\media\\icon.png'))
file_adress = home+"data.txt"


def time():
    now = datetime.now()
    time = now.strftime("%Y_%m_%d_%H_%M_%S")
    return time




try:
    connection = sqlite3.connect(home+'data_center.db')
except:
    pass
try:
    connection.execute(''' CREATE TABLE \"data_center\"
            (code TEXT PRIMARY KEY     NOT NULL,
            name           TEXT    NOT NULL,
            conf            INT     NOT NULL,
            cord        INT,
            time        TEXT);
            ''')
except:
    pass
    # messagebox.showerror("error", "error accured while connecting/creating the database")


# chang txt to sql
# connection.execute(f''' CREATE TABLE DBaddress
#         (code TEXT PRIMARY KEY     NOT NULL,
#         address            INT     NOT NULL);
#          ''')



try:
    open(file_adress).close()
except:
    open(file_adress, "w+")
































#info = [library-address,  video-input, "ON or OFF"]
info = ["None", 0, "ON"]

def library():
    
    global info
    lib_win = tkinter.Tk()
    lib_win.title("library manager")
    lib_win.geometry("410x260")
    lib_win.resizable(width=False, height=False)
    tv = ttk.Treeview(lib_win, columns="number", height=9)
    tv.place(x=0, y=0)
    tv.heading("#0", text="Name")
    tv.heading("number", text="address")
    tv.column('#0', width=90)
    tv.column('number', width=300)
    verscrlbar = ttk.Scrollbar(lib_win, command = tv.yview) 
    verscrlbar.place(x=390, y=0, height=206)
    
    def refresh_lib():
        for i in tv.get_children():     
            tv.delete(i)            
        con_file = open(file_adress, "r")   
        for name, address in enumerate(con_file): 
            temp = address.rstrip().split("==")
            tv.insert('', "end", iid = name, text = temp[0], values = temp[1]) 
        lib_win.update()
    
    refresh_lib()
    
    def add_direc_txt():
        new_library_win = tkinter.Tk()
        new_library_win.title("new library")
        new_library_win.geometry("370x100")
        new_library_win.resizable(width=False, height=False)
        tkinter.Label(new_library_win, text="enter information for new library :").grid(row=0, column=1)
        tkinter.Label(new_library_win, text="enter name :").grid(row=1, column=0)
        tkinter.Label(new_library_win, text="choose address :").grid(row=2, column=0)
        name_entry = tkinter.Entry(new_library_win)
        name_entry.grid(row=1, column=1)
        tkinter.Button(new_library_win, text="choose:", command=lambda : choose_direc()).grid(row=2, column=1) 
        address = "----"
    
        def choose_direc():
            nonlocal address
            file = filedialog.askopenfile(mode='r', filetypes=[('data Files', '*.pt')])

            if file:
                address = os.path.abspath(file.name)
            #tkinter.Label(new_library_win, text= f"chosen library is: {address}").grid(row=2, column=3)
            win.bind('<FocusIn>', win.lower())
    
        def save():
            nonlocal address
            
            con_file = open(file_adress, "a")
            con_file.write(f"{name_entry.get()}=={address}\n")
            con_file.close()
            
            refresh_lib()
            new_library_win.destroy()
            win.bind('<FocusIn>', win.lower())
        tkinter.Button(new_library_win, text="save new data", command= lambda : save()).grid(row=3, column=3)
    
    def delete():
        con_list = []
        con_file = open(file_adress, "r+")
    
        try:
            x = tv.focus()
            int(x)
        except:
            return
    
        for index, i in enumerate(con_file):
            contact = i.rstrip()
            con_list.append(contact)
        con_file = open(file_adress, "w+")
        con_list.pop(int(x))
    
        for i in con_list:
            con_file.write(i+"\n")
        con_file.close()
    
        refresh_lib()
    
    def active():
        ac = int(tv.focus())
        con_file = open(file_adress, "r")
        kk = con_file.readlines()
        info[0] = kk[ac]
        lib_win.destroy()
    
    tkinter.Button(lib_win, text="add library", command=lambda : add_direc_txt()).place(x=40, y=220)
    tkinter.Button(lib_win, text="delete library", command=lambda: delete()).place(x=135, y=220)
    tkinter.Button(lib_win, text="active library", command=lambda: active()).place(x=240, y=220)































def start():
    global info
    if info[0] == "None":
        messagebox.showerror("library error", "choose your library before starting")
        return    
    elif info[1] == False:
        messagebox.showerror("input error", "choose video input")
        return
    win_start = tkinter.Tk()
    win_start.title("image matcher")
    win_start.geometry("300x140")
    win_start.state("normal")
    win.resizable(width=False, height=False)
    tkinter.Label(win_start, text="start matching :").place(x=10, y=20)
    tkinter.Button(win_start, text="start", command=lambda: threading.Thread(target=start_match).start()).place(x=100, y=20)
    tkinter.Label(win_start, text="stop matching :   press Esc on your keyboard").place(x=10, y=90)

    def switch():
        if info[2] == "ON":
            info[2] = "OFF"
            switch_but = tkinter.Button(win_start, text=info[2], command=lambda: switch())
            switch_but.place(x=250, y=45)
            win_start.update()
        else:
            info[2] = "ON"
            switch_but = tkinter.Button(win_start, text=info[2]+" ", command=lambda: switch())
            switch_but.place(x=250, y=45)
            win_start.update()
    switch_lab = tkinter.Label(win_start, text="view mode :")
    switch_lab.place(x=170, y=45)
    switch_but = tkinter.Button(win_start, text=info[2], command=lambda: switch())
    switch_but.place(x=250, y=45)
        
    adds = info[0].rstrip().split("==")
    model = YOLO(adds[1])
    threshold = 0.7  #add threshold option

    if info[1] == "0":
        cap = cv2.VideoCapture(0)
    else:
        cap = cv2.VideoCapture(info[1])
    
    def start_match():        
        global info
        uuid4 = str(uuid.uuid4())
        while True:
            _, frame = cap.read()
            view = frame
            results = model.track(view, persist=True, conf=threshold) #  save_txt=True save data in txt
            result = results[0]
            for box in result.boxes:
                class_id = result.names[box.cls[0].item()]
                cords = box.xyxy[0].tolist()
                cords = [round(x) for x in cords]
                conf = round(box.conf[0].item(), 2)
                id_item = box.cls[0].item()
                if conf >= threshold:
                    view = results[0].plot()
                    try:  
                        connection.execute(f"INSERT INTO \"data_center\" values (\"{uuid4+str(box.id[0].item())}\", \"{class_id}\", {conf}, \"{cords}\", \"{time()}\")")
                        connection.commit()
                        cv2.imwrite(f"{home}ML_train\\train\\images\\{time()}_{class_id}.jpg", frame)
                        open(f"{home}ML_train\\train\\labels\\{time()}_{class_id}.txt", "w+").write(f"{int(id_item)} {((cords[0]+cords[2])/2/frame.shape[1])} {((cords[1]+cords[3])/2/frame.shape[0])} {(cords[2]-cords[0])/frame.shape[1]} {(cords[3]-cords[1])/frame.shape[0]}")#x center y center width hight
                    except:
                        pass
            cv2.imshow("item Tracker", view)        
            if cv2.waitKey(1) == 27 :
                cv2.destroyAllWindows()
                break
        






























        
        # try:
        #     os.mkdir(os.path.join(adds[1], "features"))
        # except:
        #     pass
        # tkinter.Label(win_start, text="library is being procceesed..         ", fg="red").place(x=140, y=20)
        # win_start.update()
        # sift = cv2.xfeatures2d.SIFT_create()
        # for i in os.listdir(adds[1]):
        #     if i[-3:].lower() == "jpg" or i[-3:].lower() == "png":
        #         image = cv2.imread(adds[1]+"\\"+i)
        #         image = cv2.convertScaleAbs(image)
        #         BW_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #         keypoints, descriptors = sift.detectAndCompute(BW_image, None)
        #         with open(adds[1]+"\\"+"features\\"+i[0:-4]+".txt", "w") as file:
        #             for j in descriptors:
        #                 des_numpy = ' '.join(str(validue) for validue in j)
        #                 file.write(des_numpy + '\n')
        #         print(f"image {i} features extracted")
        # tkinter.Label(win_start, text="library proccess finished          ", fg="blue").place(x=140, y=20)
        # win_start.update()
        # txt_list = []
        # for i in os.listdir(adds[1]+"\\"+"features"):
        #     txt_list.append(i)
        # if info[1] == "webcam" or "0":
        #     cam = cv2.VideoCapture(0)
        #     #cam res set
        #     cam.set(3, 640)
        #     cam.set(4, 480)
        # else:
        #     print(info[1])
        #     cam = cv2.VideoCapture(info[1])
        # bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
        # highest_match = [0, 0]
        # while True:
        #     id, frame = cam.read()
        #     frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #     key, des = sift.detectAndCompute(frame_gray, None)            
        #     highest_match[0] = 0
        #     for i in txt_list:
        #         info_mat = np.loadtxt(adds[1]+"\\"+"features"+"\\"+i)
        #         info_mat = info_mat.astype(np.float32)
        #         matches = bf.match(info_mat, des)
        #         if len(matches) > highest_match[0]:
        #             highest_match[0] = len(matches)
        #             highest_match[1] = i
        #     save(highest_match[1][:-4])
        #     if info[2] == "ON" :
        #         image_hm = cv2.imread(adds[1]+"\\"+highest_match[1][:-4]+".jpg")
        #         matcher = np.concatenate((frame, image_hm), axis=1)
        #         cv2.putText(matcher, f"image found: {highest_match[1][:-4]}.jpg", (750, 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
        #         cv2.putText(matcher, "camera", (300, 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)                    
        #         cv2.imshow("two image", matcher)
        #     if cv2.waitKey(1) == 27:
        #         cv2.destroyAllWindows()
        #         break

























def video():
    vid_win = tkinter.Tk()
    vid_win.title("choose video input")
    vid_win.geometry("320x110")
    vid_win.resizable(width=False, height=False)
    tkinter.Label(vid_win, text="choose a camera : ").place(x=20, y=10)
    
    cam_chooser = ttk.Combobox(vid_win, width = 20, textvariable = tkinter.StringVar())
    if arr != []:
        cam_chooser['values'] = arr
        cam_chooser.current(0)
    else:
        info[1] = False
        cam_chooser['values'] = ["no camera found"]
        cam_chooser.current(0)
    cam_chooser.place(x=150, y=10) 
        
    tkinter.Label(vid_win, text="choose a video : ").place(x=20, y=50)
    tkinter.Button(vid_win, text="choose", command=lambda:video_loc()).place(x=180, y=50)    
    tkinter.Button(vid_win, text="save", fg="red", command=lambda:save()).place(x=270, y=50)

    def video_loc():
        info[1] = filedialog.askopenfile(filetypes=[('data Files', '*.mp4')]).name
        win.bind('<FocusIn>', win.lower())
        if info[1][-3:] == "mp4":
            vid_win.destroy()
        else:
            messagebox.showerror("file type", "make sure the file you choose is a mp4")    
    def save():
        info[1] = cam_chooser.get()
        print(info)
        vid_win.destroy()





















# add setting to choose camera and other stuff
def setting():
    s_win = tkinter.Tk()
    s_win.title("setting")
    s_win.geometry("300x150") 
    s_win.resizable(width=False, height=False)
    tkinter.Label(s_win, text="options will be coming soon", fg="red").pack()

    try:
        connection.execute(f''' CREATE TABLE setting
                (pt TEXT PRIMARY KEY     NOT NULL,
                input            INT     NOT NULL);
                ''')    
    except:
        pass























def train():
    train_win = tkinter.Tk()
    train_win.title("train")
    train_win.geometry("300x120")
    train_win.resizable(width=False, height=False)
    tkinter.Label(train_win, text="choose algoritm to train model :").place(x=10, y=10)
    tkinter.Button(train_win, text="choose:", command=lambda : choose_direc()).place(x=210, y=10)
    tkinter.Button(train_win, text="start training", command= lambda : threading.Thread(target=start_train).start()).place(x=200, y=80)
    address = ""

    def choose_direc():
        nonlocal address
        file_ad = filedialog.askopenfile(mode='r', filetypes=[('data Files', '*.pt')])
        if file_ad:
            address = os.path.abspath(file_ad.name)
            tkinter.Label(train_win, text= f"chosen:{address}", fg="red").place(x=10, y=35)
        win.bind('<FocusIn>', win.lower())    
    def start_train():
        nonlocal address
        try:
            model = YOLO(address)
            model.train(data=home + "ML_train\\data.yaml", epochs=30)
        except:
            messagebox.showerror("training error", "make sure all data is correct")
















label = tkinter.Label(win)
label.place(x=-60, y=-30)
image = Image.open(home+"\\media\\item_detec.gif")
frames = []
try:
    while True:
        frames.append(ImageTk.PhotoImage(image))
        image.seek(len(frames))
except EOFError:
    pass
def update_frame(frame_index):
    label.config(image=frames[frame_index])
    win.after(100, update_frame, (frame_index + 1) % len(frames))
update_frame(0)


















labe_intro = tkinter.Label(text="wellcome").place(x=190, y=10)
tkinter.Button(win, text="start", command= lambda : start(), fg="blue").place(x=10, y=50)
tkinter.Button(win, text="choose input", command=lambda: video()).place(x=10, y=85)
tkinter.Button(win, text="library manager", command= lambda : library()).place(x=10, y=120)
tkinter.Button(win, text="ML trainer", command= lambda : train()).place(x=10, y=155)
tkinter.Button(win, text="setting", command= lambda : setting()).place(x=10, y=190)
tkinter.Button(win, text="close", command= lambda : sys.exit("Error message"), fg="red").place(x=10, y=225)

win.mainloop()