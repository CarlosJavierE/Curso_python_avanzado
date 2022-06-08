from datetime import datetime

# para poder averiguar cuanto tiempo tarda en ejecutarce una funcion
def execution_time(func):
    def wrapper(*args, **kwargs): # esta funcion calcula el tiempo que tarda en ejecutarce
        # *args -> no importa la cantidad de argumentos posicionales la funcion los va recibir
        # **kwargs -> no importa la cantidad de argumentos nombrados la funcion los va recibir
        # esto quiere decir que no importa que tipos de parametros la funcion se ejecuta igual 
        # * -> es el operador de desectructuracion dentro de python
        initial_time = datetime.now() # nos devuelve la fecha y hora de cuando se ejecuta el programa
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasasaron " + str(time_elapsed.total_seconds()) + " segundos")
        # total_seconds nos permite saber solo los segundos
    return wrapper

@execution_time
def randon_func():
    for _ in range(1, 1000000000):
        pass


@execution_time
def suma(a: int, b: int) -> int:
    return a + b


# ejemplo de **kwargs
@execution_time
def saludo(nombre="Cesar"): # estos son key words arguments kwargs
    print("Hola " + nombre)

randon_func()
suma(5, 10)
saludo("Carlos")