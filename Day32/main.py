import smtplib, datetime as dt, random
my_email = "kelvc.app@gmail.com"
password = "jhljkmlnwhsybpkx"

reciever_email = "nsmonkeydluffy@gmail.com"


now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday() + 1



with open("./Day32/quotes.txt", 'r') as file:
    quote = file.readlines()

randome_quote = (random.choice(quote))

if day_of_week == 4:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Creating a secure connection
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=reciever_email, 
            msg=f"Subject:Motivational Quote of The Day\n\n{randome_quote}"
        )




