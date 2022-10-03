"""
Realaxx Real Estate Appointment App
Lorelei Gatten
This program is intended to allow users to schedule, search, and re-schedule previously set appointments
with a local real estate company."""

# Import necessary libraries and functions
from tkinter import *
from appointmentCreator import app_set
from appointmentSearch import app_find

# Creating main window and setting selections
main_window = Tk()
main_window.title("Realaxx Real Estate Appointment Scheduler")
main_window.configure(bg="#EBE094")
main_window.geometry("835x800")

# Banner with Company Name
real_Logo = PhotoImage(file="RealaxxLogo.png")
logo_label = Label(image=real_Logo)
logo_label.grid(row=1, column=3)


# Label to direct user to choose which action to take
question_title = Label(main_window, text="What Would You Like to Do?", background="#EBE094", borderwidth=25, font=40)
question_title.grid(row=2, column=3)

# Button to schedule new appointment
new_appointment_button = Button(background="#412A42", foreground="white", text="Schedule New Appointment",
                                command=app_set)
new_appointment_button.grid(row=3, column=2)

# Button to search scheduled appointments
search_appointment_button = Button(bg="#412A42", fg="white", text="Search For Scheduled Appointments",
                                   command=app_find)
search_appointment_button.grid(row=3, column=4)


main_window.mainloop()
