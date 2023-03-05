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
    emails = [e[:-1] for e in emails[:-1]]
    emails.append(emails[-1])
    #proxy_list = Get_Proxy.get_socks_proxys()
    for n in range(i):
        print(f"getting {n + 1}th bot")
        try: #zkusí vytvořit nový účet
            #proxy_ip = proxy_list[n]
            emails.append(bezProxy.makeBot()) #uloží ho na konec listu
        except: #při chybě přeruší cyklus a další účty už nevytváří
            print(f"some problem occured with creating {n + 1}th bot")
            break

    with open("emails.txt", "w", encoding="utf8") as file: #otevře znovu soubor
        file.write('\n'.join(emails)) #nahraje do něj aktualizovaný list s emaily všech vytvořených účtů

create(1) #spustí funkci s parametrem i, tedy kolik nových účtů se chceme pokusit vytvořit