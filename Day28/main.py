from Day31.main import BACKGROUND_COLOR
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
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps, timer
    reps = 0
    canvas.itemconfig(timer_text, text='00:00')
    title.config(text='Timer',fg=GREEN)
    window.after_cancel(timer)
    checkLabel.config(text='')


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps

    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        title.config(text='Work',fg=GREEN)
        count_down(work_sec)
    elif reps % 8 == 0:
        title.config(text='Work', fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title.config(text='Break', fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer

        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

        mark = ''
        work_sess = math.floor(reps/2)
        for _ in range(work_sess):
            mark += '✓'
            checkLabel.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='./Day28/tomato.png')
canvas.create_image(100,112, image=tomato)
canvas.grid(column=1,row=1)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))


title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, 'bold'))
title.grid(column=1,row=0)


startBtn = Button(text='Start', highlightthickness=0, command=start_timer)
startBtn.grid(column=0,row=2)

resetBtn = Button(text='Reset', highlightthickness=0, command=reset_timer)
resetBtn.grid(column=2,row=2)

checkLabel = Label(text='', bg=YELLOW , fg=GREEN)
checkLabel.grid(column=1,row=3)

window.mainloop()