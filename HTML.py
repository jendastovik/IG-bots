from bot import Bot
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
import pyautogui
import re


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
    return (item , driver)


def DoIG(full_name, line, user_name, pass_word):
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/accounts/emailsignup/")
    driver.implicitly_wait(10)
    time.sleep(3)
    

    pyautogui.click(756, 793)
    time.sleep(2)   #cookies se musí nějak vyřešit tady

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
    print("first part of putting in info done")
    driver.implicitly_wait(10)
    time.sleep(2)

    pyautogui.click(932, 567-70)
    time.sleep(2)
    pyautogui.click(925, 990-70)
    time.sleep(2)
    pyautogui.click(753, 738-70) #změní rok narození a odklikne
       
    print("giving some time for email to arrive")
    time.sleep(60) #cas na to aby došel mail

    return driver

    

    
def getKeyfromInbox(driver):
    print("getting password")
    out = driver.page_source
    soup = BeautifulSoup(out, "lxml")
    result = soup.find_all("tbody", {"id":"schranka"})
    time.sleep(10)
    for item in result:
        item = str(item)
        x = re.findall("...... is your instagram code", item)
        if len(x)>5:
            x = x[0]
            x = x[:6]
            print(x)
            return x
    raise(Exception("no mail from ig found"))

def writeConfirmationCode(driver, key):
    keyLine = driver.find_element(By.CSS_SELECTOR, "input[name='email_confirmation_code']")
    keyLine.send_keys(key)

    loginButton = driver.find_element(By.XPATH, "//button[@type='submit']")
    loginButton.click()

def makeBot():
    email, mail_driver = getMailID()
    print("got mail")
    #email = "jenicek.konnicek@parada.com" #zkusební mail
    full_name = email.split(".")[0] + " " + email.split(".")[1].split("@")[0]
    username = full_name.replace(" ", "") + "ahoj"
    password = "xxxxYYYYY"

    ig_driver = DoIG(full_name, email, username, password)
    print("wrote all info and waiting for confirmation kode")
    key = getKeyfromInbox(mail_driver)
    print("got mail key")
    writeConfirmationCode(ig_driver, key)
    print("accound confirmed")

    
    time.sleep(10)
    ig_driver.quit()

    return Bot(email, username)


print(makeBot())
"""
mail, driver  = getMailID()
print("mail")
time.sleep(90)
key = getKeyfromInbox(driver)
print(key)
"""