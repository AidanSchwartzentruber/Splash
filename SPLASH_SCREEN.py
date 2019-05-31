'''
Created on May 30, 2019

@author: Aidan S., Francesca B.
'''
import time 
import os

from tkinter import *
root = Tk()
root.geometry("1000x750")
root.title("Splash")

splash = PhotoImage(file = "splash_pic.PNG")
splash = splash.subsample(2,2)
test = Label(root, image = splash)
test.pack()

root.after(3000, root.destroy)

root.mainloop()