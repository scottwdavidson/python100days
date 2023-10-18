from tkinter import *
from tkinter import messagebox

import secrets
import string
import pyperclip

DEFAULT_EMAIL_USERNAME = "scott@scott-davidson.com"
SEPARATOR = ":"
CRLF = "\n"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_random_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(8))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    # copy the password to the clipboard for convenience
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def reset_entries():
    website_entry.delete(0, END)
    email_username_entry.delete(0, END)
    email_username_entry.insert(0, DEFAULT_EMAIL_USERNAME)
    password_entry.delete(0, END)


def save_entry():
    # extract the data
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    # error checks
    if website.isspace() or website == "":
        messagebox.showinfo(title="Oops", message='website is blank')
        return
    if password.isspace() or password == "":
        messagebox.showinfo(title="Oops", message='password is blank')
        return
    if len(password) < 8:
        messagebox.showinfo(title="Oops", message='password is too short')
        return

    # confirm w/ user
    if messagebox.askokcancel(title=website,
                              message=f"Email: {email_username}{CRLF}"
                                      f"Password: {password}{CRLF}"
                                      f"Is it okay to save?"):
        # write it
        with open("passwords.txt", "a") as passwords_file:
            line_entry = f"{website}{SEPARATOR}{email_username}{SEPARATOR}{password}{CRLF}"
            passwords_file.write(line_entry)
            reset_entries()


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Password Manager")
root.config(padx=50, pady=50, bg='white')
canvas = Canvas(root, width=200, height=200, background='white', highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
logo = canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Website label
website_label = Label(text="Website:", bg='white')
website_label.grid(row=1, column=0)

# Website entry
website_entry = Entry(width=35, bg='white', highlightthickness=0)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

# Email/Username label
email_username_label = Label(text="Email/Username:", bg='white')
email_username_label.grid(row=2, column=0)

# Email/Username entry
email_username_entry = Entry(width=35, bg='white', highlightthickness=0)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "scott@scott-davidson.com")

# Password label
password_label = Label(text="Password:", bg='white')
password_label.grid(row=3, column=0)

# Password entry
password_entry = Entry(width=21, bg='white', highlightthickness=0)
password_entry.grid(row=3, column=1)

# Generate Password button
generate_password_button = Button(text="Generate Password", bg='white', highlightthickness=0,
                                  command=generate_random_password)
generate_password_button.grid(row=3, column=2)

# Add button
add_button = Button(text="Add", bg='white', width=36, highlightthickness=0, command=save_entry)
add_button.grid(row=4, column=1, columnspan=2)

root.mainloop()
