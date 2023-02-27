import bezProxy
import sProxy
import Get_Proxy


def create(i):
    """
    vytvoří postupně i nových účtu na instagramu 
    uloží emailové adresy nových účtu v email.txt souboru
    """
    emails = []
    with open("emails.txt", "r", encoding="utf8") as file: #otevře soubor s emaily
        emails = file.readlines() #uloží emaily už existujících účtu do listu
        
    proxy_list = Get_Proxy.get_socks_proxys()
    for n in range(i):
        print(f"getting {n + 1}th bot")
        try: #zkusí vytvořit nový účet
            proxy_ip = proxy_list[n]
            emails.append(sProxy.makeBot(proxy_ip)) #uloží ho na konec listu
        except: #při chybě přeruší cyklus a další účty už nevytváří
            print(f"some problem occured with creating {n + 1}th bot")
            break

    with open("emails.txt", "w", encoding="utf8") as file: #otevře znovu soubor
        file.writelines('\n'.join(emails)) #nahraje do něj aktualizovaný list s emaily všech vytvořených účtů

create(2) #spustí funkci s parametrem i, tedy kolik nových účtů se chceme pokusit vytvořit