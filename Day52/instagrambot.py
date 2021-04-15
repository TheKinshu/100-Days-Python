from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
import time

class InstagramBot:
    def __init__(self) -> None:
        self.chrome_option = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe', options=self.chrome_option)

    def login(self, id, ps, target):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)
        self.driver.find_element_by_name("username").send_keys(id)
        self.driver.find_element_by_name("password").send_keys(ps)
        self.driver.find_element_by_xpath("//div[contains(text(),'Log In')]").click()

        time.sleep(5)
        self.driver.get("https://www.instagram.com/{}".format(target))


    def find_followers(self,target):
        self.driver.find_element_by_css_selector("a[href='/{}/followers/']".format(target)).click()
        time.sleep(2)

    def follow(self):
        body = self.driver.find_element_by_xpath("//div[@class='isgrP']")
        scroll = 0

        while scroll < 5:
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', body)
            time.sleep(2)
            scroll += 1

        follower_list = self.driver.find_elements_by_xpath("//div[@class='isgrP']//li")

        for follower in follower_list:
            try:
                follower.find_element_by_tag_name("button").click()
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()    



TARGET_ACCOUNT = "coding"
USERNAME = ""
PASSWORD = ""

bot = InstagramBot()

bot.login(USERNAME, PASSWORD, TARGET_ACCOUNT)

bot.find_followers(TARGET_ACCOUNT)

bot.follow()