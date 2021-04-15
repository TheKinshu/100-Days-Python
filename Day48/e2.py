from selenium import webdriver

chrome_option = webdriver.ChromeOptions()

driver = webdriver.Chrome(executable_path='./Day48/chromedriver.exe', options=chrome_option)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

stats = driver.find_element_by_css_selector("a[title='Special:Statistics']").text

print(stats)

driver.quit()