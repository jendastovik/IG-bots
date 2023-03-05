import requests
import urllib


def get_socks_proxys():
    """
    Gets a random proxy from a https://proxyscrape.com/free-proxy-list
    """
    url = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&anonymity=elite'
    response = requests.get(url)
    proxy_list = response.text.split('\r\n')
    if len(proxy_list) > 0:
        print(f"vráceno {len(proxy_list) - 1} proxy socks IP")
        return proxy_list[:-1]
    else:
        return None

def is_bad_proxy(pip):  
    print("checking " + pip)  
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

def check(proxy_list, n):
    working_proxys = []
    for proxy in proxy_list:
        if is_bad_proxy(proxy) == 0:
            working_proxys.append(proxy)
            print("working")
        if len(working_proxys)== n: break
    return working_proxys

def get_working_proxys(n):
    return check(get_socks_proxys(), 1)

