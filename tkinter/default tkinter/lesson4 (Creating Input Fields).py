from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth = 5,bg='#262626', fg='white')
e.pack()
e.insert(0, "Enter Your Name: ")

#e.get() gets what the user puts in the textbox

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text= hello)
    myLabel.pack()

#Creating a Button
myButton = Button(root, text= "Enter Your Name", padx=50, pady= 50, command=myClick, fg= 'red', bg= '#262626')
myButton.pack()

root.mainloop()