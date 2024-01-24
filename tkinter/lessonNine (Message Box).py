from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("lessonNine (Message Box)")
root.iconbitmap('tkinter/img/favicon.ico')

#showinfo, showwarning, showerrror, askquestion, askokcancel, askyesno

def popup():
    #response = messagebox.showinfo("This is my Popup!", "Hello World!")
    #response = messagebox.showwarning("This is my Popup!", "Hello World!")
    #response = messagebox.askquestion("This is my Popup!", "Hello World!")
    #response = messagebox.askokcancel("This is my Popup!", "Hello World!")
    response =messagebox.askyesno("This is my Popup!", "Hello World!")
    
    #Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You Clicked Yes!").pack()
    else:
        Label(root, text="You Clicked No!").pack()
    

Button(root, text="Popup", command=popup).pack()


mainloop()