cdel = 2
cins = 2

def sub(a,b):
    if(a == b):
        return 0 
    elif((a=='A' and b =='T') or (a == 'T' and b== 'A') or (a=='G' and b == 'C') or (a=='C' and b =='G')):
        return 3
    else :
        return 4



def DIST_NAIF_REC(x, y, i, j, c, dist):
    global cdel , cins
    if(i == len(x)-1 and j == len(y)-1):
        if(c < dist):
                dist = c
    else :
        if(i < len(x)-1 and j < len(y)-1):
            dist = DIST_NAIF_REC(x, y, i+1, j+1, c+sub(x[i],y[j]),dist)
        if(i < len(x)-1):
            dist = DIST_NAIF_REC(x, y, i+1, j, c+cdel,dist)
        if(j < len(y)-1):
            dist = DIST_NAIF_REC(x, y, i, j+1, c+cins,dist)
    return dist

def DIST_NAIF(x,y):
    return DIST_NAIF_REC(x, y, 0, 0, 0, 1000000)


