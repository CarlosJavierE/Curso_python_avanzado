import time

# 0 1 2 3 5 8 13

class FiboIter:
    # aqui puedo oviar el constructor porque no necesita incicializar ninguna variable
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            # self.n1 = self.n2
            # self.n2 = self.aux
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux

if __name__ == '__main__':
    fibonacci = FiboIter()  # instancio la clase FiboIter para poder acceder al iteralbe
    for element in fibonacci:   # recorro el iterable creado
        print(element)
        time.sleep(1) # va recorrer la sucesion de a cada 1 seg