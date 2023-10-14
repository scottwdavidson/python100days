from tkinter import *


window = Tk()
window.title("My First Tkinter GUI")
window.minsize(width=500, height=300)

label = Label(text="I am a label", font=("Arial", 24, "italic"))
label["text"] = "New Text"
label.pack()

def button_clicked():
    print("... button was clicked ...  ")
    label.config(text=input.get())
button = Button(text="Click Me", command=button_clicked)
button.pack()
# entry_input
# input = Entry(textvariable=entry_input)
input = Entry()
input.pack()
print(input.get())

window.mainloop()