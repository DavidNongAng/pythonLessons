from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("ICONS AND IMAGES")
root.iconbitmap('tkinter/favicon.ico')








button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()




root.mainloop()