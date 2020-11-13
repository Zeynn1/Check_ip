
import os
import time

import select
from bs4 import BeautifulSoup as bs
import requests as rq




YELLOW = "\033[1;33m"
RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

os.system("cls")
def start():
	print(YELLOW)
	print('''


	░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗  ██╗██████╗░
	██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝  ██║██╔══██╗
	██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░  ██║██████╔╝
	██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░  ██║██╔═══╝░
	╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗  ██║██║░░░░░
	░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝  ╚═╝╚═╝░░░░░




	''')
	print(RESET)
def check_ip(ip):
	try:
		check = ip.split(".")
	except AttributeError:
		return False
	for i in check:
		try:
			i = int(i)
		except ValueError:
			return False
		if not 0 <= i <= 255:
			return False
	return True

def track_ip(ip):
	paras = {"adresseip":ip}
	page = rq.post(url ="https://www.hostip.fr/", data = paras)
	rep = bs(page.content, "html.parser")
	

	try:
		box = rep.find(attrs={"class":"pure-u-1-1 pure-u-md-7-24 l-box content"}).get_text()
		
	except AttributeError:
		return ["unknown","unknown","unknown","unknown","unknown"]
	
	box = box.replace("Adresse Ip", "|")
	box = box.replace("Pays", "|")
	box = box.replace("Département", "|")
	box = box.replace("Ville", "|")
	box = box.replace("Host", "|")
	box = box.strip()
	info = box.split("|")
	info.pop(0)
	return info

def check_web():
    try:
        test = rq.get("https://www.hostip.fr")
    except rq.exceptions.ConnectionError:
        return False

    if test.status_code == 200:
        return True
    return True

def verifyhostip():
	print("  [" +  CYAN + "*" + RESET + "]" + CYAN +" Checking if web service is online..." + RESET)

	if check_web():
		print("  [" + GREEN + "+" + RESET + "]" + GREEN + " Web service " + YELLOW + "https://www.hostip.fr " + GREEN + "is up." + RESET)
	else:
		print("  [" + RED + "x" + RESET + "] " + RED + "Web Service isn't up." + RESET)
	print("")

def command():

	while True:
			
		cmd = str(input(YELLOW + "Ip :  "+ RESET))
		track_target = cmd
		
		try:
			
					
			
			if not check_ip(track_target):
				print("Error ip not valid.")
				continue
			info = track_ip(track_target)


		except:
			print("Error while tracking ip : " + str(track_target) )
		else:
			print("")
			print("Address Ip  : " + YELLOW + info[0] + RESET)
			print("Country     : " + YELLOW + info[1] + RESET)
			print("Departement : " + YELLOW + info[2] + RESET)
			print("City        : " + YELLOW + info[3] + RESET)
			print("Host        : " + YELLOW + info[4] + RESET)
			print("")
			continue
		
def main():
	start()
	verifyhostip()
	command()

try:
	main()

except KeyboardInterrupt:
	print("Bye")		