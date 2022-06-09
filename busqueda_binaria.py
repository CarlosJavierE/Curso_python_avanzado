from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)   # para algunos ejercicios no es necesario poner el **kwargs
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper

@execution_time
def run():
    objetivo = int(input("la raiz cuadrada de: "))
    epsilon = 0.01
    bajo = 0
    alto = max(1, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta ** 2 - objetivo) >= epsilon:
        print(f'bajo = {bajo}, alto = {alto}, respuesta = {respuesta}')
        if respuesta ** 2 > objetivo:
            alto = respuesta
        else:
            bajo = respuesta

        respuesta = (alto + bajo) / 2
    print(f'La raiza cuadra de {objetivo} es {respuesta}')

if __name__ == '__main__':
    run()