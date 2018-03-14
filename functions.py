from matplotlib.pyplot import *


def dessiner_points(tab):
    plot(tab[0], tab[1], 'ko')


def dessiner_enveloppe(tab):
    plot(tab[0] + [tab[0][0]], tab[1] + [tab[1][0]], 'k-')


def plus_bas(tab):
    mint = tab[1][0]
    imin = 0
    for i, y in enumerate(tab[1]):
        if y < mint:
            imin, mint = i, y
        elif y == mint:
            if tab[0][i] < tab[0][imin]:
                imin = i
    return imin


def orient(tab, i, j, k):
    x1 = tab[0][i] - tab[0][j]
    x2 = tab[0][i] - tab[0][k]
    y1 = tab[1][i] - tab[1][j]
    y2 = tab[1][i] - tab[1][k]

    if (x1 * y2 - x2 * y1) > 0:
        return 1
    elif (x1 * y2 - x2 * y1) < 0:
        return -1
    else:
        return 0


def prochain_point(tab, i):
    maximum = 0
    if i == 0:
        maximum = len(tab) - 1
    tindice = [x for x in range(len(tab[0]))]
    del tindice[i]
    for j in tindice:
        if orient(tab, i, j, maximum) > 0:
            maximum = j
    return maximum


def conv_jarvis(tab):
    i = plus_bas(tab)
    j = i
    enveloppe = [i]
    while True:
        j = prochain_point(tab, j)
        if j == i:
            return enveloppe
        enveloppe.append(j)


def maj_es(tab, es, i):
    if len(es) < 2:
        es.append(i)
        return
    while len(es) > 1:
        j= es.pop()
        if orient(tab,i,j,es[-1]) > 0:
            es.append(j)
            es.append(i)
            return



