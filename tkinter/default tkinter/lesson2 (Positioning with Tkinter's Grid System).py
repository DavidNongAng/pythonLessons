from tkinter import *

root = Tk()

#Creating a Label Widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is David Nong-Ang")
myLabel3 = Label(root, text="                           ")

#Grid System 
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 1)
myLabel3.grid(row = 1, column = 2)

#Or it could be done as...

myLabel4 = Label(root, text="HELLO").grid(row = 4, column = 1)
myLabel5 = Label(root, text="WORLD").grid(row = 4, column = 2)
myLabel6 = Label(root, text="NEW").grid(row = 4, column = 3)

root.mainloop()