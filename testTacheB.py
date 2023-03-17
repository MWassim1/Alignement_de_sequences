#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from lectureFichier import *
from tacheB import *

# TACHE B

# Tests de l'algorithme DIST_1 sur les fichiers fournis
print(DIST_1(lecture_fichier("Instances_genome/Inst_0000010_44.adn",1) , lecture_fichier("Instances_genome/Inst_0000010_44.adn",0)))
print(DIST_1(lecture_fichier("Instances_genome/Inst_0000010_7.adn",1) , lecture_fichier("Instances_genome/Inst_0000010_7.adn",0)))
print(DIST_1(lecture_fichier("Instances_genome/Inst_0000010_8.adn",1) , lecture_fichier("Instances_genome/Inst_0000010_8.adn",0)))

# Tests de l'algorithme SOL_1 sur les fichiers fournis
x = lecture_fichier("Instances_genome/Inst_0000010_44.adn",1)
y = lecture_fichier("Instances_genome/Inst_0000010_44.adn",0)
#print(SOL_1(x, y, DIST_1(x, y)))

x = lecture_fichier("Instances_genome/Inst_0000010_7.adn",1)
y = lecture_fichier("Instances_genome/Inst_0000010_7.adn",0)
#print(SOL_1(x, y, DIST_1(x, y)))

x = lecture_fichier("Instances_genome/Inst_0000010_8.adn",1)
y = lecture_fichier("Instances_genome/Inst_0000010_8.adn",0)
#print(SOL_1(x, y, DIST_1(x, y)))

#Tests de l'algorithme PROG_DYN sur les fichiers fournis
x = lecture_fichier("Instances_genome/Inst_0000010_44.adn",1)
y = lecture_fichier("Instances_genome/Inst_0000010_44.adn",0)
print(PROG_DYN(x, y))

x = lecture_fichier("Instances_genome/Inst_0000010_7.adn",1)
y = lecture_fichier("Instances_genome/Inst_0000010_7.adn",0)
print(PROG_DYN(x, y))

x = lecture_fichier("Instances_genome/Inst_0000010_8.adn",1)
y = lecture_fichier("Instances_genome/Inst_0000010_8.adn",0)
print(PROG_DYN(x, y))
