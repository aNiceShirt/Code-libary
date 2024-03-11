from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 15
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label1.config(text="Timer")
    label2.config(text="")
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN  * 60
    reps += 1

    if reps % 8 == 0:
        print("long")
        label1.config(text="Long break", fg=RED)
        count_down(long_break_sec)
        reps = 0

    elif reps % 2 == 0:
        print("short")
        label1.config(text="Break", fg=PINK)
        count_down(short_break_sec)

    else:
        print("work sec")
        label1.config(text="Work", fg=GREEN)
        count_down(work_sec)
   

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec  < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        checkmarks = ""
        work_sessions = int(math.floor(reps)/2)
        for mark in range(work_sessions):
            checkmarks += "✅︎"
        label2.config(text = checkmarks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

## Image
tomato_image = PhotoImage(file= "day-28_Tkinter_GUI/tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)

## Timer
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


## Label 1
label1 = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
label1.grid(column=1, row=0)

## Button 1

#calls command when pressed
button1 = Button(text="Start", command=start_timer)
button1.grid(column=0, row=2)

## Button 2

#calls command when pressed
button2 = Button(text="Reset", command=reset_timer)
button2.grid(column=2, row=2)

## Label 2
label2 = Label(font=(FONT_NAME, 12), bg=YELLOW, fg=GREEN)
label2.grid(column=1, row=3)



window.mainloop()