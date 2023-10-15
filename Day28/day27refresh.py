import tkinter as tk

window = tk.Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)

# label : create component and then define layout
a_label = tk.Label(text="A Label", font=("Arial", 24, "bold"))
a_label.pack(side="left")
a_label["text"] = "New Text"
a_label.config(text="Newer Text")

button = tk.Button(text="BUTTON")
button.pack()


# keeps the window open - put at the end
# window.update()
window.mainloop()