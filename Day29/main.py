from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json

def find_password():
    website = webInput.get()
    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please enter a website name!")
    
    else:
        try:
            with open('./Day29/data.json', mode='r') as file:
                # Reading old data
                data = json.load(file)

            email = data[website]['email']
            password = data[website]['password']

        except FileNotFoundError:
            messagebox.showinfo(title='Error', message="No Data File Found.")

        except KeyError:
            messagebox.showinfo(title='Error', message="There is no data for that website")
        
        else:
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")

    

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():

    passwordInput.delete(0,'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)


    password_letters = [choice(letters) for char in range(nr_letters)]

    password_symbols = [choice(symbols) for char in range(nr_symbols)]

    password_numbers = [choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    passwordInput.insert(0,password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_information():

    website = webInput.get()
    username = usernameInput.get()
    password = passwordInput.get()
    new_data = {
                    website:{
                        "email": username,
                        "password": password
                }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    
    else:
        try:
            with open('./Day29/data.json', mode='r') as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open('./Day29/data.json', mode='w') as file:
                json.dump(new_data, file, indent=4)

        else:
            
            # Updating old data
            data.update(new_data)
            
            with open('./Day29/data.json', mode='w') as file:
                # Saving updated data
                json.dump(data, file, indent=4)

        finally:
            webInput.delete(0,'end')
            passwordInput.delete(0,'end')



# ---------------------------- UI SETUP ------------------------------- #

# padding 20
# width 200 height 200

window = Tk()
window.title('Password Manager')
window.config(pady=20, padx=20)

canvas = Canvas(width=200, height=200)
lock = PhotoImage(file='./Day29/logo.png')
canvas.create_image(100,100, image=lock)
canvas.grid(column=1, row=0)

# Labels
webLabel = Label(text='Website:')
webLabel.grid(column=0, row=1)

usernameLabel = Label(text='Email/Username:')
usernameLabel.grid(column=0, row=2)

passwordLabel = Label(text='Password:')
passwordLabel.grid(column=0, row=3)

# Entry
webInput = Entry(width=36)
webInput.grid(column=1, row=1)

usernameInput = Entry(width=53)
usernameInput.insert(0, 'kelvc.app@gmail.com')
usernameInput.grid(column=1, row=2, columnspan=2)

passwordInput = Entry(width=36)
passwordInput.grid(column=1, row=3)


# Button

searchBtn = Button(text='Search', width=13, command=find_password)
searchBtn.grid(column=2,row=1)

passGenerate = Button(text='Generate Password',width=13, command=generate_pass)
passGenerate.grid(column=2, row=3)

addButton = Button(text='Add', width=36, command=add_information)
addButton.grid(column=1, row=4, columnspan=2)

window.mainloop()
