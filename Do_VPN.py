import subprocess

def sign_in():
    mes = 'protonvpn-cli login FilykCZ'
    subprocess.call(mes, shell=True)

def change_vpn():
    disconnect ='protonvpn-cli d'

    subprocess.call(disconnect, shell=True)

    connect = "protonvpn-cli c -f"

    subprocess.call(connect, shell=True)

def connect():
    connect = "protonvpn-cli c -f"

    subprocess.call(connect, shell=True)

def disconnect():
    disconnect ='protonvpn-cli d'

    subprocess.call(disconnect, shell=True)