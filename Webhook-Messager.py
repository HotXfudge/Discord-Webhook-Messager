from discord import SyncWebhook
import os
import sys
import time
import ctypes
import string
import colorama
from colorama import Fore
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
print(Fore.GREEN+
    "██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗     ███╗   ███╗███████╗███████╗███████╗ █████╗  ██████╗ ███████╗██████╗ \n"
    "██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝     ████╗ ████║██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝ ██╔════╝██╔══██╗\n"
    "██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝█████╗██╔████╔██║█████╗  ███████╗███████╗███████║██║  ███╗█████╗  ██████╔╝\n"
    "██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗╚════╝██║╚██╔╝██║██╔══╝  ╚════██║╚════██║██╔══██║██║   ██║██╔══╝  ██╔══██╗\n"
    "╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗     ██║ ╚═╝ ██║███████╗███████║███████║██║  ██║╚██████╔╝███████╗██║  ██║\n"
     "╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝     ╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝ \n")
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)
slowprint(Fore.GREEN+"Made by: Invalid Yuki#9597")
time.sleep(1)
slowprint(Fore.GREEN+
    "\nInput your Server Webhook: ")
input1 = input()
webhook = SyncWebhook.from_url(input1)
time.sleep(2)
slowprint(Fore.GREEN+
    "\nInput the Message you want to send: ")
input2 = input()
webhook.send(input2)
time.sleep(1)
slowprint(Fore.GREEN+
                  "\nMessage sended!")
quit()

















