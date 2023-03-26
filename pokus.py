import Do_VPN
from selenium import webdriver

for _ in range(3):
    Do_VPN.connect()
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://www.instagram.com/accounts/emailsignup/") #otevře webovou stránku
    Do_VPN.change_vpn()

Do_VPN.disconnect()