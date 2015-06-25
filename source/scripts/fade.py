#!usr/bin/env python
import socket
import subprocess
import sys 
import os 
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
                    

	
