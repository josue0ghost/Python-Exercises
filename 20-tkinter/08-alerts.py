from tkinter import *
from tkinter import messagebox as MsgBox

window = Tk()
window.config(bd=70)

def alert():
    MsgBox.showinfo("Alert", "Showing message")
    MsgBox.showwarning("Alert", "Showing message")
    MsgBox.showerror("Alert", "Showing message")

def exit():
    result = MsgBox.askquestion("Exit", "Continue using app?")
    if result == "no":
        window.destroy()

Button(window, text="Show alert", command=alert).pack()
Button(window, text="Exit", command=exit).pack()

window.mainloop()