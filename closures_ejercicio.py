# Hola 3 -> HolaHolaHola

# def make_repeater_of(n):
#     def repeater(string):
#         # este assert afirma que se ingrese una cadena, sino levanta un error
#         assert type(string) == str, "Solo puedes utilizar cadenas"
#         return string * n
#     return repeater

# def run():
#     repeat_5 = make_repeater_of(5)
#     print(repeat_5("Hola"))

#     repeat_10 = make_repeater_of(10)
#     print(repeat_10("Platzi"))

# if __name__ == '__main__':
#     run()


def make_division_by(n: float) -> float:
    assert n != 0, "No se puede dividir entre cero"
    def numerador(x: float) -> float:
        assert type(x) == int, "Solo se admite numeros"
        return x / n
    return numerador

def run():
    divisor_2 = make_division_by(3)
    print(divisor_2(18))

if __name__ == '__main__':
    run()

# con lambda funcions

def hacer_division_de(n: float) -> float:
    return lambda x: x / n

valor = hacer_division_de(2)
print(valor(10))

hacer_una_division_con = lambda n: lambda x: x / n
division_by3 = hacer_una_division_con(3)
print(division_by3(18))
