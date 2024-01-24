from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title('lessonEleven (Open Files Dialog Box)')
root.iconbitmap('tkinter/img/favicon.ico')

#root.filename = filedialog.askopenfilename(initialdir='tkinter/img', title="Select a File", filetypes=(("PNG Files", "*.png"),("All Files","*.*"),("JPG Files","*.jpg")))
#myLabel = Label(root, text=root.filename).pack()
#my_img = ImageTk.PhotoImage(Image.open(root.filename))
#my_img_label = Label(image=my_img).pack()

def open():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir='tkinter/img', title="Select a File", filetypes=(("PNG Files", "*.png"),("All Files","*.*"),("JPG Files","*.jpg")))
    myLabel = Label(root, text=root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_img_label = Label(image=my_img).pack()

my_btn = Button(root, text="Open File", command=open).pack()

root.mainloop()