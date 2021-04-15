from selenium import webdriver
import time

EMAIL = "kc007919@gmail.com"
number = "289-395-1078"

URL = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=101174742&keywords=python%20developer&location=Canada&sortBy=R"

chrome_option = webdriver.ChromeOptions()

driver = webdriver.Chrome(executable_path='./Day48/chromedriver.exe', options=chrome_option)


driver.get(URL)
driver.maximize_window()

driver.find_element_by_link_text("Sign in").click()

time.sleep(0.5)

driver.find_element_by_css_selector("#username").send_keys(EMAIL)

driver.find_element_by_id("password").send_keys("")

driver.find_element_by_xpath("//button[normalize-space()='Sign in']").click()

time.sleep(5)

job_list = driver.find_elements_by_xpath("//ul[@class='jobs-search-results__list list-style-none']/li")


for job in job_list:
    time.sleep(1)
    job.click()
    driver.find_element_by_xpath("//span[normalize-space()='Apply on LinkedIn']").click()
    phonenumber = driver.find_element_by_class_name("fb-single-line-text__input").send_keys(number)
    driver.find_element_by_xpath("//span[normalize-space()='Next']").click()
