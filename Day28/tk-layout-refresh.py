import tkinter as tk

root = tk.Tk()

def button_clicked():
    print("... button clicked ... ")

# main (root) window
root.title("My First GUI")
root.minsize(width=500, height=300)
root.config(padx=55, pady=55)

# label
ex_label = tk.Label(text="I a label", font=("Arial", 24, "bold"))
# ex_label.place(x=0,y=0)
ex_label.grid(row=0,column=0)
ex_label.config(padx=15, pady=15)

# button
ex_button = tk.Button(text="Click Me", command=button_clicked)
ex_button.grid(row=0,column=2)
ex_button.config(padx=15, pady=15)

ex_button2 = tk.Button(text="Click Me too", command=button_clicked)
ex_button2.grid(row=1,column=1)
ex_button2.config(padx=15, pady=15)

# entry
ex_input = tk.Entry(width=10)
print(ex_input.get())
ex_input.grid(row=2,column=3)
# ex_input.config(padx=15, pady=15) --> padding not available
root.mainloop()