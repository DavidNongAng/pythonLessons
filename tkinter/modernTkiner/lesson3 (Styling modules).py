import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

# window
window = ctk.CTk()
window.title('customtkinter app')
window.geometry('600x400')

# widgets
string_var = ctk.StringVar(value = 'a custom string')
label = ctk.CTkLabel(
    window, 
    text = 'A ctk Label', 
    fg_color = ('blue','#262626'),
    text_color= ('black','white'),
    corner_radius= 10,
    textvariable = string_var)
label.pack()

button = ctk.CTkButton(
    window, 
    text = 'A ctk Button',
    fg_color = '#262626',
    text_color = 'white',
    corner_radius = 10,
    hover_color = '#8C8C73',
    command = lambda: ctk.set_appearance_mode('dark'))
button.pack()

frame = ctk.CTkFrame(window, fg_color = 'red')
frame.pack()

slider = ctk.CTkSlider(frame)
slider.pack(padx = 20, pady = 20)

switch = ctk.CTkSwitch(
    window, 
    text = 'Exercise Switch',
    fg_color = ('blue','red'),
    progress_color = 'pink',
    button_color = 'green',
    button_hover_color = 'yellow',
    switch_width = 60,
    switch_height = 30,
    corner_radius = 5
)
switch.pack()

# run
window.mainloop()