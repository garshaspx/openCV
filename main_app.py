# amirhosein heidari
# feature extacter
# item detector
# item tracker
# gui interface
# stores data
# uses machine learning to learn data of image


#importing all needed librarys, some need to be installed
from sys import exit
from uuid import uuid4
from sqlite3 import connect
from threading import Thread
from ultralytics import YOLO
from datetime import datetime
from PIL import ImageTk, Image
from os import path, mkdir, getcwd
from cv2 import VideoCapture, imshow, waitKey, destroyAllWindows, imwrite
from tkinter import Tk, Label, Button, Entry, StringVar, PhotoImage, messagebox, filedialog, ttk

#creating directory and needed folders
home = getcwd() + "\\"
try:
    mkdir(home+"ML_train")
except:
    pass
try:
    mkdir(home+"ML_train\\train")
except:
    pass
try:   
    mkdir(home+"ML_train\\train\\images")
except:
    pass
try:
    mkdir(home+"ML_train\\train\\labels")
except:
    pass
try:
    mkdir(home+"ML_train\\valid")
except:
    pass
try:
    mkdir(home+"ML_train\\valid\\images")
except:
    pass
try:
    mkdir(home+"ML_train\\valid\\labels")
except:
    pass


index = 0
arr = [] #list of cameras
while True:  #accessing the camera connected to  the system
    cap = VideoCapture(index)
    if not cap.read()[0]:
        break
    else:
        arr.append(index)
    cap.release()
    index += 1

win = Tk() #main tkinter window 
win.title("image processor") #title
win.geometry("400x290")
win.resizable(width=False, height=False) #make its size unchangable
win.iconphoto(False, PhotoImage(file = home + '\\media\\icon.png'))
file_adress = home+"data.txt" #txt file to store data-set locations

def time(): #function to retun time
    now = datetime.now()
    time = now.strftime("%Y_%m_%d_%H_%M_%S")
    return time

try: #opening txt file of data-set locations 
    open(file_adress).close()
except:
    open(file_adress, "w+")



#info = [library-address,  video-input, "ON or OFF"]
info = ["None", 0, "ON"]

def library(): #function to manage library manager window 
    global info
    lib_win = Tk()
    lib_win.title("library manager")
    lib_win.geometry("410x260")
    lib_win.resizable(width=False, height=False)                    #
    tv = ttk.Treeview(lib_win, columns="number", height=9)          # all window options
    tv.place(x=0, y=0)                                              #
    tv.heading("#0", text="Name")
    tv.heading("number", text="address")
    tv.column('#0', width=90)
    tv.column('number', width=300)
    verscrlbar = ttk.Scrollbar(lib_win, command = tv.yview) 
    verscrlbar.place(x=390, y=0, height=206)
    
    def refresh_lib(): #function to refresh the window
        for i in tv.get_children():     
            tv.delete(i)            
        con_file = open(file_adress, "r")   
        for name, address in enumerate(con_file): 
            temp = address.rstrip().split("==")
            tv.insert('', "end", iid = name, text = temp[0], values = temp[1]) 
        lib_win.update()
    refresh_lib()
    
    def add_direc_txt():          #window to add new library
        new_library_win = Tk()
        new_library_win.title("new library")
        new_library_win.geometry("370x100")
        new_library_win.resizable(width=False, height=False)
        Label(new_library_win, text="enter information for new library :").grid(row=0, column=1)
        Label(new_library_win, text="enter name :").grid(row=1, column=0)
        Label(new_library_win, text="choose address :").grid(row=2, column=0)
        name_entry = Entry(new_library_win)
        name_entry.grid(row=1, column=1)
        Button(new_library_win, text="choose:", command=lambda : choose_direc()).grid(row=2, column=1) 
        address = "----"
    
        def choose_direc():
            nonlocal address
            file = filedialog.askopenfile(mode='r', filetypes=[('data Files', '*.pt')])

            if file:
                address = path.abspath(file.name)
            #Label(new_library_win, text= f"chosen library is: {address}").grid(row=2, column=3)
            win.bind('<FocusIn>', win.lower())                   #puting the main window behind
    
        def save():                #saaving the data in txt file and closing new lib window
            nonlocal address
            con_file = open(file_adress, "a")
            con_file.write(f"{name_entry.get()}=={address}\n")
            con_file.close()
            refresh_lib()
            new_library_win.destroy()
            win.bind('<FocusIn>', win.lower()) #puting the main window behind
        Button(new_library_win, text="save new data", command= lambda : save()).grid(row=3, column=3)
    
    def delete():     #function to delete a library from the list
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
    
    def active():                  #function to make a specific library active  
        ac = int(tv.focus())
        con_file = open(file_adress, "r")
        kk = con_file.readlines()
        info[0] = kk[ac]
        lib_win.destroy() 
    Button(lib_win, text="add library", command=lambda : add_direc_txt()).place(x=40, y=220)
    Button(lib_win, text="delete library", command=lambda: delete()).place(x=135, y=220)
    Button(lib_win, text="active library", command=lambda: active()).place(x=240, y=220)













