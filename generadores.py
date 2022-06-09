# def my_gen():

#     """Un ejemplo de generadores"""

#     print("Hello world!")
#     n = 0
#     yield n     # yield es parecido a return, solo que esta no termina la funcion, la pausa y pasa al siguiente
#                 # yield va guardando la variable
#     print("Hello heaven!")
#     n = 1
#     yield n

#     print("Hello hell!")
#     n = 2
#     yield n

# a = my_gen()    #hay que instanciar para ejecutar la funcio

# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# generator expresion

my_list = [0, 1, 4, 7, 9, 10]

lista_comprehension = [x * 2 for x in my_list]
print(lista_comprehension)
my_second_gen = (x * 2 for x in my_list)    # esto me genera un iterable
for i in my_second_gen:
    print(i)

