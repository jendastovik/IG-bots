import requests
import random


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


