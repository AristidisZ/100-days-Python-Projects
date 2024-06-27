from tkinter import *
from tkinter import messagebox

import pyperclip
import random
import string
import json

file_path = 'data.json'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_random_password(length=12):
    entry_pass.delete(0, END)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print(password)
    entry_pass.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_text():
    global file_path
    file_path = 'data.json'
    website = entry_web.get()
    email_username = entry_em.get()
    password = entry_pass.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please dont leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n{email_username}"
                                                              f"\n{password} \nIs it ok to save?")
        if is_ok:
            try:
                with open(file_path, "r") as data_file:
                    # read
                    data = json.load(data_file)
                    # update
                    data.update(new_data)
            except FileNotFoundError:
                with open(file_path, "w") as data_file:
                    # write
                    json.dump(new_data, data_file, indent=4)
                    # print(data)
                    # data_file.write(f"{website} | {email_username} | {password}\n")
            else:
                with open(file_path, "w") as data_file:
                    # write
                    json.dump(data, data_file, indent=4)
                    # print(data)
                    # data_file.write(f"{website} | {email_username} | {password}\n")
            finally:
                entry_web.delete(0, END)
                entry_pass.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

def search():
    website = entry_web.get()
    global file_path
    try:
        with open(file_path, "r") as data_file:
            # read
            data = json.load(data_file)
            print(data)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Info", message=f"Email/Username: {email} \n "
                                                      f"Password: {password}")
        else:
            messagebox.showinfo(title="Info", message=f"No such Data as {website}")


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
# timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("courier", 30, "bold"))
canvas.grid(column=1, row=0)

# Labels
label_web = Label(text="Website: ")
label_web.grid(column=0, row=1)

entry_web = Entry(width=35)
# Add some text to begin with
entry_web.insert(END, string="")
# Gets text in entry
print(entry_web.get())
entry_web.grid(column=1, row=1, columnspan=2)

# calls action() when pressed
button_search = Button(text="Search", command=search)
button_search.grid(column=2, row=1)

label_em = Label(text="Email/Username: ")
label_em.grid(column=0, row=2, pady=5)

entry_em = Entry(width=35)
# Add some text to begin with
entry_em.insert(END, string="aristidiszotka@gmail.com")
# Gets text in entry
# print(entry_em.get())
entry_em.grid(column=1, row=2, columnspan=2)

label_pass = Label(text="Password: ")
label_pass.grid(column=0, row=3)

entry_pass = Entry(width=25)
# Add some text to begin with
entry_pass.insert(END, string="")
# Gets text in entry
# print(entry_em.get())
entry_pass.grid(column=1, row=3, columnspan=1)

# calls action() when pressed
button_gene = Button(text="Generate Password", command=generate_random_password)
button_gene.grid(column=2, row=3)

# calls action() when pressed
button_add = Button(text="Add", command=add_text, width=20)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