def video():        #func to choose video input 
    vid_win = Tk()
    vid_win.title("choose video input")
    vid_win.geometry("320x110")
    vid_win.resizable(width=False, height=False)
    Label(vid_win, text="choose a camera : ").place(x=20, y=10)
    
    cam_chooser = ttk.Combobox(vid_win, width = 20, textvariable = StringVar()) #creating a combobox
    if arr != []:  #adding cams to combobox
        cam_chooser['values'] = arr
        cam_chooser.current(0)
    else:
        info[1] = False
        cam_chooser['values'] = ["no camera found"]
        cam_chooser.current(0)
    cam_chooser.place(x=150, y=10) 
        
    Label(vid_win, text="choose a video : ").place(x=20, y=50)
    Button(vid_win, text="choose", command=lambda:video_loc()).place(x=180, y=50)    
    Button(vid_win, text="save", fg="red", command=lambda:save()).place(x=270, y=50)

    def video_loc():    #choosing video file from hard drive
        info[1] = filedialog.askopenfile(filetypes=[('data Files', '*.mp4')]).name #file has to be mp4
        win.bind('<FocusIn>', win.lower())
        if info[1][-3:] == "mp4": 
            vid_win.destroy()
        else:
            messagebox.showerror("file type", "make sure the file you choose is a mp4")    
    def save():  #saving
        info[1] = cam_chooser.get()
        vid_win.destroy()













def start():           #main func to start the program and start window
    global info
    
    
    if info[0] == "None": #incase input and data-set wasnt choosen
        messagebox.showerror("library error", "choose your library before starting")
        return    
    elif info[1] == False:
        messagebox.showerror("input error", "choose video input")
        return
    
    win_start = Tk()  #creating start window
    win_start.title("image matcher")
    win_start.geometry("300x140")
    win_start.state("normal")
    win.resizable(width=False, height=False) #make its size unchangeable
    Label(win_start, text="start matching :").place(x=10, y=20)
    Button(win_start, text="start", command=lambda: Thread(target=start_match).start()).place(x=100, y=20)
    Label(win_start, text="stop matching :   press Esc on your keyboard").place(x=10, y=90)

    def switch():          #option to make view mode on or off
        if info[2] == "ON":
            info[2] = "OFF"
            switch_but = Button(win_start, text=info[2], command=lambda: switch())
            switch_but.place(x=250, y=45)
            win_start.update()
        else:
            info[2] = "ON"
            switch_but = Button(win_start, text=info[2]+" ", command=lambda: switch())
            switch_but.place(x=250, y=45)
            win_start.update()
    switch_lab = Label(win_start, text="view mode :")
    switch_lab.place(x=170, y=45)
    switch_but = Button(win_start, text=info[2], command=lambda: switch())
    switch_but.place(x=250, y=45)
        
    adds = info[0].rstrip().split("==") 
    model = YOLO(adds[1]) #loading data-set
    threshold = 0.7  #add threshold option

    if info[1] == "0": #loading webcam
        cap = VideoCapture(0)
    else:
        cap = VideoCapture(info[1])
    
    def start_match():        #starting the main prosec
        global info
        connection = connect(home+'data_center.db')          #connecting to data base
        
        try:     #createa a table incase it doesnt have it
            connection.execute(''' CREATE TABLE \"data_center\"
                    (code TEXT PRIMARY KEY     NOT NULL,
                    name           TEXT    NOT NULL,
                    conf            INT     NOT NULL,
                    cord        INT,
                    time        TEXT);
                    ''')
        except:
            pass
        
        uuid = str(uuid4()) #create a uniqe id , its used in database
        while True: #main loop 
            _, frame = cap.read()
            view = frame 
            
            results = model.track(view, persist=True, conf=threshold)#proccessing the frame              #  save_txt=True save data in txt
            result = results[0] 
            
            for box in result.boxes:         # puting bouding box around found items
                
                class_id = result.names[box.cls[0].item()]
                cords = [round(x) for x in box.xyxy[0].tolist()]
                conf = round(box.conf[0].item(), 2)
                id_item = box.cls[0].item()
                
                if conf >= threshold:        #threshold if
                    view = results[0].plot()
                
                    try:   # storing data in database and saving image and labels for training
                        connection.execute(f"INSERT INTO \"data_center\" values (\"{uuid+str(box.id[0].item())}\", \"{class_id}\", {conf}, \"{cords}\", \"{time()}\")")           
                        connection.commit()
                        imwrite(f"{home}ML_train\\train\\images\\{time()}_{class_id}.jpg", frame)
                        open(f"{home}ML_train\\train\\labels\\{time()}_{class_id}.txt", "w+").write(f"{int(id_item)} {((cords[0]+cords[2])/2)/frame.shape[1]} {((cords[1]+cords[3])/2)/frame.shape[0]} {(cords[2]-cords[0])/frame.shape[1]} {(cords[3]-cords[1])/frame.shape[0]}")#x center y center width hight
                    except:
                        pass
       
            imshow("item Tracker", view)        #showing it live
            if waitKey(1) == 27 : #close the windows by taping Esc
                destroyAllWindows()
                break







