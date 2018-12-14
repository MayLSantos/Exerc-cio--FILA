class Fila:
    
    def __init__(self):
        self. avioes= []

    def lenght (self):
        return len(self.avioes)

    def isEmpyt(self):
        return len(self.avioes) == 0

    def chegada (self, aviao):
        self.avioes.append(aviao)

    def decolagem (self):
        if (not(self.isEmpyt())):
            self.avioes.pop(0)


i=1
primeiro= []
def controle():

    #aviões aguardando
    n= int(input("Digite o número de aviões aguardando: "))
    i= 1
    while i <= n:
        fila.chegada(i)
        i+=1

    #autorizar a decolagem
    print("Digite 1 para autorização")
    autorização= (int(input("Autorizar decolagem do próximo avião? "))
    if autorização == 1: 
        fila.decolagem()

    #adicionar avião 
    adicionar= (int(input("Adicinar a chegada de mais um avião? "))
    if adicionar == 1:
        i+=1
        fila.chegada(i)

    #aviões na lista de espera
    print("Aviões na lista de espera: ")
    print(self.avioes)

    #primeiro avião
    print("1° avião na espera: ")
    for t in range(n+1):
        v= (str(input("Caracteristica {}: ".format(t+1)))
        primeiro.append(v)

fila= Fila()
for c in range(len(self.avioes)):
    controle()
       
