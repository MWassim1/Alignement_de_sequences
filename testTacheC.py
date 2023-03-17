#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from lectureFichier import *
from tacheC import *

# TACHE C 

x = lecture_fichier("Instances_genome/Inst_0000010_44.adn",1)
y = lecture_fichier("Instances_genome/Inst_0000010_44.adn",0)
print("Distance d'édition (DIST_2) : ",DIST_2(x, y),"\n")


x = lecture_fichier("Instances_genome/Inst_0000010_7.adn",1)
y = lecture_fichier("Instances_genome/Inst_0000010_7.adn",0)
print("Distance d'édition (DIST_2) : ",DIST_2(x, y),"\n")

x = lecture_fichier("Instances_genome/Inst_0000010_8.adn",1)
y = lecture_fichier("Instances_genome/Inst_0000010_8.adn",0)
print("Distance d'édition (DIST_2) : ",DIST_2(x, y),"\n")
'''

'''
'''
start = time.time()
x = lecture_fichier("Instances_genome/Inst_0020000_5.adn",1)
y = lecture_fichier("Instances_genome/Inst_0020000_5.adn",0)
print(DIST_2(x, y))
end = time.time()
elapsed = end-start
print(str(elapsed)+" secondes\n")
'''