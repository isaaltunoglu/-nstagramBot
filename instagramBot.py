from my_imports import *

# Create an instance of InteractionInfo class

#create a url

def login():
    user_info = InteractionInfo()
    user_info.sign_in()
    url = f"https://www.instagram.com/"
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)

# Login to Instagram
    driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(user_info.username)
    driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(user_info.password)

# Click the login button

    driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]").click()
    time.sleep(3)
    return "succesfull"


login()
print(login())