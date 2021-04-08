import smtplib, datetime as dt, random, pandas


myEmail = "kelvc.app@gmail.com"
password = "jhljkmlnwhsybpkx"

bday = pandas.read_csv("./Day32/birthdayEmail/birthdays.csv")
bdayList = bday.to_dict()

currentDate = dt.datetime.now()

currentMonth = currentDate.month
currentDay = currentDate.day

bdayPerson = []
bdayFound = False

for index in range(len(bdayList['name'])):
    month = bdayList['month'][index]
    day = bdayList['day'][index]

    if currentMonth == month and currentDay == day:
        bdayPerson.append(bdayList['name'][index])
        bdayPerson.append(bdayList['email'][index])
        bdayFound = True

if bdayFound:

    with open(f'./Day32/birthdayEmail/letter_templates/letter_{random.randint(1,3)}.txt') as file:
        letterTemplate = file.readlines()

    letter = ''
    for char in letterTemplate:
        letter += char.replace('[NAME]', bdayPerson[0])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Creating a secure connection
        connection.starttls()
        connection.login(user=myEmail, password=password)
        connection.sendmail(
            from_addr=myEmail, 
            to_addrs=bdayPerson[1], 
            msg=f"Subject:Happy Birthday\n\n{letter}"
        )



