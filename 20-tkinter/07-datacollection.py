from tkinter import *
window = Tk()
window.geometry("700x700")

def getData():
    result.set(data.get())

    if len(result.get()) >= 1:
        gettedText.config(
            bg="green",
            fg="white"
        )

data = StringVar()
result = StringVar()

Label(window, text="Insert a text").pack()
Entry(window, textvariable=data).pack()

Label(window, text="Collected data: ").pack()
gettedText = Label(window, textvariable=result)
gettedText.pack()

Button(window, text="Show data", command=getData).pack()

window.mainloop()