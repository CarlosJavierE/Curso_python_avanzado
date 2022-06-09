# Union de dos conjuntos
# es la union de dos conjuntos, si tienen elementos en comun solo toma 1

# my_set1 = {3, 4, 5}
# my_set2 = {5, 6, 7}

# my_set3 = my_set1 | my_set2     # pipe es el operador de union
# print(my_set3)


# Interseccion
# es la combinacion de ambos sets, pero quedarse con los elementos que tienen en comun

# my_set1 = {3, 4, 5}
# my_set2 = {5, 6, 7}

# my_set3 = my_set1 & my_set2
# print(my_set3)


# Diferencia
# es tomar dos sets y tomar los elemneto de un set
# my_set1 = {3, 4, 5}
# my_set2 = {5, 6, 7}

# my_set3 = my_set1 - my_set2
# print(my_set3)

# my_set4 = my_set2 - my_set1
# print(my_set4)


# Diferencia simetrica
# es el resultado de tomar ambos set pero sin los elememtos en comun

my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}

my_set3 = my_set1 ^ my_set2
print(my_set3)