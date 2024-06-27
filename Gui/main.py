from tkinter import *


def button_clicked():
    number = float(name_var.get())
    number *= 1.609
    my_label2.config(text=f"{number}")


# window
window = Tk()
window.title("Hello")
window.minsize(width=100, height=100)
window.config(padx=30, pady=30)


# entry
name_var = IntVar()
name_entry = Entry(width=5, textvariable=name_var, font=('calibre', 10, 'normal'))
name_entry.insert(END, string="")
name_entry.grid(column=1, row=0)

# label
my_label = Label(text="Miles")
my_label.grid(column=2, row=0)

my_label1 = Label(text="is equal to")
my_label1.grid(column=0, row=1)

my_label2 = Label(text="0")
my_label2.grid(column=1, row=1)


my_label3 = Label(text="Km")
my_label3.grid(column=2, row=1)

# button
fred = Button(text='Calculate', command=button_clicked)
fred.grid(column=1, row=2)


window.mainloop()
