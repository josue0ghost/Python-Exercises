from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Form")

header = Label(window, text="Forms for Tkinter")
header.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans", 18)
)
header.grid(row=0, column=0, sticky=W)

# text input
textInput = Entry(window)
textInput.grid(row=1, column=0, padx=5, pady=5)

# big text area
bigText = Text(window)
bigText.grid(row=2, column=0)
bigText.config(
  width=30,
  height=5,
  font=("Arial", 12),
  padx=10,
  pady=10
)

# buttons
button = Button(window, text="Send")
button.grid(row=3, column=0, sticky=E)

window.mainloop()

'''
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-111276284-9"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-111276284-9');
</script>
'''