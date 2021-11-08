from selenium import webdriver
import keyboard

#class info
class Info():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\Jad Mershad\\Desktop\\chromedriver.exe")

    

    def get_info(self, query, engine):
        self.query = query
        self.engine = engine
        self.driver.get(url="https://www.wikipedia.org/")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        enter.click()

        #the defintion the bot can read
        info = self.driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/p[3]')
        readable_text = info.text
        engine.say("Here what i found about" +query)
        def close():
            if keyboard.is_pressed("esc"):
                self.driver.__exit__()
                engine.stop()
            engine.connect('started-word', close())
            engine.say(readable_text)
        engine.runAndWait()
        self.driver.__exit__()
        return 1