# imports everything from tkinter
from tkinter import *

window = Tk()
window.title("GUI program")
window.minsize(width=4, height=4)
window.config(padx=20,pady=20)


# # Label

# my_label = Label(text="I am a label", font=("Calibri", 24, "bold"))
# my_label.pack()

# # access attribute like a dictionary
# my_label["text"] = "New label text"
# # or
# my_label.config(text="new label text")


# # Button
# def button_clicked():
#     print("Button got clicked")
#     output = input.get()
#     my_label.config(text=output)

# button = Button(text="click me", command=button_clicked)
# button.pack()

# # Entry
# input = Entry(width=10)
# input.pack()
# #output = input.get()



# Label

my_label = Label(text="I am a label", font=("Calibri", 12, "bold"))
my_label.grid(column=0, row=0)

# access attribute like a dictionary
my_label["text"] = "New label text"
# or
my_label.config(text="new label text")


# Button
def button_clicked():
    print("Button got clicked")
    output = input.get()
    my_label.config(text=output)

button = Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)

button = Button(text="new_button", command=button_clicked)
button.grid(column=3, row=0)

# Entry
input = Entry(width=10)
input.grid(column=4, row=4)
#output = input.get()


window.mainloop()