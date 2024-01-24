from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("lessonTen (Create New Windows)")
root.iconbitmap('tkinter/img/favicon.ico')

#Function to open second window.
def open():
    global my_img
    #Second window 
    top = Toplevel()
    top.title("Second Window")
    top.iconbitmap('tkinter/img/favicon.ico')
    my_img = ImageTk.PhotoImage(Image.open("tkinter/img/cat1.jpg"))
    my_label = Label(top, image=my_img).pack()  
    btn2 = Button(top, text="close window", command=top.destroy).pack()

btn = Button(root, text="Open Second Window", command=open).pack()


mainloop()
