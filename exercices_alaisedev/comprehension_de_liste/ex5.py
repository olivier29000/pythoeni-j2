# crée une liste de liste
# pour les tables de multiplications de 1 à 10
# [[1,2,3,...], [2,4,6,...],...]

print([[y * x for y in range(1, 10)] for x in range(1, 10)])
matrice = [[y * x for y in range(1, 10)] for x in range(1, 10)]

# aplati ensuite cette liste de liste
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9....
print([el for ligne in matrice for el in ligne])