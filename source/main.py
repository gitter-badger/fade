#!usr/bin/python
import socket
import subprocess
import sys 
import os 
from colorama import *
init()

class Fade(object):
	"""docstring for Fade"""
	def __init__(self, arg):
		self.host = 'http://127.0.0.1/'
		
	

subprocess.call('clear', shell=True)

def banner():

	print(Fore.CYAN + "  _______          _       ")
	print" (_______)        | |        "
	print"  _____  ____   _ | |  ____  "
	print" |  ___)/ _  | / || | / _  ) "
	print" | |   ( ( | |( (_| |( (/ /  "
	print" |_|    \_||_| \____| \____) "

banner()
                    

	
