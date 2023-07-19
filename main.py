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
















  







import tkinter
from tkinter import filedialog
from tkinter import ttk
from getpass import getuser
import cv2
from tkinter import messagebox
import os
































win = tkinter.Tk()
win.title("image processor")
win.geometry("450x270")

labe_intro = tkinter.Label(text="wellcome").pack()
file_adress = "C:\\Users\\"+getuser()+"\Documents\data.txt"

try:
    open(file_adress).close()
except:
    open(file_adress, "w+")

































#info = [library-address,  video-input]
info = ["None", "None"]


def library():
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
        tkinter.Label(win, text=f"library is now active : {info[0]}").pack()
        win.update()
    tkinter.Button(lib_win, text="add library", command=lambda : add_direc_txt()).place(x=40, y=220)
    tkinter.Button(lib_win, text="delete library", command=lambda: delete()).place(x=135, y=220)
    tkinter.Button(lib_win, text="active library", command=lambda: active()).place(x=240, y=220)

    



























sift = cv2.xfeatures2d.SIFT_create()



def start():
    print("main program")
    
 #   if info[0] == "None" or info[1] == "None":
  #      print("FGN")
   #     messagebox.showerror("error", "choose your library and input first")
#        return

    adds = info[0].rstrip().split("==")
    os.mkdir(os.path.join(adds[1], "features"))
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
    



    



































def video():
    vid_win = tkinter.Tk()
    vid_win.title("choose video input")
    vid_win.geometry("320x110")
    tkinter.Label(vid_win, text="choose a camera : ").place(x=20, y=10)
    cam_chooser = ttk.Combobox(vid_win, width = 20, textvariable = tkinter.StringVar())
    
    #fill the camera list 
    #add it
    
    cam_chooser['values'] = (' webcam', ' cam 14', ' cam 32c')    
    cam_chooser.place(x=150, y=10)
    cam_chooser.current(0)
    tkinter.Label(vid_win, text="choose a video : ").place(x=20, y=50)
    tkinter.Button(vid_win, text="choose", command=lambda:video_loc()).place(x=200, y=50)    
    tkinter.Button(vid_win, text="save", fg="red", command=lambda:save()).place(x=270, y=80)


    def video_loc():
        info[1] = filedialog.askopenfilename()    
        win.bind('<FocusIn>', win.lower())
        if info[1][-3:] == "mp4":
            tkinter.Label(win, text=info).pack()
            win.update()
            vid_win.destroy()
        else:
            messagebox.showerror("file type", "make sure the file you choose is a mp4")
    def save():
        info[1] = cam_chooser.get()
        vid_win.destroy()








































def setting():
    
    S_win = tkinter.Tk()
    S_win.title("setting")
    S_win.geometry("300x150")
    
    
    """
    add setting to choose camera and other stuff
    """    
    print("setting opened")
    

def starxnxfnt():
    # checks the first 10 indexes.
    index = 0
    arr = []
    i = 10
    while i > 0:
        cap = cv2.VideoCapture(index)
        if cap.read()[0]:
            arr.append(index)
            cap.release()
        index += 1
        i -= 1
    print(arr)











tkinter.Button(win, text="start", command= lambda : start()).pack()
tkinter.Button(win, text="choose input", command=lambda: video()).pack()
tkinter.Button(win, text="library manager", command= lambda : library()).pack()
tkinter.Button(win, text="setting", command= lambda : setting()).pack()

win.mainloop()