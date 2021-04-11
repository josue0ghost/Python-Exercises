from tkinter import *

window = Tk()
window.geometry("500x500")

text = Label(window, text="Hello there!")
text.config(
    fg = "white",
    bg = "black",
    padx = 100,
    pady = 20,
    font = ("Sans-Serif", 50),
    justify=RIGHT
)
text.pack()

text = Label(window, text="General Kenobi!")
text.config(
    height=5,
    padx = 100,
    pady = 20,
    bg="cyan",
    cursor="spider"
)
text.pack(anchor=NW) # N NE E SE S SW W NW

text = Label(window, text="General Kenobi!")
text.config(
    height=5,
    padx = 100,
    pady = 20,
    bg="cyan",
    cursor="spider"
)
text.pack(anchor=NE) # N NE E SE S SW W NW

window.mainloop()