from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("lessonSix (Adding A Status Bar)")
root.iconbitmap('tkinter/img/favicon.ico')

#Initialize Image Objects
my_img1 =  ImageTk.PhotoImage(Image.open("tkinter/img/cat1.jpg"))
my_img2 =  ImageTk.PhotoImage(Image.open("tkinter/img/cat2.PNG"))
my_img3 =  ImageTk.PhotoImage(Image.open("tkinter/img/cat3.jpg"))
my_img4 =  ImageTk.PhotoImage(Image.open("tkinter/img/cat4.png"))
my_img5 =  ImageTk.PhotoImage(Image.open("tkinter/img/cat5.png"))

#Store Images in a List
image_list = [my_img1,my_img2,my_img3,my_img4,my_img5]

#Create Label for the status bar at the bottom of the program.
status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)


my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

#Function to scroll forward through the images.
def forward(image_num):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget() #Delete the previous image on screen
    my_label = Label(image=image_list[image_num-1]) #Create new Label for the next image.
    button_forward = Button(root, text=">>", command = lambda: forward(image_num+1)) #Create button to scroll to the next image.
    button_back = Button(root, text="<<", command=lambda: back(image_num-1)) #Create button to scroll to the previous image.
    
    #Disable the forward button when it reaches the end.
    if image_num == 5:
        button_forward = Button(root,text=">>", state=DISABLED)
    
    #Display the image and buttons on the screen.
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    
    #Create status Labels to display what number of image you are on.
    status = Label(root, text="Image "+ str(image_num) +" of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E) #convert the number to a string after calling it.
    status.grid(row=2, column=0, columnspan=3, sticky=W+E) #Display the status bar at the botton.
    
#Function to scroll backwards through the images
def back(image_num):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget() #Delete the previous image on screen
    my_label = Label(image=image_list[image_num-1]) #Create new Label for the next image.
    button_forward = Button(root, text=">>", command = lambda: forward(image_num+1)) #Create button to scroll to the next image.
    button_back = Button(root, text="<<", command=lambda: back(image_num-1)) #Create button to scroll to the previous image.
    
    #Disable the forward button when it reaches the beginning.
    if image_num == 1:
        button_back = Button(root,text="<<", state=DISABLED)
    
    #Display the image and buttons on the screen.
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    
    #Create status Labels to display what number of image you are on.
    status = Label(root, text="Image "+ str(image_num) +" of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E) #convert the number to a string after calling it.
    status.grid(row=2, column=0, columnspan=3, sticky=W+E) #Display the status bar at the botton.

#Create buttons.
button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

#Display buttons
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()