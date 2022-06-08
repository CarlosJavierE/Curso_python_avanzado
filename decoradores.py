# def decorador(func):
#     def envoltura():
#         print("Esto añade a mi funcion original")
#         func()
#     return envoltura

# def saludo():
#     print("Hola!")

# # saludo()

# saludo = decorador(saludo)
# saludo()

# ahora con decoradores
# esto hace los mismo pero de manera mas ordenada y clara
# sugar sintaxtico
# la funcion de un decorador añade cosas a la funcion original

# def decorador(func):
#     def envoltura():
#         print("Esto añade a mi funcion original")
#         func()
#     return envoltura

# @decorador
# def saludo():
#     print("Hola!")

# saludo()

# ejemplo 2 colocar en mayusculas el valor de una funcion

def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayusculas
def mensaje(nombre):
    return f"{nombre}, recibiste un mensaje"

print(mensaje("Cesar"))

