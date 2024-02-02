''' 
NOTES
- You can anmate widgets but there are no prebuilt components 
- To make your own, you need to use the after method and combine either with the layouts or the configure method of the widget
- Widgets can be updated in real time using either configure or the layout methods
- Calling a layout method multiple times on the same widget overrised the previous one
button.place(x = 10, y = 50)
button.place(x = 200, y = 0) # the previous one will be removed.
- That way you can update the position and the size of the widget
- configure can update the text, font, colors, etc...

IMPORTANT:
- When animating widgets with layouts, you want to use 'place'
- It is the only one that can change values pixel by pixel.


- 'After' is a method of Tk that can call a function after some time
window.after(1000, func)
- This can be circular. A function called with 'after' can call after itself

def funct():
    print('test')
    window.after(1000,func)
'''

import customtkinter as ctk
from random import choice

class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master = parent)
        
        # general attributes
        self.start_pos = start_pos + 0.04
        self.end_pos = end_pos - 0.03
        self.width = abs(start_pos - end_pos)
        
        # Animation Logic
        self.pos = self.start_pos
        self.in_start_pos = True # track if its in the start pos or not
        
        # Layout
        self.place(relx = self.start_pos, rely = 0.05, relwidth = self.width, relheight = 0.9)
        
    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backward()
    
    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.place(relx = self.pos, rely = 0.05, relwidth = self.width, relheight = 0.9)
            self.after(10, self.animate_forward)
        else:
            self.in_start_pos = False
            
    def animate_backward(self):
        if self.pos < self.start_pos:
            self.pos += 0.008
            self.place(relx = self.pos, rely = 0.05, relwidth = self.width, relheight = 0.9)
            self.after(10, self.animate_backward)
        else:
            self.in_start_pos = True
        
def move_btn():
    global button_x
    button_x += 0.001
    button.place(relx = button_x, rely = 0.5, anchor = 'center')
    
    if button_x < 0.9:
        window.after(10, move_btn)
    
    # configure
    # colors = ['red', 'yellow', 'pink', 'green', 'blue', 'black', 'white']
    # color = choice(colors)
    # button.configure(fg_color = color)
    
def infinite_print():
    global button_x
    button_x += 0.5
    if button_x < 10:
        print('Infinite')
        print(button_x)
        window.after(100, infinite_print)

# window 
window = ctk.CTk()
window.title('Animated Widgets')
window.geometry('600x400')
ctk.set_appearance_mode('light')

# Animated Widget
animated_panel = SlidePanel(window, 1.0, 0.7)
ctk.CTkLabel(animated_panel, text = 'Label 1').pack(expand = True, fill = 'both', padx = 2, pady = 10)
ctk.CTkLabel(animated_panel, text = 'Label 2').pack(expand = True, fill = 'both', padx = 2, pady = 10)
ctk.CTkButton(animated_panel, text = 'Button', corner_radius = 0).pack(expand = True, fill = 'both', pady = 10)
ctk.CTkTextbox(animated_panel, fg_color = ('#dbdbdb', '#2b2b2b')).pack(expand = True, fill = 'both', pady = 10)

# button 
button_x = 0.5
button = ctk.CTkButton(window, text = 'toggle_sidebar', command = animated_panel.animate)
button.place(relx = button_x, rely = 0.5, anchor = 'center')




# run 
window.mainloop()