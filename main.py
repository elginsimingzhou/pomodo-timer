from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK ="✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    checkMark_label.config(text="")

    global reps
    reps= 0
    print(reps)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def handle_start():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps%2 != 0:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)
    elif reps%8 == 0:
        count_down(long_break_sec)
        label.config(text="Break", fg=RED)
    else:
        count_down(short_break_sec)
        label.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec <10:
        count_sec = (f"0{count_sec}")
    canvas.itemconfig(timer_text, text=(f"{count_min}:{count_sec}") )
    if count>0:
        global timer
        timer = window.after(1000, count_down, count -1)
    elif count == 0:
        handle_start()
        if reps%2 ==  0:
            repeat_times = math.floor(reps/2)
            checkMark_label.config(text=CHECK_MARK*repeat_times)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(101,112, image= tomato_img)
timer_text = canvas.create_text(103,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
label.grid(column=2, row=1)

checkMark_label = Label(bg=YELLOW, fg=GREEN)
checkMark_label.grid(column=2, row=4)

start_button = Button(text="Start", command=handle_start)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset" , command= reset_timer)
reset_button.grid(column=3, row=3)



window.mainloop()