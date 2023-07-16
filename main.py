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
    lib_win.geometry("315x260")
    
    tv = ttk.Treeview(lib_win, columns="number", height=9)
    tv.place(x=0, y=0)
    tv.heading("#0", text="Name")
    tv.heading("number", text="number")
    tv.column('#0', width=150)
    tv.column('number', width=150)
    verscrlbar = ttk.Scrollbar(lib_win, command = tv.yview) 
    verscrlbar.place(x=295, y=0, height=206)
    
    def add_direc():
        x = filedialog.askdirectory()
        return x
    for i in tv.get_children():      #clearing treeview
        tv.delete(i)            
    con_file = open(file_adress, "r")   #reading file 
    for name, address in enumerate(con_file): #re-adding new items
        temp = address.rstrip().split("==")
        tv.insert('', "end", iid = name, text = temp[0], values = temp[1]) #adding items to treeview
    lib_win.update() #refresh
    
    con_file = open(file_adress, "a")
    con_file.write(f"{add_direc}==sdgh\n")#adds name to txt file
    con_file.close()
    
    
    lib_but1 = tkinter.Button(lib_win, text="add library").pack()
    lib_but2 = tkinter.Button(lib_win, text="delete library").pack()
    #lib_but3 = tkinter.Button(lib_win, text="add library").pack()
    




def setting():
    
    S_win = tkinter.Tk()
    S_win.title("setting")
    S_win.geometry("300x150")
    
    
    """
    add setting to choose camera and other stuff
    """    
    print("setting opened")




























but1 = tkinter.Button(win, text="start", command= lambda : print("424")).pack()
but2 = tkinter.Button(win, text="library manager", command= lambda : library()).pack()
but3 = tkinter.Button(win, text="setting", command= lambda : setting()).pack()





win.mainloop()