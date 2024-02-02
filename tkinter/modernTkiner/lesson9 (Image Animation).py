'''
- If you can import images and animate widgets you have the basics

- The actual difficult problems:
1 Import a large amount of images
2 Implement state management
3 Prevent interruptions

'''

import customtkinter as ctk
from PIL import Image
from os import walk

class AnimatedButton(ctk.CTkButton):
    def __init__(self, parent, light_path, dark_path):
        self.import_folders(light_path, dark_path)
        
        super().__init__(master = parent, text = 'A animated button')
        self.pack(expand = True)
        
    def import_folders(self, light_path, dark_path):
        for path in (light_path, dark_path):
            print(list(walk(path)))

# window
window = ctk.CTk()
window.title('Animations')
window.geometry('300x200')

AnimatedButton(window, 'black', 'yellow')

# run 
window.mainloop()