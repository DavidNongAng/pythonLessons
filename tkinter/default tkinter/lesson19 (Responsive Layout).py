'''
- Tkinter lacks inbuilt tools for responsive layouts
- We cannot update an exisitng layout
- We need to create a separate layout for each window size.


- We are setting break points for the minimum width of a layout
- From a width of 300: small layout
- From a width of 600: medium layout
- From a width of 1200: large layout


- Whenever the window resizes, we check the width and if it crosses a threshold, we build a new layout
'''

import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, start_size):
        super().__init__()
        self.title('Responsive Layout')
        self.geometry(f'{start_size[0]}x{start_size[1]}')
        
        self.frame = ttk.Frame(self)
        self.frame.pack(expand = True, fill = 'both')   
        
        size_notifier = SizeNotifier(self, {300: self.create_small_layout, 600: self.create_medium_layout, 1200: self.create_large_layout})
        self.mainloop()
        
    def create_small_layout(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        
        ttk.Label(self.frame, text = 'Label 1', background = 'red').pack(expand = True, fill = 'both')
        ttk.Label(self.frame, text = 'Label 2', background = 'green').pack(expand = True, fill = 'both')
        ttk.Label(self.frame, text = 'Label 3', background = 'blue').pack(expand = True, fill = 'both')
        ttk.Label(self.frame, text = 'Label 4', background = 'yellow').pack(expand = True, fill = 'both')
        self.frame.pack(expan = True, fill = 'both')
        
    def create_medium_layout(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        
        

    def create_large_layout(self):
        pass

class SizeNotifier:
    def __init__(self, window, size_dict):
        pass
    
    def check(self, event):
        pass
    
app = App((400,300))
        
        
