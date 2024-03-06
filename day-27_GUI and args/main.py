import tkinter

window = tkinter.Tk()
window.title("GUI program")
window.minsize(width=500, height=300)


# Label

my_label = tkinter.Label(text="I am a label", font=("Calibri", 24, "bold"))
my_label.pack()




window.mainloop()