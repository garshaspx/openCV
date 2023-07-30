# amirhosein heidari
# 
# feature extacter
# item detector 
# item tracker
# gui interface
# stores data
# 
# 
#








import cv2
import os
import numpy as np
import tkinter
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from getpass import getuser
import pandas as pd
from datetime import datetime
from PIL import Image, ImageTk









"""
from cv2 import VideoCapture, cvtColor, imread, convertScaleAbs, COLOR_BGR2GRAY, NORM_L1, BFMatcher, FONT_HERSHEY_PLAIN, imshow, waitKey, destroyAllWindows, xfeatures2d, putText
from os import getcwd, listdir, mkdir, path
from numpy import concatenate, loadtxt, float32
from tkinter import Tk, PhotoImage, Label, Button, Entry, StringVar
from tkinter.filedialog import askdirectory, askopenfilename
from tkinter.ttk import Treeview, Scrollbar, Combobox
from tkinter.messagebox import showerror
from getpass import getuser
from pandas import ExcelWriter, DataFrame
from datetime import datetime
from PIL import Image, ImageTk
"""








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

win.iconphoto(False, tkinter.PhotoImage(file = os.getcwd() + '\\icon.png'))
file_adress = "C:\\Users\\"+getuser()+"\Documents\data.txt"

try:
    open(file_adress).close()
except:
    open(file_adress, "w+")
















def time():
    now = datetime.now()
    time = now.strftime("%Y_%m_%d_%H_%M_%S")
    return time

































#info = [library-address,  video-input, "ON or OFF"]
info = ["None", 0, "ON"]

