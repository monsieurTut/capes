from functions import *

X = [0, 1, 1, 4, 4, 5, 5, 7, 7, 8, 11, 13]
Y = [0, 4, 8, 1, 4, 9, 6, -1, 2, 5, 6, 1]
tab = [X, Y]
dessiner_points(tab)
# dessiner_enveloppe(tab)
print(plus_bas(tab))
# print(orient(tab, 0, 3, 4))
# print(orient(tab, 8, 9, 10))
# print(orient(tab, 8, 9, 9))
# print(prochain_point(tab, 0))
# print(compute_enveloppe(tab))
# ENVELOPPE = [[X[i] for i in compute_enveloppe(tab)]]
# ENVELOPPE
dessiner_enveloppe([[X[i] for i in compute_enveloppe(tab)], [Y[i] for i in compute_enveloppe(tab)]])
show()
