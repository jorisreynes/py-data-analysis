import numpy as np

# 1. Créer un ndarray x comprenant 25 valeurs séquentielles commençant par 10 et finissant par 260.
x = np.linspace(10, 260, 25)
print(x)

# 2. Créer un ndarray y comprenant 10 valeurs aléatoires allant de 0 à 9.
y = np.random.randint(0, 10, size=10)
print(y)

# 3. Créer un ndarray z résultant de la concaténation de x et y.
z = np.concatenate((x, y))
print(z)

# 4. Calculer et afficher la moyenne des valeurs du ndarray z.
mean = z.mean()
print(mean)

# Soit matrix le ndarray suivant :
# [
# [15, 12, 8007],
# [121, 5, 171],
# [5123, 444, 68]
# ]

matrix = np.array([
        [15, 12, 8007],
        [121, 5, 171],
        [5123, 444, 68]
    ])

# 5. Afficher le tuple correspondant aux dimensions de matrix.
print(matrix.shape)

# 6. Changer la valeur 444 de matrix en 12688 puis l'afficher.
matrix[2, 1] = 12688
print(matrix[2, 1])

# 7. Quel est le type de données le plus adapté aux valeurs comprises dans matrix ?
# Je dirais uint16, unsigned parce qu'il y a que des valeurs positives, en partant du principe que le tableau ne va contenir 
# que des valeurs positives, 2**16=65535

# 8. Afficher le niveau de profondeur (nombre de dimensions) de matrix.
print(matrix.ndim)

# 9. Avec vos propres mots, expliquez l'intérêt d'une librairie comme NumPy dans l'analyse et la
# manipulation de grande quantité de données.
# NumPy apporte des methodes pour manipuler des données, notamment sous forme de matrices, et des meilleurs types de données. 
# C'est aussi mieux pour l'algebre lineaire
# Les données sont plus simple à manipuler, c'est plus rapide, et on peut faire plus de choses