from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

## Window setup ##
window = Tk()
window.title("MyPass")
window.config(padx=20, pady=20, bg="white")

## Image setup ##
mypass_image = PhotoImage(file= "day-29_password_manager/logo.png")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=mypass_image)
canvas.grid(column=1, row=0)

## Labels ##
label_website = Label(text="Website:", font=("calibri", 12, "bold"), bg="white")
label_website.grid(column=0, row=1)

label_email_username = Label(text="Email/Username:", font=("calibri", 12, "bold"), bg="white")
label_email_username.grid(column=0, row=2)

label_password = Label(text="Password:", font=("calibri", 12, "bold"), bg="white")
label_password.grid(column=0, row=3)

## Entries ##
entry_website = Entry(width=35, borderwidth=2)
entry_website.grid(column=1,row=1, columnspan=2)

entry_email_username = Entry(width=35, borderwidth=2)
entry_email_username.grid(column=1,row=2, columnspan=2)

entry_password = Entry(width=18, borderwidth=2)
entry_password.grid(column=1,row=3)

## Buttons ##
def action_password():
    print("Action_password")

button = Button(text="Generate Password", command=action_password, width=14)
button.grid(column=2, row=3)


def action_add():
    print("Action_add")

button = Button(text="Add Password", command=action_add, width=30)
button.grid(column=1, row=4, columnspan=2)








window.mainloop()
