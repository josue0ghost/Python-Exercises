from tkinter import *

window = Tk()
window.title("Frames")
window.geometry("700x400")

frame = Frame(window, width=250, height=250)
frame.config(
    bg="red",
    bd=12,
    relief=RAISED #flat, raised, etc
)
frame.pack()
frame.pack_propagate(False)

Label(frame, text="text in frame").pack()

window.mainloop()