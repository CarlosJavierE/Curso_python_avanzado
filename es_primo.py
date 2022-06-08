def es_primo(numero: int) -> bool:
    contador = 0
    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False

def run():
    numero = int(input("Escriba un numero: "))
    if es_primo("numero"):
        print("Es numero primo")
    else:
        print("No es numero primo")


if __name__ == '__main__':
    run()


# correr en consola
# mypy es_primo.py --check-untyped-defs