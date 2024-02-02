from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('lessonThirteen (Checkboxes)')
root.iconbitmap('tkinter/default tkinter/img/favicon.ico')
root.geometry("500x500")

def show():
    myLabel = Label(root, text=clicked.get()).pack()
    
options = [
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday"
]

clicked = StringVar()
clicked.set(options[0])

#Craete dropdown menu
drop = OptionMenu(root, clicked, *options)
drop.pack()

myBtn = Button(root, text="Show selection", command=show).pack()

root.mainloop()