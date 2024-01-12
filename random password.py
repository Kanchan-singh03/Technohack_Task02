import secrets
import string
import tkinter as tk
from tkinter import Label, Button, Entry

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def generate_password_and_update_label():
    length = int(length_entry.get())
    password = generate_password(length)
    password_label.config(text="Generated Password: " + password)

# Create the main application window
app = tk.Tk()
app.title("Password Generator")

# Create and pack GUI components
length_label = Label(app, text="Password Length:")
length_label.pack()


length_entry = Entry(app)
length_entry.pack()

generate_button = Button(app, text="Generate Password", command=generate_password_and_update_label)
generate_button.pack()

password_label = Label(app, text="Generated Password:")
password_label.pack()

# Start the main event loop
app.mainloop()
