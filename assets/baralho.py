import random
import assets.carta as carta

class Baralho:
    def __init__(self):
        self.cartas = []

        cores = ['azul', 'vermelho', 'verde', 'amarelo']
        tipos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'pular', 'reverter', '+2']
        coringas = ['coringa', '+4']

        for coringa in coringas:
            for _ in range(8):
                self.cartas.append(carta.Carta('', coringa))

        for cor in cores:
            for tipo in tipos:
                for _ in range(4):
                    self.cartas.append(carta.Carta(cor, tipo))

    def embaralhar(self):
        random.shuffle(self.cartas)
        return self.cartas

    def distribuir(self, quantidade):
        cartas_distribuidas = []
        for _ in range(quantidade):
            carta = self.cartas.pop()
            cartas_distribuidas.append(carta)
        return cartas_distribuidas