def train():    #creating tkinter window to train a new data-set
    train_win = Tk()
    train_win.title("train")
    train_win.geometry("300x120")
    # train_win.resizable(width=False, height=False)
    Label(train_win, text="choose algoritm to train model :").place(x=10, y=10)
    Button(train_win, text="choose:", command=lambda : choose_direc()).place(x=210, y=10)
    Button(train_win, text="start training", command= lambda : Thread(target=start_train).start()).place(x=200, y=80)
    Button(train_win, text="stop training", bg="red" ,command= lambda : stop_tain()).place(x=100, y=80)
    address = ""
    def choose_direc():  #loading training algoritm
        nonlocal address
        file_ad = filedialog.askopenfile(mode='r', filetypes=[('data Files', '*.pt')])
        if file_ad:
            address = path.abspath(file_ad.name)
            Label(train_win, text= f"chosen:{address}", fg="red").place(x=10, y=35)
        win.bind('<FocusIn>', win.lower())
    def start_train(): 
        nonlocal address
        try:
            model = YOLO(address)
            model.train(data=home + "ML_train\\data.yaml", epochs=30)
        except:
            messagebox.showerror("training error", "make sure all data is correct")
    def stop_tain():
        # add terminate option
        # x.terminate()
        return










# add setting to choose camera and other stuff
def setting():
    s_win = Tk()
    s_win.title("setting")
    s_win.geometry("300x150") 
    s_win.resizable(width=False, height=False)
    Label(s_win, text="options will be coming soon", fg="red").pack()
    connection = connect(home+'data_center.db')
    try:
        connection.execute(f''' CREATE TABLE setting
                (pt TEXT PRIMARY KEY     NOT NULL,
                input            INT     NOT NULL);
                ''')    
    except:
        pass








# tkinter backgroung and icon

label = Label(win)
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


labe_intro = Label(text="wellcome").place(x=190, y=10)
Button(win, text="start", command= lambda : start(), fg="blue").place(x=10, y=50)
Button(win, text="choose input", command=lambda: video()).place(x=10, y=85)
Button(win, text="library manager", command= lambda : library()).place(x=10, y=120)
Button(win, text="ML trainer", command= lambda : train()).place(x=10, y=155)
Button(win, text="setting", command= lambda : setting()).place(x=10, y=190)
Button(win, text="close", command= lambda : quit(), fg="red").place(x=10, y=225)

win.mainloop()