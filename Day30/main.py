from tkinter import *
from tkinter import messagebox

import secrets
import string
import pyperclip
import json
import logging

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
    # extract the data and create a dict element for storage
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    entry = {website: {"email": email_username, "password": password}}
    passwords = {}

    # error checks
    if website.isspace() or website == "":
        messagebox.showinfo(title="Oops", message='website is blank')
    elif password.isspace() or password == "":
        messagebox.showinfo(title="Oops", message='password is blank')
    elif len(password) < 8:
        messagebox.showinfo(title="Oops", message='password is too short')
    else:
        try:
            # read existing data
            with open("passwords.json", "r") as passwords_file:
                passwords = json.load(passwords_file)
                passwords.update(entry)

        except FileNotFoundError:
            passwords = entry

        try:
            with open("passwords.json", "w") as passwords_file:
                print(type(passwords))
                print(passwords)
                json.dump(passwords, passwords_file, indent=4)
                reset_entries()
        except:
            logging.exception("not expecting anything here")


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    # get passwords
    try:
        # read existing data
        with open("passwords.json", "r") as passwords_file:
            passwords = json.load(passwords_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message='there are no passwords stored yet')
    else:
        # search for the website
        website = website_entry.get()
        if website in passwords:
            message = (f"email: {passwords[website]['email']}{CRLF}"
                       f"password: {passwords[website]['password']}")
            messagebox.showinfo(title="Success", message=message)
        else:
            message = f"website: {website} not found"
            messagebox.showinfo(title="Failure", message=message)


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Password Manager")
root.config(padx=50, pady=50)
canvas = Canvas(root, width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
logo = canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Website label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

# Website entry
website_entry = Entry(width=21, highlightthickness=0)
website_entry.grid(row=1, column=1)
website_entry.focus()

# Search button
search_button = Button(text="Search", highlightthickness=0,
                       width=14,
                       command=search_password)
search_button.grid(row=1, column=2)

# Email/Username label
email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

# Email/Username entry
email_username_entry = Entry(width=35, highlightthickness=0)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "scott@scott-davidson.com")

# Password label
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Password entry
password_entry = Entry(width=21, highlightthickness=0)
password_entry.grid(row=3, column=1)

# Generate Password button
generate_password_button = Button(text="Generate Password", width=14,
                                  command=generate_random_password)
generate_password_button.grid(row=3, column=2)

# Add button
add_button = Button(text="Add", width=36, highlightthickness=0, command=save_entry)
add_button.grid(row=4, column=1, columnspan=2)

root.mainloop()
