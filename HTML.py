import requests
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


def getMailID():
    driver = webdriver.Chrome()
    driver.get("https://www.minuteinbox.com/")
    driver.implicitly_wait(10)
    output = driver.page_source

    soup = BeautifulSoup(output, "lxml")
    result = soup.find_all("span", {"id": "email"})

    for item in result:
        item = str(item)
        item = item.replace("</span>", "")
        item = item.replace('<span class="animace" id="email" style="font-size: 1.4em;">', "")
        print(item)
    driver.quit()
    return (item , driver)


def DoIG(full_name, line, user_name, pass_word):
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/accounts/emailsignup/")

    email = driver.find_element(By.CSS_SELECTOR, "input[name='emailOrPhone']")
    fullname = driver.find_element(By.CSS_SELECTOR, "input[name='fullName']")
    username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
    password = driver.find_element(By.CSS_SELECTOR, "input[name='password']")

    loginButton = driver.find_element(By.XPATH, "//button[@type='submit']")

    email.send_keys(line)
    fullname.send_keys(full_name)
    username.send_keys(user_name)
    password.send_keys(pass_word)
    loginButton.click()

def makeBot():
    pass