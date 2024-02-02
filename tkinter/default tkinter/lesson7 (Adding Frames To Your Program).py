from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("lessonSeven (Adding Frames To Your Program)")
root.iconbitmap('tkinter/default tkinter/img/favicon.ico')

#Craete Frame Object
frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10, pady=10)

#Put the Button inside the Frame
b = Button(frame, text="Don't Click Here!")
b2 = Button(frame, text="...or here!")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)


root.mainloop()