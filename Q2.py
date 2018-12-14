class Fila:
    
    def __init__(self):
        self. lista= []

    def lenght (self):
        return len(self.lista)

    def isEmpyt(self):
        return len(self.lista) == 0

    def enqueue (self, valor):
        self. lista. append(valor)

    def dequeue (self):
        if (not(self.isEmpyt())):
            self.lista.pop(0)
