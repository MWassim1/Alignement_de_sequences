#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from lectureFichier import *
from tacheD import *


'''
start = time.time()
x = lecture_fichier("Instances_genome/Inst_0020000_5.adn",1)
y = lecture_fichier("Instances_genome/Inst_0020000_5.adn",0)
testD(x,y)
end = time.time()
elapsed = end-start
print(str(elapsed)+" secondes\n")
'''

# TACHE D
testD("AGTACGCA", "TATGC")
testD("ATTGTA","ATCTTA")
