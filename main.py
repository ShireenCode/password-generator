from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    input_password.insert(0, password)

    print(f"Your password is: {password}")


# ---------------------------- RECALL WEBSITES ------------------------------- #
def retrieve_website():
    website = input_website.get()
    try:
        with open("saved_passwords.json", "r") as saved:
            data = json.load(saved)
    except FileNotFoundError:
        messagebox.showinfo(title=f"No Passwords", message=f"Sorry! No passwords saved yet.")
    else:
        if website in data:
            website_email = data[website]["email"]
            website_password = data[website]["password"]
            messagebox.showinfo(title=f"{website} Password", message=f"Email: {website_email} "
                                                                     f"\n Password: {website_password}")
        else:
            messagebox.showinfo(title=f"No Password", message=f"Sorry! No password saved for this site.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
    }
        }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please fill in all boxes!")
    else:
        try:
            with open("saved_passwords.json", "r") as saved:
                data = json.load(saved)
                data.update(new_data)
        except FileNotFoundError:
            with open("saved_passwords.json", "w") as saved:
                json.dump(new_data, saved, indent=4)
        else:
            data.update(new_data)

            with open("saved_passwords.json", "w") as saved:
                json.dump(data, saved, indent=4)
        finally:
            input_website.delete(0, END)
            input_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

#BACKGROUND
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

#LABELS
label_website = Label(text="Website:", font=("Arial", 12))
label_website.grid(row=1, column=0)
label_email = Label(text="Email/Username:", font=("Arial", 12))
label_email.grid(row=2, column=0)
label_password = Label(text="Password:", font=("Arial", 12))
label_password.grid(row=3, column=0)

#INPUTS
input_website = Entry(width=21)
input_website.grid(row=1, column=1)
input_website.focus()
input_email = Entry(width=35)
input_email.insert(0, "test@testthispassman.com")
input_email.grid(row=2, column=1, columnspan=2)
input_password = Entry(width=21)
input_password.grid(row=3, column=1)

#BUTTONS
button_generate = Button(text="Generate Password", font=("Arial", 12), command=generate_password)
button_generate.grid(row=3, column=2)
button_add = Button(text="Add", font=("Arial", 12), width=36, command=save)
button_add.grid(row=4, column=1, columnspan=2)
button_search = Button(text="Search", font=("Arial", 12), command=retrieve_website)
button_search.grid(row=1, column=2)


window.mainloop()
