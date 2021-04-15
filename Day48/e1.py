from selenium import webdriver

chrome_option = webdriver.ChromeOptions()

driver = webdriver.Chrome(executable_path='./Day48/chromedriver.exe', options=chrome_option)

driver.get("https://www.python.org/")
driver.maximize_window()

events = driver.find_elements_by_css_selector("div[class='medium-widget event-widget last'] ul li")

dict = {}
count = 0
for event in events:
    date = (event.find_element_by_tag_name("time").text)
    event_name = (event.find_element_by_tag_name("a").text)
    if count < len(events):
        dict[count] = {'time': date, 'name': event_name}

    count += 1

driver.quit()

print(dict)