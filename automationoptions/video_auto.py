import keyboard
from selenium import webdriver

#class info
class Music():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\Jad Mershad\\Desktop\\chromedriver.exe")

    def play(self, name):
        self.name = name
        self.driver.get(url="https://www.youtube.com/results?search_query="+name)
        video = self.driver.find_element_by_xpath('//*[@id="contents"]/ytd-video-renderer[1]')
        video.click()
        if keyboard.is_pressed("esc"):
            self.driver.__exit__()