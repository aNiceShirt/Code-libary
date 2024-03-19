from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [random.choice(letters) for letter in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for letter in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for letter in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    return password

# ---------------------------- SAVE PASSWORD ------------------------------- #

## Gets entires 
def get_entries():
    website = entry_website.get()
    email_username = entry_email_username.get()
    password = entry_password.get()
    return website, email_username, password

## Saves login to a new line in txt and clears entires
def save_login():
    website, email_username, password = get_entries()
    ## JSON data
    new_data = {
        website: {
            "email": email_username,
            "password": password,
        }
    }

    if website == "" or email_username == "" or password == "":
        messagebox.showinfo(title="Error", message="Don't leave any fields empty")
    
    # else:
    #     with open("day-29_password_manager/data.json", "r") as data_file:
    #         #Reading old data
    #         data = json.load(data_file)
    #         #Updating data with new_data
    #         data.update(new_data)
    #     with open("day-29_password_manager/data.json", "w") as data_file:
    #         json.dump(data, data_file, indent=4)
    #         entry_website.delete(0, END)
    #         entry_password.delete(0, END)
    
    else:
        try:
            with open("day-29_password_manager/data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:           ## If no file is found, create it and write new_data to it
            with open("day-29_password_manager/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:                               ## Updating data with new_data and writing to file
            data.update(new_data)
            with open("day-29_password_manager/data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:                            ## Delete enties
            entry_website.delete(0, END)
            entry_password.delete(0, END)


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
entry_website = Entry(width=20, borderwidth=2)
entry_website.grid(column=1,row=1, columnspan=1)
entry_website.focus()

entry_email_username = Entry(width=38, borderwidth=2)
entry_email_username.grid(column=1,row=2, columnspan=2)
entry_email_username.insert(0, "mhelnaes@gmail.com")

entry_password = Entry(width=20, borderwidth=2)
entry_password.grid(column=1,row=3, columnspan=1)

## Buttons ##
def action_password():
    password = generate_password()
    entry_password.delete(0,END)
    entry_password.insert(0, password)
    pyperclip.copy(password)

button = Button(text="Generate Password", command=action_password, width= 15)
button.grid(column=2, row=3, columnspan=1)


def action_add():
    save_login()

button = Button(text="Add Password", command=action_add, width=32)
button.grid(column=1, row=4, columnspan=2)

def action_search():
    website = entry_website.get()
    try:
        with open("day-29_password_manager/data.json", "r") as data_file:
            #Reading old data
            data = json.load(data_file)
            messagebox.showinfo(title=f"Login info for: {website}", message=f"Email: {data[website]['email']} \nPassword: {data[website]['password']}")
    except FileNotFoundError as error:
        messagebox.showinfo(title=error, message="No datafile found")
    except KeyError as error:
        messagebox.showinfo(title=f"Key error: {error}", message="No details found for that website")
        
button = Button(text="Search", command=action_search, width=15)
button.grid(column=2, row=1, columnspan=1)



window.mainloop()