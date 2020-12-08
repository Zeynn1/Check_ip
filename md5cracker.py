
import hashlib
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

def fonction_hash():
	print("Vous avez chosi de hasher un mot de passe ")
	result = input("Entrer le mot de passe que vous voulez hasher : ")
	mot_de_passe_hash = hashlib.md5(result.encode()) 
	print(mot_de_passe_hash.hexdigest())

def crack_hash_testant(hash_a_casser):
	compteur = 0
	for a in caractere_liste:
		mot = a
		mot_de_passe_hash = hashlib.md5(mot.encode())
		compteur += 1
		print(str(compteur)+ ")Try : "+str(mot))

		if hash_a_casser == mot_de_passe_hash.hexdigest():
			print("Le mot de passe est : " + str(a))
			choix()
		for b in caractere_liste:
			mot = a+b
			mot_de_passe_hash = hashlib.md5(mot.encode())
			compteur += 1
			print(str(compteur)+ ")Try : "+str(mot))

			if hash_a_casser == mot_de_passe_hash.hexdigest():
				print("Le mot de passe est : " + str(mot))
				choix()
			for c in caractere_liste:
				mot = a+b+c
				mot_de_passe_hash = hashlib.md5(mot.encode())
				compteur += 1
				print(str(compteur)+ ")Try : "+str(mot))

				if hash_a_casser == mot_de_passe_hash.hexdigest():
					print("Le mot de passe est : " + str(mot))
					choix()
				for d in caractere_liste:
					mot = a+b+c+d
					mot_de_passe_hash = hashlib.md5(mot.encode())
					compteur += 1
					print(str(compteur)+ ")Try : "+str(mot))

					if hash_a_casser == mot_de_passe_hash.hexdigest():
						print("Le mot de passe est : " + str(mot))
						choix()
def crack_hash_dict(hash_a_casser):
	compteur = 0
	listedemotdepasse = open("rockyou.txt","r", encoding ="utf-8", errors = 'ignore' ) #liste de mot de passe selectionné
	
	for mot in listedemotdepasse:
		mot = mot.split("\n")
		

		mot_de_passe_hash = hashlib.md5(mot[0].encode())
		
		compteur += 1
		
		print(str(compteur)+ ")Try : "+str(mot[0]))
		if mot_de_passe_hash.hexdigest() == hash_a_casser :
			print("Le mot de passe est : " + str(mot[0]))
			choix()
	print("Aucun mot de passe trouvé essayer avec une autre liste")
def crack_hash():
	print("Vous avez choisi de casser un mot de passe ")
	hash_a_casser = str(input("Entrer le hash a casser : "))
	print("Voulez vous attaquez le mot de passe avec : ")
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
				By Zeynn
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
		print("2 - Voulez vous cassez un mot de passe ?")
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
