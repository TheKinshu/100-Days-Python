from bs4 import BeautifulSoup
from selenium import webdriver
import requests, lxml, time

class FORMSUBMITTER:

    def __init__(self, url) -> None:
        self.chrome_option = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe', options=self.chrome_option)
        self.driver.get(url)

    def send_information(self, links, addresses, prices):

        size = len(links)

        for i in range(size):
            time.sleep(1)
            field1 = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            field1.send_keys(" ".join(addresses[i]))

            field2 = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            field2.send_keys(prices[i])

            field3 = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            field3.send_keys(links[i])

            submit = self.driver.find_element_by_xpath("//span[@class='appsMaterialWizButtonPaperbuttonContent exportButtonContent']")
            submit.click()

            time.sleep(1)

            another = self.driver.find_element_by_xpath("//a[normalize-space()='Submit another response']")
            another.click()

            time.sleep(1)




formURL = "https://forms.gle/TLKJEg3BRVv3XrWHA"

realtorURL = "https://www.point2homes.com/CA/Apartments-For-Rent.html?location=Toronto%2C+ON&PriceMax=2%2C000&Bedrooms=1-2&search_mode=location&page=1&SelectedView=listings&LocationGeoId=783094&location_changed=&ajax=1" 

response = requests.get(realtorURL)

soup = BeautifulSoup(response.text, "lxml")

listings = soup.find_all(name="div", class_="item-right-cnt")

links = []
addresses = []
prices = []

#print(response.text)
for listing in listings:
    # Search for the important information
    link = "https://www.point2homes.com/{}".format(listing.find(name="div", class_="item-address").find(name="a").get("href"))
    address = listing.find(name="div", class_="address-container").getText().split()
    price = listing.find(name="div", class_="price has-rental-term").get("data-price")
    # Added to the offical list
    links.append(link)
    addresses.append(address)
    prices.append(price)


bot = FORMSUBMITTER(formURL)

bot.send_information(links,addresses,prices)
