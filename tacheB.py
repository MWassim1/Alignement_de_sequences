from tacheA import *
import numpy as np

T = []
c_del = 2
c_ins = 2



def sub(a,b):
    if(a == b):
        return 0 
    elif((a=='A' and b =='T') or (a == 'T' and b== 'A') or (a=='G' and b == 'C') or (a=='C' and b =='G')):
        return 3
    else :
        return 4

def DIST_1(x, y):
	global T,c_ins,c_del
	tailleX = len(x)
	tailleY = len(y)
	T = np.zeros((tailleX+1, tailleY+1), dtype = int)		# Met le tableau int à 0
	for i in range(tailleX+1):
		T[i, 0] = i*c_del	# par définition par rapport à la réponse à la question 11
	for j in range(tailleY+1):
		T[0, j] = j*c_ins		# par définition par rapport à la réponse à la question 11

	for i in range(1, tailleX+1):
		for j in range(1, tailleY+1): # par définition par rapport à la réponse à la question 7
			T[i][j] = min(T[i-1][j]+c_del, T[i-1][j-1]+sub(x[i-1],y[j-1]), T[i][j-1]+c_ins)
	print(T)
	return (T[tailleX-1, tailleY-1])


def SOL_1(x, y, T):
	global c_del, c_ins
	i = len(x)
	j = len(y)

	align1 = ""
	align2 = ""

	while((i!=0) and (j!=0)):## l'idée ici, c'est de remonter dans notre tableau T pour 'créer' le chemin optimal. On va donc faire l'opération inverse de DIST_1.
		if(T[i][j] == T[i-1][j-1]+sub(x[i-1],y[j-1])):## On remonte en diagonale haut gauche
			align1+=x[i-1]
			align2+=y[j-1]
			i-=1
			j-=1
		else : 
			if(T[i][j]==T[i][j-1]+c_ins):## On se déplace dans le tableau d'une case vers la gauche
				align1+="-"
				align2+=y[j-1]
				j-=1
			else :##On se déplace dans le tableau d'une case vers le haut .
				align1+=x[i-1]
				align2+="-"
				i-=1
	align1=align1[::-1]
	align2=align2[::-1]
	return (align1,align2)




def PROG_DYN(x, y):
	global T
	print("Distance d'édition : ",DIST_1(x, y), "\n", "Alignement optimal : ", SOL_1(x, y, T))