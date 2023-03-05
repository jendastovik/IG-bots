import pyautogui, time, sys
print('Press Ctrl-C to quit.')
while True:
    CurserPos = pyautogui.position()
    print(CurserPos)
    time.sleep(2)
    sys.stdout.flush()

def checkProxy1(proxy_list, n):
    instagram_proxies = []
    for proxy in proxy_list[:60]:
        try:
            response = requests.get('https://www.instagram.com/', proxies={'http': 'http://' + proxy, 'https': 'https://' + proxy}, timeout=5)
            if response.status_code == 200:
                instagram_proxies.append(proxy)
                if len(instagram_proxies)>= n: break
                print("found one")
        except:
            print("timeout asi")
    return instagram_proxies

def checkProxy2(proxy_list, n):
    instagram_proxies = []
    for proxy in proxy_list[:n]:
        ans = is_bad_proxy(proxy)
        if ans == 0: 
            instagram_proxies.append(proxy)
            print("GOOD")
    return instagram_proxies

def checkProxy3(proxy):
    print("checking " + proxy)
    try:
        response = requests.get('https://w3schools.com/python/demopage.php', proxies={'http': 'http://' + proxy, 'https': 'https://' + proxy}, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False