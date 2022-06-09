# las llaves son los sets
# los sets eliminan los elementos repetidos
# my_set = {3, 4, 5}
# print("my_set ", my_set)

# my_set2 = {"Hola", 23.3, False, True}
# print("my_set ", my_set2)

# my_set3 = {3, 3, 2}
# print("my_set ", my_set3)

# my_set4 = {[1, 2, 3], 4}
# print("my_set ", my_set4)

# empty_set = {}
# print(type(empty_set))

# real_empty_set = set()  # para poder crear un set vacio
# print(type(real_empty_set))


# mi_lista = [1, 1, 2, 3, 4, 4, 5]
# mi_set = set(mi_lista)  # eliminda los elemntos repetidos
# print(mi_set)
# se puede hacer con tuplas


# mi_set = {1, 2, 3}
# print(mi_set)
# #añadir un elemento
# mi_set.add(4)
# print(mi_set)
# # añadir miltiples elementos
# mi_set.update([1 , 2 , 5])
# print(mi_set)
# # añadir miltiples elementos
# mi_set.update((1, 7, 2), {6, 8})
# print(mi_set)
# todos los transforma a set y elmina los elemntos repetidos


# borrando sets
mi_set = {1, 2, 3, 4, 5, 6, 7}
print(mi_set)
# borrar un elemnto existente
mi_set.discard(1)
print(mi_set)
# borrar un elemnto existente
mi_set.remove(2)
print(mi_set)
# borrar un elemnto existente
mi_set.discard(10)
print(mi_set)
# borrar un elemnto existente
# mi_set.remove(12)
# print(mi_set)

# discard elimina un numero del set y si no esta devuelve el mismo set
# remove elimina un numero del set y si no esta salta un keyerror por no hay ese elemntp

# borrar un elemnto aleatorio
mi_set.pop()
print(mi_set)

# limpiar set
mi_set.clear()
print(mi_set)


