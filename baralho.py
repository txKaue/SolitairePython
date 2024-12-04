import random

class Jogo:

    def __init__ (self, cartas):
        self.cartas = cartas
        self.pilha1 = []
        self.pilha2 = []
        self.pilha3 = []
        self.pilha4 = []
        self.pilha5 = []
        self.pilha6 = []
        self.pilha7 = []
        self.copas = []
        self.espadas = []
        self.paus = []
        self.ouro = []


#Essa classe é responsável por criar todas as 52 cartas do barlho.
#Além disso temos também uma função para ordenar as cartas.
#Essa função, além de ordenar, retorna uma lista com dicionarios como número e naipe das cartas.
class Cartas:

    def __init__ (self):
        cartas = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

        copas, ouro, espada, paus = [], [], [], []

        for i in cartas:
            copas.append(i)
            ouro.append(i)
            espada.append(i)
            paus.append(i)
        
        monte = [copas, ouro, espada, paus]

        self.copas = copas
        self.ouro = ouro
        self.espada = espada
        self.paus = paus
        self.monte = monte
        self.totalDeCartas = len(monte[0]) + len(monte[1]) + len(monte[2]) + len(monte[3])
    
    def __str__ (self):
        total = len(self.copas) + len(self.ouro) + len(self.paus) + len(self.espada)
        return f"Copas: {self.copas}\nPaus: {self.paus}\nOuro: {self.ouro}\nEspada: {self.espada}\nTotal: {totalDeCartas}"
    
    def OrdenarCartas(self):
        ordem = []
        for i in range(len(self.monte)):
            for j in self.monte[i]:
                item = {}
                if (i == 0):
                    item.update({j: "Copas"})
                elif (i == 1):
                    item.update({j: "Ouro"})
                elif (i == 2):
                    item.update({j: "Espada"})
                else:
                    item.update({j: "Paus"})
                ordem.append(item)
        return ordem
    
    @staticmethod
    def Embaralhar(cartas):
        novaPilha = []
        while len(cartas) > 0:
            r = random.randint(0, len(cartas)- 1)
            novaPilha.append(cartas[r])
            cartas.pop(r)
        return novaPilha

baralho = Cartas()
baralho = baralho.OrdenarCartas()
baralho = Cartas.Embaralhar(baralho)
print(baralho)
    