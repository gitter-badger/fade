#!usr/bin/env python
import subprocess
import sys, os
from flask import Flask
from colorama import *
init()

# Class to run fade 
class Fade(object):
	port = 8888
	address = 'http://127.0.0.1'

	def __init__(self, port, address):
		self.port = port
		self.address = address
		
# subprocess.call('clear', shell=True)

# Show the banner header
def banner():

	print(Fore.YELLOW + "\t  _______          _       ")
	print"\t (_______)        | |        "
	print"\t  _____  ____   _ | |  ____  "
	print"\t |  ___)/ _  | / || | / _  ) "
	print"\t | |   ( ( | |( (_| |( (/ /  "
	print"\t |_|    \_||_| \____| \____) "

banner()

#Main menu. Yes, its not that clean and need work :/

menu_actions  = {}  

def main_menu():

    print"\t+--------------------------------------------------------------------+"
    print"\t|            Modules            |            Description             |"
    print"\t+--------------------------------------------------------------------+"
        
    print"\t+--------------------------------------------------------------------+"      
    print"\t|[1] ICMP Flood                 | Create a new flood;                |"
    print"\t|[2] DoS Attack                 | Start a Denial-of-service attack;  |"
    print"\t|[3] Port Scan                  | Run TCP port scan;                 |"
    print"\t|[4] Sniffer                    | Sniff out log traffic;             |"
    print"\t|[5] Spoof                      | Run a Spoof attack;                |"
    print"\t|--------------------------------------------------------------------|"
    print"\t|[6] Exit                       | Exit Aeon Web Attack Tool;         |"
    print"\t+--------------------------------------------------------------------+"

    choice = raw_input("> ")
    exec_menu(choice)
 
    return

if __name__ == "__main__":
    app.run()
