import time

def fibo_gen(limite):
    n1 = 0
    n2 = 1
    counter = 0

    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux

            if aux > limite:
                raise StopIteration
        

if __name__ == '__main__':
    fibonacci = fibo_gen(100)
    for element in fibonacci:
        print(element)
        time.sleep(0.5)
