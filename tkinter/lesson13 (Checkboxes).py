from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('lessonThirteen (Checkboxes)')
root.iconbitmap('tkinter/img/favicon.ico')
root.geometry("500x500")

def show():
    myLabel = Label(root, text=var.get()).pack()    

var = StringVar()

c = Checkbutton(root, text="Check this box!", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()


myBtn = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
