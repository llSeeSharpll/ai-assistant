from selenium import webdriver

#class info
class Music():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="your location of chromedriver\chromedriver.exe")

    def play(self, name):
        self.name = name
        self.driver.get(url="https://www.youtube.com/results?search_query="+name)
        video = self.driver.find_element_by_xpath('//*[@id="contents"]/ytd-video-renderer[1]')
        video.click()
        return 1