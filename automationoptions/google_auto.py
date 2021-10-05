from selenium import webdriver

#class info
class GoogleSearch():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\Jad Mershad\\Desktop\\chromedriver.exe")

    def search_result(self, name):
        self.driver.get(url="https://www.google.com/")
        search = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        search.click()
        search.send_keys(name)
        submit = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
        submit.click()
        return 1