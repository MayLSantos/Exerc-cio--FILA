class No:
    def __init__(self, valor):
        self.valor= valor
        self.primeiro= None

def pecorrer(cabeça):
    atual= cabeça
    while(atual is not None):
        print(atual.valor)
        atual= atual.proximo

def buscar(cabeca, valorBusca):  
    atual = cabeca  
    while (atual is not None and atual.valor != valorBusca): 
        atual = atual.proximo 

    return atual is not None

def adicionar(cabeca, valor): 
    atual = cabeca 
    anterior = None 
    while (atual is not None): 
        anterior = atual 
        atual = atual.proximo 

    novoNo = No(valor) 
    anterior.proximo = novoNo 

def remover(cabeca, valorRemover): 
    antecessor = None 
    atual = cabeca 
    while (atual is not None and atual.valor != valorRemover):
        antecessor = atual
        atual = atual.proximo 
    if (atual is not None): 
        if (atual is cabeca): 
            cabeca = atual.proximo 
        else: 
            antecessor.proximo = atual.proximo 
    return cabeca 


def main():
    #Criar lista ligada
    cabeça= No("www.google.com.br")
    no2= No("www.wikipedia.com.br")
    cabeça.proximo= no2
    no3= No("www.youtube.com.br")
    no2.proximo= no3
    no4= No("www.ifpb.edu.br")
    no3.proximo= no4
    #burcar link
    print(buscar(cabeca, "google"))
    print(buscar(cabeca, "youtube"))
    print(buscar(cabeca, "ifpb"))

if(__name__=="__main__"): 
    main()
