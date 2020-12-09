




import hashlib
import os
from datetime import datetime

YELLOW = "\033[1;33m"
RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

caractere_liste = ["a","b","c","d",'e',"f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]

def fonction_hash():
	print("Vous avez chosi de hasher un mot de passe ")
	result = input("Entrer le mot de passe que vous voulez hasher : ")
	mot_de_passe_hash = hashlib.md5(result.encode()) 
	print(mot_de_passe_hash.hexdigest())

def crack_hash_testant(hash_a_casser):
	minsize = 0
	maxsize = 20
	caractere = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghikjlmnopqrstuvwxyz" 
	array = []
	time_debut = datetime.now()
	compteur = 0
	for i in range(maxsize-1):
		if i < minsize:
			array.append(0)
		else:
			array.append(-1)
	while True:
		password = ""
		array[0] += 1
		for i in range(maxsize-1):
			if array[i] > len(caractere)-1:
				array[i] = 0
				if i == maxsize-1:
					exit()
				else:
					array[i+1] += 1
			if array[i] > -1:
				password = password + caractere[array[i]]

			elif array[i] == -1:
				break
		mot_de_passe_hash = hashlib.md5(password.encode())
		compteur +=1
		print(str(compteur)+")Try: "+str(password))
		if hash_a_casser == mot_de_passe_hash.hexdigest():
			print("Le mot de passe est : " + str(password))
			time_fin = datetime.now()
			time = time_fin - time_debut
			print("Time : "+str(time)+str(" secondes"))
			choix()				

def crack_hash_dict(hash_a_casser):
	compteur = 0
	listedemotdepasse = open("rockyou.txt","r", encoding ="utf-8", errors = 'ignore' ) #liste de mot de passe selectionné
	time_debut = datetime.now()
	for mot in listedemotdepasse:
		mot = mot.split("\n")
		mot_de_passe_hash = hashlib.md5(mot[0].encode())
		compteur += 1
		print(str(compteur)+ ")Try : "+str(mot[0]))
		if mot_de_passe_hash.hexdigest() == hash_a_casser :
			print("Le mot de passe est : " + str(mot[0]))
			time_fin = datetime.now()
			time = time_fin - time_debut
			print("Time : "+str(time) +str(" secondes"))
			choix()
	print("Aucun mot de passe trouvé essayer avec une autre liste")

def crack_hash():
	print("Vous avez choisi de casser un mot de passe ")
	hash_a_casser = str(input("Entrer le hash a casser : "))
	print("Voulez vous attaquer le mot de passe avec : ")
	print("1) Un dictionnaire")
	print("2) En testant tous ")
	choix = str(input("Entrer votre choix : "))
	if choix[:1] == "1":
		crack_hash_dict(hash_a_casser)
	elif choix[:1] == "2":
		crack_hash_testant(hash_a_casser)

def flex():
	print(YELLOW)
	print("""

			███╗░░░███╗██████╗░███████╗
			████╗░████║██╔══██╗██╔════╝
			██╔████╔██║██║░░██║██████╗░
			██║╚██╔╝██║██║░░██║╚════██╗
			██║░╚═╝░██║██████╔╝██████╔╝
			╚═╝░░░░░╚═╝╚═════╝░╚═════╝░		


""")
	print(RESET)	

def choix():

	while True:
		print("1 - Voulez vous hasher un mot de passe ? ")
		print("2 - Voulez vous casser un mot de passe ?")
		choix = str(input("Que voulez vous faire ? : "))

		if choix[:] == "":
			continue
		elif choix[:1] == "1" :
			fonction_hash()
		elif choix[:1] == "2":
			crack_hash()
		else:
			continue		

def main():
	os.system("clear")
	flex()
	choix()
try:
	main()

except KeyboardInterrupt:
	print("Aurevoir ! ")


   