def library():
    global info
    lib_win = tkinter.Tk()
    lib_win.title("library manager")
    lib_win.geometry("410x260")    
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
        tkinter.Label(new_library_win, text="enter information for new library :").grid(row=0, column=1)
        tkinter.Label(new_library_win, text="enter name :").grid(row=1, column=0)
        tkinter.Label(new_library_win, text="choose address :").grid(row=2, column=0)
        name_entry = tkinter.Entry(new_library_win)
        name_entry.grid(row=1, column=1)
        tkinter.Button(new_library_win, text="choose:", command=lambda : choose_direc()).grid(row=2, column=1) 
        address = "----"
        def choose_direc():
            nonlocal address
            address = filedialog.askdirectory()
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
        messagebox.showerror("error", "choose your library before starting\n video input is webcam by default")
        return    
    win_start = tkinter.Tk()
    win_start.title("image matcher")
    win_start.geometry("300x140")    
    tkinter.Label(win_start, text="start matching :").place(x=10, y=20)
    tkinter.Button(win_start, text="start", command=lambda: start_match()).place(x=100, y=20)
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
    
    lib_name =info[0].rstrip().split("==")[0]
    
    excel_address = "C:\\Users\\" + getuser() + "\\Documents\\"+lib_name+"--"+time()+".xlsx"
    df = pd.DataFrame(columns=["time", "image", "ID"])

    def save(img):    
        if len(df.index) > 0 and df.loc[len(df.index)-1][1] == img :
            return
        df.loc[len(df.index)] = [time(), img, None]
        with pd.ExcelWriter(excel_address, engine="auto") as excel:
            df.to_excel(excel, sheet_name=lib_name)

        
    def start_match():        
        global info
        adds = info[0].rstrip().split("==")
        try:
            os.mkdir(os.path.join(adds[1], "features"))
        except:
            None
        tkinter.Label(win_start, text="library is being procceesed..         ", fg="red").place(x=140, y=20)
        win_start.update()
        sift = cv2.xfeatures2d.SIFT_create()
        for i in os.listdir(adds[1]):
            if i[-3:].lower() == "jpg" or i[-3:].lower() == "png":
                image = cv2.imread(adds[1]+"\\"+i)
                image = cv2.convertScaleAbs(image)
                BW_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                keypoints, descriptors = sift.detectAndCompute(BW_image, None)
                with open(adds[1]+"\\"+"features\\"+i[0:-4]+".txt", "w") as file:
                    for j in descriptors:
                        des_numpy = ' '.join(str(value) for value in j)
                        file.write(des_numpy + '\n')
                print(f"image {i} features extracted")
        tkinter.Label(win_start, text="library proccess finished          ", fg="blue").place(x=140, y=20)
        win_start.update()
        set
        txt_list = []
        for i in os.listdir(adds[1]+"\\"+"features"):
            txt_list.append(i)
        if info[1] == "webcam" or "0":
            cam = cv2.VideoCapture(0)
            
            #cam res set
            cam.set(3, 640)
            cam.set(4, 480)
            
        else:
            print(info[1])
            cam = cv2.VideoCapture(info[1])
        bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
        highest_match = [0, 0]
        while True:
            id, frame = cam.read()
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            key, des = sift.detectAndCompute(frame_gray, None)            
            highest_match[0] = 0
            for i in txt_list:
                info_mat = np.loadtxt(adds[1]+"\\"+"features"+"\\"+i)
                info_mat = info_mat.astype(np.float32)
                matches = bf.match(info_mat, des)
                if len(matches) > highest_match[0]:
                    highest_match[0] = len(matches)
                    highest_match[1] = i
            save(highest_match[1][:-4])
            if info[2] == "ON" :
                image_hm = cv2.imread(adds[1]+"\\"+highest_match[1][:-4]+".jpg")
                matcher = np.concatenate((frame, image_hm), axis=1)
                cv2.putText(matcher, f"image found: {highest_match[1][:-4]}.jpg", (750, 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
                cv2.putText(matcher, "camera", (300, 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)                    
                cv2.imshow("two image", matcher)
            if cv2.waitKey(1) == 27:
                cv2.destroyAllWindows()
                break

























































def video():
    vid_win = tkinter.Tk()
    vid_win.title("choose video input")
    vid_win.geometry("320x110")
    tkinter.Label(vid_win, text="choose a camera : ").place(x=20, y=10)
    cam_chooser = ttk.Combobox(vid_win, width = 20, textvariable = tkinter.StringVar())

    #fill the camera list 
    #add it
    cam_chooser['values'] = arr  
    cam_chooser.place(x=150, y=10)
    cam_chooser.current(0)
    tkinter.Label(vid_win, text="choose a video : ").place(x=20, y=50)
    tkinter.Button(vid_win, text="choose", command=lambda:video_loc()).place(x=180, y=50)    
    tkinter.Button(vid_win, text="save", fg="red", command=lambda:save()).place(x=270, y=50)

    def video_loc():
        info[1] = filedialog.askopenfilename()    
        win.bind('<FocusIn>', win.lower())
        if info[1][-3:] == "mp4":
            vid_win.destroy()
        else:
            messagebox.showerror("file type", "make sure the file you choose is a mp4")    
    def save():
        info[1] = cam_chooser.get()
        vid_win.destroy()























































def setting():
    s_win = tkinter.Tk()
    s_win.title("setting")
    s_win.geometry("300x150") 
    
    tkinter.Label(s_win, text="options will be coming soon", fg="red").pack()
    """
    add setting to choose camera and other stuff
    """    
    print("setting opened")
















































label = tkinter.Label(win)
label.place(x=-60, y=-30)
image = Image.open(os.getcwd()+"\\item_detec.gif")
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
tkinter.Button(win, text="start", command= lambda : start(), fg="blue").place(x=10, y=60)
tkinter.Button(win, text="choose input", command=lambda: video()).place(x=10, y=95)
tkinter.Button(win, text="library manager", command= lambda : library()).place(x=10, y=130)
tkinter.Button(win, text="setting", command= lambda : setting()).place(x=10, y=165)
tkinter.Button(win, text="close", command= lambda : quit(), fg="red").place(x=10, y=200)

win.mainloop()