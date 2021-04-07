from tkinter import *

def convert():
    num = float(input.get())
    km = round(num * 1.609)
    numLabel.config(text=f'{km}')

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)
label1 = Label(text="Miles")
label1.grid(column=2,row=0)

label2 = Label(text="is equal to")
label2.grid(column=0,row=1)

numLabel = Label(text="0")
numLabel.grid(column=1, row=1)

label3 = Label(text="Km")
label3.grid(column=2,row=1)

input = Entry(width=10)
input.grid(column=1, row=0)

calculate = Button(text='Calculate', command=convert)
calculate.grid(column=1, row=2)

window.mainloop()