from tkinter import *

## Window
window = Tk()
window.title("km to mile converter")
window.minsize(width=5, height=5)
window.config(padx=20, pady=20)


# Button click
def button_clicked():
    kilometer_converted = float(entry.get())*1.609
    label3.config(text=kilometer_converted)


#Miles Entry
entry = Entry(width=10)
#Add some text to begin with
entry.insert(END, string="0")
#Gets text in entry
entry.grid(column=1, row=0)

# Label1
label1 = Label(text="Miles")
label1.grid(column=2, row=0)

# Label2
label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

# Label3 km value
label3 = Label(text="0")
label3.grid(column=1, row=1)

# Label4 km
label4 = Label(text="km")
label4.grid(column=2, row=1)

#calls action() when pressed
button = Button(text="Convert", command=button_clicked)
button.grid(column=1, row=2)

















window.mainloop()