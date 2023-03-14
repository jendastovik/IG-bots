#ProtonVPN
#Login: FilykCZ
#Password: &hC8E^7AbAh@AsBHz9ez

import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui
import requests
#import protonvpn_cli
#from protonvpn_cli import connection 
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Firefox

moje_IP_adresy = []
"""
list do kterého se mi budou zapisovat moje použité ip adresy
"""
a=0 
str_pocet_prihlaseni=input("Kolik pokusů?")
pocet_prihlaseni = int(str_pocet_prihlaseni)
"""
Kolikrát se má program zkusit přihlásit
"""

ip_adresa = ""

"""
V cmd spustí ProtonVPN - bohužel ne vždy s random IP adresou
"""

while a<pocet_prihlaseni:

    ip_adresa = ""

    connect = "protonvpn-cli connect --random"

    subprocess.call(connect, shell=True)

    time.sleep(5)

    response = requests.get('https://api.ipify.org')
    ip_adresa = response.text

    moje_IP_adresy.append(ip_adresa)
    print(ip_adresa)

    time.sleep(5)

    browser = webdriver.Chrome()
    url = "https://www.google.com/"
    browser.get(url)

    browser.implicitly_wait(10)

    browser.quit()

    time.sleep(5)
    a += 1

    disconnect = "protonvpn-cli disconnect"

    time.sleep(5)

print("Toto je seznam uspesne vyuzitych ip adres")
print(moje_IP_adresy)


