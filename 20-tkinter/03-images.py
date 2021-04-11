# Pls Do: pip install --upgrade Pillow

from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.geometry("500x500")

Label(window, text="Hello there").pack(anchor=W)

image = Image.open('./images/Act01.png')
render = ImageTk.PhotoImage(image)

Label(window, image=render).pack(anchor=N)

window.mainloop()