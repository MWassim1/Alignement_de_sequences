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

def DIST_2(x, y):
	global T,c_ins,c_del
	tailleX = 2
	tailleY = len(y)

	T = np.zeros((len(x)+1, len(y)+1), dtype = int)
	T_tmp = np.zeros((tailleX, tailleY+1), dtype = int)		# Met le tableau int à 0
	for i in range(tailleX):
		T_tmp[i, 0] = i*c_del	# par définition par rapport à la réponse à la question 11
	for j in range(tailleY+1):
		T_tmp[0, j] = j*c_ins		# par définition par rapport à la réponse à la question 11

	T[0] = T_tmp[0]
	for i in range(1,len(x)+1):
		for j in range(1, tailleY+1):
			if(i%2==0): ## On regarde sur quelle ligne on est 
				k = 0
				T_tmp[k][0] = i*c_del
				T_tmp[k][j] =  min(T_tmp[k+1][j]+c_del, T_tmp[k+1][j-1]+sub(x[i-1],y[j-1]), T_tmp[k][j-1]+c_ins)  ## On regarde à "l'envers", en inversant les positions 
			else : 
				k = 1
				T_tmp[k][0] = i*c_ins
				T_tmp[k][j] =  min(T_tmp[k-1][j]+c_del, T_tmp[k-1][j-1]+sub(x[i-1],y[j-1]), T_tmp[k][j-1]+c_ins)
		T[i]=T_tmp[k] ## On affecte la ligne courante à T
		if(k):  ## On écrase la première ligne par la deuxième
			T_tmp[k-1] = T_tmp[k]
	print(T)
	return (T[len(x)-1, len(y)-1])