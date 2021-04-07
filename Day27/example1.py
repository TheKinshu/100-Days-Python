from tkinter import *


def button_clicked():
    my_label.config(text=input.get())
    print("I got clicked")



window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)
# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))

my_label.config(text="New Text")

# my_label.pack()
my_label.grid(column=0 , row=0)




# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

newbutton = Button(text="New Button", command=button_clicked)
newbutton.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=4, row=3)


# Scale
# Spinbox
# Checkbutton
# Radiobutton
# Listbox

window.mainloop()