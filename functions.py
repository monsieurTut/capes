from matplotlib.pyplot import *

def dessiner_points(tab):
    plot(tab[0], tab[1], 'ko')
        
def dessiner_Enveloppe(tab):
    plot(tab[0] + [tab[0][0]], tab[1] + [tab[1][0]], 'k-')

