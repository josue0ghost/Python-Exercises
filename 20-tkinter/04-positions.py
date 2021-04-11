from tkinter import *

window = Tk()

text = Label(window, text="Hello there!")
text.config(
    fg = "white",
    bg = "black",
    padx = 100,
    pady = 20,
    font = ("Sans-Serif", 50),
    justify=RIGHT
)
text.pack(side=TOP)

text = Label(window, text="General Kenobi!")
text.config(
    height=5,
    padx = 100,
    pady = 20,
    bg="cyan",
    cursor="spider"
)
text.pack(side=TOP, fill=X, expand=YES)

text = Label(window, text="General Kenobi!")
text.config(
    height=5,
    padx = 100,
    pady = 20,
    bg="red",
    cursor="spider"
)
text.pack(side=LEFT) # N NE E SE S SW W NW

window.mainloop()