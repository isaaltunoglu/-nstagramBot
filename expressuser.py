from selenium import webdriver
import json
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time




class InteractionInfo:
    def __init__(self, username="", password=""):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome()
    def sign_in(self):
        print("Please enter your username and password")
        self.username = input("Username: ")
        self.password = input("Password: ")
        # Dosya yolunu kontrol edip oluşturuyoruz
        file_path = "accountinfo.json"
        with open(file_path, "w") as file:
            json.dump({"username": self.username, "password": self.password}, file, indent=4)
        print(f"Data saved to {file_path}")
    def load_account_info(self):
        # Dosya yolunu kontrol edip açıyoruz
        file_path = "accountinfo.json"
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                account_info = json.load(file)
                self.username = account_info["username"]
                self.password = account_info["password"]
        else:
            print("Account information file not found.")
    def login(self):
        url = f"https://www.instagram.com/"
        self.browser.get(url)
        time.sleep(3)

    # Login to Instagram
        self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.username)
        self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.password)

# Click the login button

        self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]").click()
        time.sleep(60)
        self.browser.find_element(By.XPATH,"//*[@id='mount_0_0_Ab']/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[8]/div/span/div/a/div/div[1]/div/div/span/img").click()
        self.browser.find_element(By.XPATH,"//*[@id='mount_0_0_kT']/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a").click()
        action =webdriver.ActionChains(self.browser)
        action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        time.sleep(5)

        time.sleep(3)
        #for clciking fallowers page
        self.browser.find_element(By.XPATH,"//*[@id='mount_0_0_kT']/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a").click()
        action =webdriver.ActionChains(self.browser)
        action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        time.sleep(5)
    #     return "succesfull"
    # def getFollowers(self):
    #     self.browser.find_element(By.XPATH,"//*[@id='mount_0_0_Ab']/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[8]/div/span/div/a/div/div[1]/div/div/span/img").click()
    #     self.browser.find_element(By.XPATH,"//*[@id='mount_0_0_kT']/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a").click()
    #     action =webdriver.ActionChains(self.browser)
    #     action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
    #     time.sleep(5)

    #     time.sleep(3)
    #     #for clciking fallowers page
    #     self.browser.find_element(By.XPATH,"//*[@id='mount_0_0_kT']/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a").click()
    #     action =webdriver.ActionChains(self.browser)
    #     action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
    #     time.sleep(5)




if __name__ == "__main__":
    print("This is the module.py file.")

