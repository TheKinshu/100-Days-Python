from typing import Text
from selenium import webdriver
import time

chrome_option = webdriver.ChromeOptions()

driver = webdriver.Chrome(executable_path='./Day48/chromedriver.exe', options=chrome_option)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

timeout = time.time() + 60*5
while True:
    if timeout < time.time():
        break
    driver.find_element_by_css_selector("#cookie").click()


    cookie_count = int(driver.find_element_by_id("money").text)

    store = driver.find_elements_by_xpath("//div[@id='store']/div")
    
    for product in store:
        price = product.find_element_by_tag_name("b")
        price = price.text.split()
        if not price == []:
            temp = ''.join(price[-1].split(","))
            if cookie_count >= int(temp):
                product.click()
                time.sleep(0.1)
                break
cps = driver.find_element_by_id("cps")

print(cps.text)