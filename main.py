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
    
    
    for i in tv.get_children():     
        tv.delete(i)            
    con_file = open(file_adress, "r")   
    for name, address in enumerate(con_file): 
        temp = address.rstrip().split("==")
        tv.insert('', "end", iid = name, text = temp[0], values = temp[1]) 
    lib_win.update() #refresh
    

    def add_direc_txt():
     
        new_contact_root = tkinter.Tk()
        new_contact_root.title("new contact")
        new_contact_root.geometry("370x100")
        tkinter.Label(new_contact_root, text="enter information for new contact :").grid(row=0, column=1)
        tkinter.Label(new_contact_root, text="enter name :").grid(row=1, column=0)
        tkinter.Label(new_contact_root, text="enter number :").grid(row=2, column=0)
        name_entry = tkinter.Entry(new_contact_root)
        name_entry.grid(row=1, column=1)
        number_entry = tkinter.Entry(new_contact_root)
        number_entry.grid(row=2, column=1) 
        
        con_file = open(file_adress, "a")
        con_file.write(f"{add_direc()}==sdgh\n")
        con_file.close()

        lib_win.update()
    
    
        tkinter.Button(new_contact_root, text="save new data").grid(row=3, column=3)

    
    
    
    
    lib_but1 = tkinter.Button(lib_win, text="add library", command=lambda : add_direc_txt()).pack()
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