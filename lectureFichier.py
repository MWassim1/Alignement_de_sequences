#!/usr/bin/env python
# -*- coding: utf-8 -*-

def lecture_fichier(nom_fichier,x):
    """ si x == 1 alors on retourne la séquence x
        y sinon"""

    file = open(nom_fichier,"r")
    for i in range (0,3):
        line = file.readline()
    tmp_line=""
    if(x):
        file.close()
        for k in line :
            if (k != " " and k !="\n"):
                tmp_line+=k
        return tmp_line
    line = file.readline()
    for k in line :
            if (k != " " and k!="\n"):
                tmp_line+=k
    file.close()
    return tmp_line
