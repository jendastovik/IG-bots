import subprocess
import time

def sign_in():
    """Sign in to ProtonVPN"""
    mes = 'protonvpn-cli login yourUsername' #
    subprocess.call(mes, shell=True)

def change_vpn():
    """Change VPN server"""
    disconnect ='protonvpn-cli d'

    subprocess.call(disconnect, shell=True)

    connect = "protonvpn-cli c -f"

    subprocess.call(connect, shell=True)

def connect():
    """Connect to ProtonVPN"""
    connect = "protonvpn-cli c -f"

    subprocess.call(connect, shell=True)

def disconnect():
    """Disconnect from ProtonVPN"""
    disconnect ='protonvpn-cli d'

    subprocess.call(disconnect, shell=True)

def testVPN():
    connect()
    time.sleep(10)
    change_vpn()
    time.sleep(10)
    disconnect()