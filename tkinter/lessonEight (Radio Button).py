from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("lessonEight (Radio Button)")
root.iconbitmap('tkinter/img/favicon.ico')

#r = IntVar()
#r.set("2")

#Create list and tuples inside.
TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

#Use tkinter String Variable.
pizza = StringVar()
pizza.set("Pepperoni")

#Loop through the list and display all radiobuttons.
for text, topping in TOPPINGS: 
    Radiobutton(root, text=text, variable=pizza, value=topping, ).pack(anchor=W)
    
#Function to display the clicked variable.
def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


#Radiobutton(root,text="Option 1", variable=r, value=1, command= lambda: clicked(r.get())).pack()
#Radiobutton(root,text="Option 2", variable=r, value=2, command= lambda: clicked(r.get())).pack()

#myLabel = Label(root, text=pizza.get())
#myLabel.pack()

myButton = Button(root, text="Click me!", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()