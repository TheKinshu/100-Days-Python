from email import message
from bs4 import BeautifulSoup
import requests, lxml, smtplib

URL = "https://www.amazon.ca/VTANMS-Adjustable-Foldable-Exercise-Multi-Purpose/dp/B08L7YLXQJ/ref=pd_ybh_a_2?_encoding=UTF8&psc=1&refRID=7AYNFD8M783FWVQR600C"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    "Accept-Language": "en-CA,en;q=0.9,zh-HK;q=0.8,zh;q=0.7,en-GB;q=0.6,en-US;q=0.5"
}

response =  requests.get(URL, headers=headers)
response.raise_for_status()


soup = BeautifulSoup(response.text, "lxml")

web_price = soup.find(name="span", class_="a-size-medium a-color-price")

price = float(web_price.getText().split()[1])

#
product_name = URL.split("/")[3]

my_email = "kelvc.app@gmail.com"
password = "jhljkmlnwhsybpkx"
msg = f"Subject:{product_name}\n\n{product_name} is currently ${price}.\n{URL}"
if price < 200:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="kc007919@gmail.com",
            msg=msg
        )