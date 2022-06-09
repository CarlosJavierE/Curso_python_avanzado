# creando un iterador

# my_list = [1, 2, 3, 4, 5]
# my_iter = iter(my_list) # internamente el lenguaje convierte a my_list a un iterador con la funcion iter

# iterando un iterador

# print(next(my_iter))    # para acceder a los elementos iterables se accedea con la funcion next
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))    # va iterar hasta el 5, como ya no hay mas iterables
# print(next(my_iter))    # salta un error de tipo StopIteration

# para poder iterar muchos elementos se hace con while

# my_list = [1, 2, 3, 4, 5]
# my_iter = iter(my_list)
# while True:
#     try:
#         element = next(my_iter)
#         print(element)
#     except StopIteration:
#         break

# # un ciclo for no es mas que azucar sintactica de lo de arriba
# # el ciclo for no existe dentro de python, es un alias de cliclo while de arriba

# for element in my_list:
#     print(element)


# construyendo un iterdor

class EvenNumbers:
    """
    clase que implementa un iterador, de todos
    los numeros pares, o los numeros pares hasta un maximo
    """

    def __init__(self, max=None):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self
    
    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration
        

