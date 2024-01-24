from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('lessonTwelve (Sliders)')
root.iconbitmap('tkinter/img/favicon.ico')
root.geometry("900x500")

vertical = Scale(root, from_=0, to=200)
vertical.pack()

def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))
    
    
horizontal = Scale(root, from_=0, to=500, orient=HORIZONTAL)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()

my_btn = Button(root, text="click me", command=slide).pack()

root.mainloop()