import tkinter as tk

root = tk.Tk()
root.title("Mile to Km Converter")

# entry for miles
miles_entry = tk.Entry(width=8)
miles_entry.grid(row=0, column=1)

# miles label
miles_label = tk.Label(text="Miles")
miles_label.grid(row=0, column=2)
miles_label.config(padx=5, pady=5)

# is equal to label
is_equal_to_label = tk.Label(text="is equal to ")
is_equal_to_label.grid(row=1, column=0)
is_equal_to_label.config(padx=5, pady=5)

# km value label
km_value_label = tk.Label(text=" --- ")
km_value_label.grid(row=1, column=1)
km_value_label.config(padx=5, pady=5)

# km value label
km_label = tk.Label(text=" Km ")
km_label.grid(row=1, column=2)
km_label.config(padx=5, pady=5)


def button_clicked():
    miles = float(miles_entry.get())
    miles_to_km_multiplier = 1.61
    kms = miles * miles_to_km_multiplier
    print(f"... button clicked ... {miles} --> {kms}")
    km_value_label.config(text=kms)


# calculate button
calculate_button = tk.Button(text="Calculate", command=button_clicked)
calculate_button.grid(row=2, column=1)
calculate_button.config(padx=5, pady=5)

# # main (root) window
# root.title("My First GUI")
# root.minsize(width=500, height=300)
# root.config(padx=55, pady=55)
#
# # label
# ex_label = tk.Label(text="I a label", font=("Arial", 24, "bold"))
# # ex_label.place(x=0,y=0)
# ex_label.grid(row=0,column=0)
# ex_label.config(padx=5, pady=5)
#
# # button
# ex_button = tk.Button(text="Click Me", command=button_clicked)
# ex_button.grid(row=0,column=2)
# ex_button.config(padx=5, pady=5)
#
# ex_button2 = tk.Button(text="Click Me too", command=button_clicked)
# ex_button2.grid(row=1,column=1)
# ex_button2.config(padx=5, pady=5)

root.mainloop()
