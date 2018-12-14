class Fila:
    
    def __init__(self):
        self. pacientes= []

    def lenght (self):
        return len(self.pacientes)

    def isEmpyt(self):
        return len(self.pacientes) == 0

    def agendamento(self, pessoa):
        while len(self.pacientes)<= 20:
            self.pacientes.append(pessoa)

    def atendimento (self):
        if (not(self.isEmpyt())):
            self.pacientes.pop(0)

fila= Fila()
#agendamentos
fila.agendamento("Maria")
fila.agendamento("Ana")
fila.agendamento("João")
fila.agendamento("Pedro")
fila.agendamento("Alex")
#atendimento
fila.atendimento
fila.atendimento
fila.atendimento
#Maria é a primeira da fila e Alex o último agendado.
#Então, Maria vai ser atendida primeiro e Alex por último.
