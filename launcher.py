import os
import tkinter

from tkinter import *

print
root = Tk()
root.title("Launcher")
root.minsize(200, 200)  # width, height
root.geometry("300x300+50+50")
image = PhotoImage(file="banner.png")
img = Label(root, image=image)
img.pack()
def play():
    root.destroy()
    os.system('python main.py')
    exit()
def edit():
    root.destroy()
    os.system('python editor.py')
    exit()
B = Button(root, text ="Play", command = play)
B.place(x=130,y=200)
B = Button(root, text ="Editor", command = edit)
B.place(x=125,y=240)
root.mainloop()