#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from lectureFichier import *
from tacheA import *

# TACHE A

# Tests de l'algorithme DIST_NAIF sur les fichiers fournis
print(DIST_NAIF(lecture_fichier("Instances_genome/Inst_0000010_44.adn",1) , lecture_fichier("Instances_genome/Inst_0000010_44.adn",0)))
print(DIST_NAIF(lecture_fichier("Instances_genome/Inst_0000010_7.adn",1) , lecture_fichier("Instances_genome/Inst_0000010_7.adn",0)))
print(DIST_NAIF(lecture_fichier("Instances_genome/Inst_0000010_8.adn",1) , lecture_fichier("Instances_genome/Inst_0000010_8.adn",0)))


print("Pour le fichier test.txt on obtient :")
## FICHIER TEST.TXT
# Taille d'instance jusqu'à laquelle on peut résoudre les instances fournies en moins d'une minute (DIST_NAIF)
print("Temps de calcul pour DIST_NAIF")
start = time.time()
DIST_NAIF(lecture_fichier("test.txt", 1), lecture_fichier("test.txt", 0))
end = time.time()
elapsed = end-start
print(str(elapsed)+" secondes\n")

# Taille d'instance jusqu'à laquelle on peut résoudre les instances fournies en moins d'une minute (DIST_NAIF_REC)
print("Temps de calcul pour DIST_NAIF_REC")
start = time.time()
DIST_NAIF_REC(lecture_fichier("test.txt", 1), lecture_fichier("test.txt", 0), 0, 0, 0, 1000000)
end = time.time()
elapsed = end-start
print(str(elapsed)+" secondes\n")

print("Pour le fichier test2.txt on obtient :")
## FICHIER TEST2.TXT
# Taille d'instance jusqu'à laquelle on peut résoudre les instances fournies en moins d'une minute (DIST_NAIF)
print("Temps de calcul pour DIST_NAIF")
start = time.time()
DIST_NAIF(lecture_fichier("test2.txt", 1), lecture_fichier("test2.txt", 0))
end = time.time()
elapsed = end-start
print(str(elapsed)+" secondes\n")

# Taille d'instance jusqu'à laquelle on peut résoudre les instances fournies en moins d'une minute (DIST_NAIF_REC)
print("Temps de calcul pour DIST_NAIF_REC")
start = time.time()
DIST_NAIF_REC(lecture_fichier("test2.txt", 1), lecture_fichier("test2.txt", 0), 0, 0, 0, 1000000)
end = time.time()
elapsed = end-start
print(str(elapsed)+" secondes\n")
