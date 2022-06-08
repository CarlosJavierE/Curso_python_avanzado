# def main():
#     a = 1
#     def nested():
#         print(a)
    
#     nested()

# main()

# que pasaria si envez de llamar a la funcion nested, la retorno

# def main():
#     a = 1
#     def nested():
#         print(a)
    
#     return nested       # las funciones que son retornadas se les llama closures
# my_func = main()  # my_func va a contener un funcion nested
# my_func()

# Closures
# Es una forma de acceder a variables de otros scopes a través de una nested function. 
# Se retorna la nested function y esta recuerda el valor que imprime, aunque a la hora de ejecutarla 
# no este dentro de su alcance.

# ejemplo
def make_multiplier(x):

    def multiplier(n):
        return x * n
    
    return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3)) # aqui 10 ya esta recordado por ende se puede pasar a la siguiente funcion nested
print(times4(5))
print(times10(times4(2)))
# 1 teremos una nested funcion
# 2 esta nested funcion referencia a un valor de un niver superior
# 3 y a su vez esta nested funcion es retornada
# cumple con todos los requisito para que sea closure