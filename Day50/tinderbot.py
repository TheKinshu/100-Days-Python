from selenium import webdriver
import time

EMAIL = ""


URL = "https://tinder.com/"

chrome_option = webdriver.ChromeOptions()

driver = webdriver.Chrome(executable_path='./Day48/chromedriver.exe', options=chrome_option)

driver.get(URL)
driver.maximize_window()

time.sleep(30)

while True:
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="s1107296492"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button').click()