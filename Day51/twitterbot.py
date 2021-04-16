from selenium import webdriver
import time
class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.chrome_option = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path='./Day51/chromedriver.exe', options=self.chrome_option)
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()
        self.download = 0
        self.upload = 0

    def get_internet_speed(self):
        time.sleep(1)
        self.driver.find_element_by_xpath("//span[@class='start-text']").click()
        time.sleep(40)
        self.download = float(self.driver.find_element_by_xpath("//span[@class='result-data-large number result-data-value download-speed']").text)
        self.upload = float(self.driver.find_element_by_xpath("//span[@class='result-data-large number result-data-value upload-speed']").text)

        print(f"Download Speed: {self.download}\nUpload Speed: {self.upload}")


    def tweet_at_provider(self, dl = 0, up  = 0):
        time.sleep(1)
        self.driver.find_element_by_xpath("//a[@aria-label='Tweet']").click()

        tweet_box = self.driver.find_element_by_xpath("//br[@data-text='true']")
        tweet_box.send_keys(f"Hey Internet Provider, why is my internet speed {self.download}down/{self.upload}up when I pay for {dl}down/{up}up")
        self.driver.find_element_by_xpath("//div[@data-testid='tweetButton']//span[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'][normalize-space()='Tweet']").click()
        
    def connecting_to_twitter(self, email, password):
        self.driver.get("https://twitter.com/home")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys(email)
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
        self.driver.find_element_by_xpath("//div[@data-testid='LoginForm_Login_Button']").click()
        

PROMISED_UP = 10
PROMISED_DOWN = 75

yourEmail = "your@email.com"
yourPassword = "some sort of password"

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.connecting_to_twitter(yourEmail, yourPassword)
bot.tweet_at_provider(PROMISED_DOWN,PROMISED_UP)

