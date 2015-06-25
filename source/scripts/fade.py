#!usr/bin/env python
import socket
import subprocess
import sys 
import os 
from colorama import *
init()

class Fade(object):
	port = 8888
	address = 'http://127.0.0.1'

	def __init__(self, port, address):
		self.port = port
		self.address = address
		
# subprocess.call('clear', shell=True)

def banner():

	print(Fore.CYAN + "  _______          _       ")
	print" (_______)        | |        "
	print"  _____  ____   _ | |  ____  "
	print" |  ___)/ _  | / || | / _  ) "
	print" | |   ( ( | |( (_| |( (/ /  "
	print" |_|    \_||_| \____| \____) "

banner()
                    

	
