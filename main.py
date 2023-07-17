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


































win = tkinter.Tk()
win.title("image processor")
win.geometry("400x270")

labe_intro = tkinter.Label(text="wellcome").pack()
file_adress = "C:\\Users\\"+getuser()+"\Documents\data.txt"

try:
    open(file_adress).close()
except:
    open(file_adress, "w+")





































def library():
    lib_win = tkinter.Tk()
    lib_win.title("library manager")
    lib_win.geometry("409x260")    
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
    tkinter.Button(lib_win, text="add library", command=lambda : add_direc_txt()).place(x=50, y=220)
    tkinter.Button(lib_win, text="delete library", command=lambda: delete()).place(x=150, y=220)

    








































def setting():
    
    S_win = tkinter.Tk()
    S_win.title("setting")
    S_win.geometry("300x150")
    
    
    """
    add setting to choose camera and other stuff
    """    
    print("setting opened")






























def start():
    
    print("start main")
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

        
    
    print(arr)
    
    
    
    
    
    
    
    
    











but1 = tkinter.Button(win, text="start", command= lambda : start()).pack()
but2 = tkinter.Button(win, text="library manager", command= lambda : library()).pack()
but3 = tkinter.Button(win, text="setting", command= lambda : setting()).pack()

win.mainloop()