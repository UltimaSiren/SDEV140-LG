from tkinter import *


# defining function to open appointment form in new window
def app_find():
    find_window = Toplevel()
    find_window.title("Search for a Scheduled Appointment")
    find_window.configure(background="#EBE094")
    find_window.geometry("835x800")

    # Customer Name field
    customer_name_label = Label(find_window, text="Enter Your First and Last Name: ", bg="#EBE094")
    customer_name_entry = Entry(find_window, width=50)
    customer_name_label.grid(row=1, column=1, sticky='E', pady=(10, 0))
    customer_name_entry.grid(row=1, column=2, sticky='NSEW', pady=(10, 0))

    # Customer Phone Number
    phone_entry_label = Label(find_window, text="Enter Your Phone Number: ", bg="#EBE094")
    phone_entry_label.grid(row=2, column=1, sticky='E', pady=(10, 0))
    phone_entry = Entry(find_window, width=25)
    phone_entry.grid(row=2, column=2, columnspan=4, sticky='NSEW', pady=(10, 0))

    # Customer Email Address
    email_entry_label = Label(find_window, text="Enter Your Email Address: ", bg="#EBE094")
    email_entry_label.grid(row=3, column=1, sticky='E', pady=(10, 0))
    email_entry = Entry(find_window, width=25)
    email_entry.grid(row=3, column=2, columnspan=4, sticky='NSEW', pady=(10, 0))

    new_submit = Button(find_window, text="Search", width=10)
    new_submit.grid(row=5, column=2, sticky='W', pady=(10, 0))
