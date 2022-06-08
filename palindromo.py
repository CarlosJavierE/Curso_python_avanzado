def es_palindromo(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]

def run():
    # palabra = input("Ingrese una palabra: ")
    print(es_palindromo(1000))


if __name__ == '__main__':
    run()


# mypy palindromo.py --check-untyped-defs
# esto se corre en la consola
# para saber si hay algun error de tipo typo