from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

## Image
tomato_image = PhotoImage(file= "day-28_Tkinter_GUI/tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)

## Timer
canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

## Label 1
label1 = Label(text="Pomodoro timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
label1.grid(column=1, row=0)

## Button 1
def action1():
    print("Button 1 clicked")

#calls action() when pressed
button = Button(text="Start", command=action1)
button.grid(column=0, row=2)

## Button 2
def action2():
    print("Button 2 clicked")

#calls action() when pressed
button = Button(text="Reset", command=action2)
button.grid(column=2, row=2)

## Label 2
label1 = Label(text="✔", font=(FONT_NAME, 12), bg=YELLOW, fg=GREEN)
label1.grid(column=1, row=3)



window.mainloop()