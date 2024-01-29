import tkinter as tk
from tkinter import ttk, font

# Window
window = tk.Tk()
window.title('Styling')
window.geometry('400x300')

# print(font.families())

# style
style = ttk.Style()
# print(style.theme_names())
# style.theme_use('vista')

# style for all of the specific type of widget
# style.configure('TButton', foreground = 'green', font = ('SimSun', 20))

# style for specific widgets with style = 'new.TButton'.
style.configure('new.TButton', foreground = 'green', font = ('SimSun', 20))
style.map('new.TButton', 
          foreground = [('pressed','red'),('disabled', 'yellow')],
          background = [('pressed', 'green'),('active', 'blue')])

style.configure('new.TFrame', background= 'pink')

# Widgets
label = ttk.Label(
    window, 
    text='A label\nAnd then type on another line', 
    background = 'red', 
    foreground= 'white',
    font=('SimSun', 20),
    justify = 'center')
label.pack()

button = ttk.Button(window, text='A button', style = 'new.TButton')
button.pack()

#Exercise:
#add a frame with a width and height and give it a pink background color.

frame = ttk.Frame(window, width = 100, height = 100, style = 'new.TFrame')
frame.pack()

# Run
window.mainloop()