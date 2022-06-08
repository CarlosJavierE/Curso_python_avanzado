# a: int= 5       # de esta forma se hace de tipado statico en python
# print(a)

# b: str = "Hola"
# print(b)

# c: bool = True
# print(c)


# def suma(a: int, b: int) -> int:
#     return a + b

# print(suma(1, 2))

# print(suma("1", "2"))   # aunque declares las variables, python va seguir haciendo su trabajo
#                         # va concatenar los dos numeros


# from typing import Dict, List

# positives: List[int] = [1, 2, 3, 4, 5]  # se declare q va ser una lista de enteros
# # print(positives)

# # aqui se declara q users va ser un diccionario con str y int respectivamente
# users: Dict[str, int] = {
#     "argentina": 1,
#     "mexico": 34,
#     "colombia": 45
# }
# # print(users)

# # aqui se declara q countries va ser una lista que contiene diccionarios
# countries: List[Dict[str, str]] = [
#     {
#         "name": "Aregentina",
#         "people": "450000"
#     },
#     {
#         "name": "Mexico",
#         "people": "9000000"
#     },
#     {
#         "name": "Colombia",
#         "people": "999999999"
#     }
# ]
# # print(countries)


# tuplas
# from typing import Tuple

# # como una tupla es inmutable, se puede definir todos sus valores
# numbers: Tuple[int, float, int] = (1, 0.5, 1)
# print(numbers)


from typing import Tuple, Dict, List

CoordinatesType = List[Dict[str, Tuple[int, int]]] # aqui guarda en una varible la declaracion de las variable
# aqui declara la variable coordinates con la variable anterior
coordinates: CoordinatesType = [
    {
        "coord1": (1, 2),
        "coord2": (3, 5)
    },
    {
        "coord1": (0, 1),
        "coord2": (2, 5)
    }
]