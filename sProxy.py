from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
import pyautogui
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys


def getMailID():
    """
    vytvoří emailovou adresu s přístupem 10 minut do její schránky
    provedeno pomocí webu https://www.minuteinbox.com/
    """
    driver = webdriver.Chrome() 
    driver.get("https://www.minuteinbox.com/") #otevře webovou stránku
    driver.implicitly_wait(10) #počká na její načtení
    output = driver.page_source #uloží zdrojový kód

    soup = BeautifulSoup(output, "lxml")
    result = soup.find_all("span", {"id": "email"}) #najde část zdrojového kódu s emailem

    for item in result:
        item = str(item) #převede tuto část na text
        item = item.replace("</span>", "")
        item = item.replace('<span class="animace" id="email" style="font-size: 1.4em;">', "")
        #extrahuje z něho samotný email
        print(item)
    return (item , driver)


def DoIG(full_name, line, user_name, pass_word, PROXY):
    """
    projde celým procesem vytváření nového účtu na instagramu až do ověření emailové adresy
    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    driver.get("https://www.instagram.com/accounts/emailsignup/") #otevře instagram
    driver.implicitly_wait(10) #počká na jeho načtení

    pyautogui.click(756, 793) #odklikává cookies oznámení
    time.sleep(2) #počká na odkliknutí

    email = driver.find_element(By.CSS_SELECTOR, "input[name='emailOrPhone']")
    fullname = driver.find_element(By.CSS_SELECTOR, "input[name='fullName']")
    username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
    password = driver.find_element(By.CSS_SELECTOR, "input[name='password']") 
    #najde kolonky pro potřebné informace
    loginButton = driver.find_element(By.XPATH, "//button[@type='submit']")
    #najde tlačítko pro potvrzení
    email.send_keys(line)
    fullname.send_keys(full_name)
    username.send_keys(user_name)
    password.send_keys(pass_word)
    loginButton.click()
    #napíš informace do kolonek a potvrdí
    print("first part of putting in info done")

    driver.implicitly_wait(10) #čeká na načtení druhé části vytváření účtu
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + Keys.HOME) #vyjede na vrch okna
    time.sleep(1) #počká na odkliknutí
    pyautogui.click(1088, 519)
    time.sleep(1) #počká na odkliknutí
    pyautogui.click(1052, 1009)
    time.sleep(1) #počká na odkliknutí
    pyautogui.click(937, 676) #změní rok narození a odklikne
    #provedeno pomocí souřadnic na obrazovce, protože byl problém kolonky nalézt ve zdrojovém kódu
    print("giving some time for email to arrive")

    return driver
   
def getKeyfromInbox(driver: webdriver.Chrome):
    """
    najde v inboxu 10 minutové emailové adresy email od instagramu a extrahuje potvrzovací heslo
    """
    print("getting password")
    for i in range(100): #dá 100x obnovovací čas k tomu a by přišel potvrzovací email
        time.sleep(3) #obnovovací čas
        driver.refresh()
        out = driver.page_source #uloží zdrojový kód stránky do proměnné
        soup = BeautifulSoup(out, "lxml")
        result = soup.find_all("tbody", {"id":"schranka"}) #najde inbox s emaily pomocí knihovny bs4
        for item in result:
            item = str(item) #převede zdrojový kód na text
            x = re.findall("...... is your Instagram code", item) #najde větu s ověřovacím kódem
            if len(x)>0: #pokud byla věta nalezena
                x = x[0] #vybere první zmínění této věty
                x = x[:6] #extrahuje kód
                print(x)
                return x
    raise Exception("no mail from ig found") #vrátí error pokud není nalezen email ani po daném čase

def writeConfirmationCode(driver, key):
    """
    zadá ověřovací kód do kolonky na instagramu
    """
    keyLine = driver.find_element(By.CSS_SELECTOR, "input[name='email_confirmation_code']") #najde kolonku
    keyLine.send_keys(key) #napíše do ní kód

    loginButton = driver.find_element(By.XPATH, "//button[@type='submit']") #najde tlačítko potvrzení
    loginButton.click() #potvrdí
    driver.implicitly_wait(30) #počká zpracování servrem

def makeBot(PROXY):
    """
    provede všepotřebné pro vytvoření nového účtu na instagramu
    """
    email, mail_driver = getMailID() #získá email
    print("got mail")

    full_name = email.split(".")[0] + " " + email.split(".")[1].split("@")[0]
    #extrahuje z emailové adresy celé jméno
    username = full_name.replace(" ", "") + "ahoj"
    #extrahuje z emailové adresy uživatelské jméno
    password = "xxxxYYYYY"
    #univerzální heslo

    ig_driver = DoIG(full_name, email, username, password, PROXY=PROXY)
    print("wrote all info and waiting for confirmation kode")
    #projde celým procesem vytváření nového účtu na instagramu až do ověření emailové adresy
    
    key = getKeyfromInbox(mail_driver)
    print("got mail key")
    #najde v inboxu 10 minutové emailové adresy email od instagramu a extrahuje potvrzovací heslo
    mail_driver.quit() #opustí stránku
    
    writeConfirmationCode(ig_driver, key)
    print("accound confirmed")
    #zadá ověřovací kód do kolonky na instagramu
    ig_driver.quit() #opustí stránku

    return email #vrátí email nově vytvořeného bota
