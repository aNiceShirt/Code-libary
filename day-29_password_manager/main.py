from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

## Gets entires 
def get_entries():
    website = entry_website.get()
    email_username = entry_email_username.get()
    password = entry_password.get()
    return {"website": website, "username": email_username, "password": password}

## Saves login to a new line in txt and clears entires
def save_login():
    file = open("day-29_password_manager/data.txt", "a")
    file.write(str(get_entries())+'\n')
    file.close()
    entry_website.delete(0,END)
    #entry_email_username.delete(0,END)
    entry_password.delete(0,END)


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
entry_website.focus()

entry_email_username = Entry(width=35, borderwidth=2)
entry_email_username.grid(column=1,row=2, columnspan=2)
entry_email_username.insert(0, "mhelnaes@gmail.com")

entry_password = Entry(width=17, borderwidth=2,)
entry_password.grid(column=1,row=3, columnspan=1)

## Buttons ##
def action_password():
    print("Action_password")

button = Button(text="Generate Password", command=action_password)
button.grid(column=2, row=3, columnspan=1)


def action_add():
    save_login()

button = Button(text="Add Password", command=action_add, width=30)
button.grid(column=1, row=4, columnspan=2)








window.mainloop()