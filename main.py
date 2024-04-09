__author__ = "Shubham Kuchankar"
import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog

main = Tk()
main.geometry("1366x768")
main.title("Ganesh Nutrition")
main.resizable(0, 0)
main.configure(bg='black')
main.wm_iconbitmap("Icon.ico")

def Exit():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=main)
    if sure == True:
        main.destroy()
        
main.protocol("WM_DELETE_WINDOW", Exit)

def emp():
    main.withdraw()
    os.system("python employee.py")
    main.deiconify()


def adm():
    main.withdraw()
    os.system("python admin.py")
    main.deiconify()


img=Image.open("images/GN.png")
img=img.resize((1366,768),Image.Resampling.LANCZOS)
main.photoimg=ImageTk.PhotoImage(img)
lb_img=Label(main,image=main.photoimg,)
lb_img.place(anchor='center',x=683,y=300,width=1366,height=768)


button1 = Button(main)
button1.place(relx=0.316, rely=0.746, width=146, height=90)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(activebackground="#ffffff")
button1.configure(cursor="hand2")
button1.configure(foreground="#ffffff")
button1.configure(background="#ffffff")
button1.configure(borderwidth="0")
img2 = PhotoImage(file="./images/1.png")
button1.configure(image=img2)
button1.configure(command=emp)

button2 = Button(main)
button2.place(relx=0.566, rely=0.746, width=146, height=90)
button2.configure(relief="flat")
button2.configure(overrelief="flat")
button2.configure(activebackground="#ffffff")
button2.configure(cursor="hand2")
button2.configure(foreground="#ffffff")
button2.configure(background="#ffffff")
button2.configure(borderwidth="0")
img3 = PhotoImage(file="./images/2.png")
button2.configure(image=img3)
button2.configure(command=adm)

main.mainloop()
