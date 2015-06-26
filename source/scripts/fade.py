#!usr/bin/env python
import subprocess
import sys, os
from flask import Flask
from colorama import *
init()

# Class to run fade 
class Fade(object):
	def __init__(self):
		self.address = 'http://127.0.0.1/'
		
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


if __name__ == "__main__":
    app.run()
