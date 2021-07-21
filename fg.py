import socket
import threading
import concurrent.futures
import colorama
from colorama import Fore
colorama.init()


print_lock = threading.Lock()
ip = "1.1.1.1"
def scan(ip,port):
    # tcp scanner
    scanner =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    scanner.settimeout(3)

    try:
        scanner.connect((ip,port))
        scanner.close()

        with print_lock:
          print(Fore.WHITE, f"[{ip}:{port}]", Fore.GREEN , "opened")

    except:
        with print_lock:
          print(Fore.WHITE, f"[{ip}:{port}]", Fore.RED , "closed")




