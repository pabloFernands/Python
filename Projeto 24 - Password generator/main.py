from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_box.insert(0, string=password)
    #print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save(*args):
    with open("save.txt", "a") as data_file:
        website_input = website_box.get()
        email_input = email_box.get()
        password_input = password_box.get()

        if website_input == "" or len(email_input) == 0 or len(password_input) == 0:
            messagebox.showerror(title="Ops", message="You forgot something!")

        else:
            is_ok = messagebox.askokcancel(title=website_input,
                                           message=f"The email: {email_input}\nPassword: {password_input}\n"
                                                   f"Are correct?")
            if is_ok:
                data_file.write(f"{website_input} | {email_input} | {password_input} \n")

                website_box.delete(0, END)
                email_box.delete(0, END)
                password_box.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=5, pady=20)
photo_background = PhotoImage(file="logo.png")

canvas = Canvas(width=180, height=180, highlightthickness=0)
canvas.create_image(90, 90, image=photo_background)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=("Arial", 10, "bold"))
website_label.grid(column=0, row=1)

website_box = Entry(width=35)
website_box.grid(column=1, row=1, columnspan=2)
website_box.focus()

email_label = Label(text="Email/Username:", font=("Arial", 10, "bold"))
email_label.grid(column=0, row=2)

email_box = Entry(width=35)
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
