from tkinter import *
import os.path

class Program:
    def __init__(self):
        self.title = "UI with Python"
        self.icon = "./images/favicon.ico"
        self.icon_alt = "./20-tkinter/images/favicon.ico"
        self.size = "400x400"
        self.resizable = FALSE
        self.window = Tk()

    def load(self):
        # window title
        self.window.title(self.icon)
        # size of window
        self.window.geometry(self.size)

        # resize window?
        if self.resizable:
            self.window.resizable(1, 1) # X, Y
        else:
            self.window.resizable(0, 0)

        # file exists?
        icon_path = os.path.abspath(self.icon)
        if not os.path.isfile(icon_path):
            icon_path = os.path.abspath(self.icon_alt)
        # favicon
        self.window.iconbitmap(icon_path)        

    def addText(self, txt):
        # show text
        text = Label(self.window, text=txt)
        text.pack()
    
    def show(self):
        # open window
        self.window.mainloop()

# Instance program
program = Program()
program.load()
program.addText("Hi")
program.show()