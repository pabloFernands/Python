from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- SEARCH ------------------------------- #
def search(*args):
    website_input = website_box.get()
    try:
        with open("save.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="File error!", message="Data not found.")

    else:
        if website_input in data:
            email = data[website_input]["email"]
            password = data[website_input]["password"]
            messagebox.showinfo(title=website_input, message=f"Email: {email}\nPassword: {password}")
            #print(data)
        else:
            messagebox.showinfo(title="Website data error!", message="Website not found.")



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def password_generator(*args):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_box.insert(0, string=password)
    pyperclip.copy(password)
    #print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save(*args):

        website_input = website_box.get()
        email_input = email_box.get()
        password_input = password_box.get()
        new_data = {
            website_input: {
                "email": email_input,
                "password": password_input
            }
        }

        if website_input == "" or len(email_input) == 0 or len(password_input) == 0:
            messagebox.showerror(title="Ops", message="You forgot something!")

        else:
            try:
                with open("save.json", "r") as data_file:
                    data = json.load(data_file)

            except (FileNotFoundError, json.decoder.JSONDecodeError):
                with open("save.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                data.update(new_data)
                with open("save.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                website_box.delete(0, END)
                email_box.delete(0, END)
                password_box.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=5, pady=20)
photo_background = PhotoImage(file="logo.png")

canvas = Canvas(width=150, height=170, highlightthickness=0)
canvas.create_image(90, 90, image=photo_background)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=("Arial", 10, "bold"))
website_label.grid(column=0, row=1)

website_box = Entry(width=22)
website_box.grid(column=1, row=1)
website_box.focus()

button_search = Button(text="Search", width=15, command=search)
button_search.grid(column=2, row=1)

email_label = Label(text="Email/Username:", font=("Arial", 10, "bold"))
email_label.grid(column=0, row=2)

email_box = Entry(width=41)
email_box.grid(column=1, row=2, columnspan=2)
email_box.insert(0, "pablo@google.com")

password_label = Label(text="Password:", font=("Arial", 10, "bold"))
password_label.grid(column=0, row=3)

password_box = Entry(width=22)
password_box.grid(column=1, row=3)
password_box.get()

button_generate = Button(text="Generate Password", command=password_generator)
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
