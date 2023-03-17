from tacheA import *
import numpy as np

T = []
c_del = 2
c_ins = 2
p = 0

def concatenation(a,b):
	return((a[0]+b[0],a[1]+b[1]))

def coupure(x,y,T):
	global c_ins,c_del,p
	i = len(x)
	j = len(y)
	p = (len(x)//2) #  p <=> i*
	while(i!=p  and j!=0): # On va remonter dans le tableau T en prenant le chemin optimal jusqu'à couper i*
		if(T[i][j] == T[i-1][j-1]+sub(x[i-1],y[j-1])):
			i-=1
			j-=1
		else : 
			if(T[i][j]==T[i][j-1]+c_ins):
				j-=1
			else :
				i-=1
	return j
def SOL_2(x, y):
	global T
	n = len(x)
	m = len(y)
	p = n//2 # p = i*
	DIST_2(x,y) # Nous permet de mettre à jour un tableau T , contenant toutes les valeurs de D
	if((n==0) and (m == 0)): # cas de base 1
		return ("","")
	if ((n  == 0) and (m >= 1)): # cas de base 2 
		return(m*"-",y)
	if((m == 0 ) and (n >= 1)): # cas de base 3 
		return(x,n*"-")
	if((n==1) and (m==1)): # cas de base 4
		return(x,y)
	if((n==1) and( m!=1)): # gerer le cas où n=1 , afin d'éviter une RecursionError car on aura  p = n//2 = 1//2 = 0
		d = m-n
		return(x+d*"-",y)
	c = coupure(x,y,T)
	return concatenation(SOL_2(x[0:p],y[0:c]),SOL_2(x[p:n],y[c:m]))

def DIST_2(x, y):
	global T,c_ins,c_del
	tailleX = 2
	tailleY = len(y)

	T = np.zeros((len(x)+1, len(y)+1), dtype = int)
	T_tmp = np.zeros((tailleX, tailleY+1), dtype = int)		# Met le tableau int à 0
	for i in range(tailleX):
		T_tmp[i, 0] = i*c_del	# Met les cases i à la valeur de i
	for j in range(tailleY+1):
		T_tmp[0, j] = j*c_ins		# Met les cases j à la valeur de j
	k = 0
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
	#print(T)
	return (T[len(x)-1, len(y)-1])



def testD(x,y):
	global T 
	print(SOL_2(x,y))

