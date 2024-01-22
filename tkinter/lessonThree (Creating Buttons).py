from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="BOOM!")
    myLabel.pack()

#Creating a Button
myButton = Button(root, text= "Click Me!", padx=50, pady= 50, command=myClick, fg= 'red', bg= '#262626')
myButton.pack()


root.mainloop()
