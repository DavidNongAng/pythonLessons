from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('using databases.')
root.iconbitmap('tkinter/default tkinter/img/favicon.ico')
root.geometry("500x500")

#Databases

#Create or connect to a database.

conn = sqlite3.connect('address_book.db')

#Create cursor
c = conn.cursor()

#Create table
c.execute("""
          CREATE TABLE addresses (
              first_name text,
              last_name text,
              address text,
              city text,
              state text,
              zipcode integer
          )""")


#Commit Changes
conn.commit()

#Close Connection
conn.close()


root.mainloop()