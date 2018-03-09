from matplotlib.pyplot import *

def dessiner_points(tab):
    plot(tab[0], tab[1], 'ko')
        
def dessiner_Enveloppe(tab):
    plot(tab[0] + [tab[0][0]], tab[1] + [tab[1][0]], 'k-')

def plus_bas(tab):
    mint =tab[1][0]
    imin = 0
    for i, y in enumerate(tab[1]):
        if y < mint:
            imin, mint = i, y
        elif y == mint:
            if tab[0][i]<tab[0][imin]:
                imin = i
    return imin
    
def orient (tab, i, j, k):
    x1 = tab[0][i] - tab[0][j]
    x2 = tab[0][i] - tab[0][k]
    y1 = tab[1][i] - tab[1][j]
    y2 = tab[1][i] - tab[1][k]
    
    if (x1*y2 -x2*y1) > 0:
        return 1
    elif (x1*y2 -x2*y1) < 0:
        return -1
    else:
        return 0
        
                
