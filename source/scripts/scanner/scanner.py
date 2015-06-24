#!/usr/bin/python
import socket
import subprocess
import sys
import time
from colorama import *
from datetime import datetime
init()
# Clear the screen
subprocess.call('clear', shell=True)

# Ask for input
remoteServer    = raw_input(Fore.CYAN + 'Enter a remote host to scan: ')
remoteServerIP  = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print (Fore.YELLOW + "-" * 60)
print (Fore.BLUE + "Please wait, scanning remote host", remoteServerIP)
print (Fore.RED + "-" * 60)

# Check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 1024)

# We also put in some error handling for catching errors

try:
    for port in range(1,10):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}: \t Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print 'Scanning Completed in: ', total