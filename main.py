from playsound import playsound
from tkinter import *
from PIL import ImageTk, Image
import keyboard

root = Tk()
img = ImageTk.PhotoImage(Image.open("indeks2.jpg"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")


while 1:
    playsound('./mantis.mp3')
    root.mainloop()
if keyboard.is_pressed('a'):
    exit()




