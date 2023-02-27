import requests
import urllib


def get_socks_proxys():
    """
    Gets a random proxy from a https://proxyscrape.com/free-proxy-list
    """
    url = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=yes&anonymity=all'
    response = requests.get(url)
    proxy_list = response.text.split('\r\n')
    if len(proxy_list) > 0:
        print(f"vráceno {len(proxy_list) - 1} proxy socks IP")
        return proxy_list[:-1]
    else:
        return None

def is_bad_proxy(pip):    
    try:        
        proxy_handler = urllib.request.ProxyHandler({'http': pip})        
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)        
        sock=urllib.request.urlopen('http://www.google.com')  
    except urllib.error.HTTPError as e:        
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:

        print( "ERROR:", detail)
        return 1
    return 0

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


ls = get_socks_proxys()
pr = checkProxy1(ls, 5)
print(pr)