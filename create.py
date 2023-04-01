import bezProxy
import Do_VPN


def create(i):
    """
    vytvoří postupně i nových účtu na instagramu 
    uloží emailové adresy nových účtu v email.txt souboru
    """
    emailsNotEdited = []
    with open("/root/Desktop/kali_bots/emails.txt", "r", encoding="utf8") as file: #otevře soubor s emaily
        emailsNotEdited = file.readlines() #uloží emaily už existujících účtu do listu
    emails = [e[:-1] for e in emailsNotEdited[:-1]]
    emails.append(emailsNotEdited[-1])
    Do_VPN.connect() #pripoji na VPN server
    ch = 0
    for n in range(i):
        print(f"getting {n + 1}th bot")
        try: #zkusí vytvořit nový účet
            emails.append(bezProxy.makeBot()) #uloží ho na konec listu
        except: #při chybě přeruší cyklus a další účty už nevytváří
            print(f"some problem occured with creating {n + 1}th bot")
            break
        if ch == 5:
            Do_VPN.change_vpn() #zmeni VPN
        else: ch += 1
    Do_VPN.disconnect() #odpoji VPN

    with open("/root/Desktop/kali_bots/emails.txt", "w", encoding="utf8") as file: #otevře znovu soubor
        file.write('\n'.join(emails)) #nahraje do něj aktualizovaný list s emaily všech vytvořených účtů

create(1) #spustí funkci s parametrem i, tedy kolik nových účtů se chceme pokusit vytvořit