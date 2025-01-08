class MaoComputador:
    def __init__(self):
        self.cartas_mao = []

    def adicionarCarta(self, lista_cartas):
        self.cartas_mao.extend(lista_cartas)

    def exibir(self):
        print(f'O computador tem {len(self.cartas_mao)} cartas \n')
        

    def podeJogar(self, carta_atual, carta_jogada):
        if carta_jogada not in self.cartas_mao:
            return False
        if carta_atual.cor == carta_jogada.cor or carta_atual.tipo == carta_jogada.tipo or carta_jogada.cor == '':
            return True
        return False

    def jogarCarta(self, carta_jogada):
        for carta in self.cartas_mao:
            if carta.cor == carta_jogada.cor and carta.tipo == carta_jogada.tipo:
                self.cartas_mao.remove(carta)
                break

    def venceu(self):
        if len(self.cartas_mao) == 0:
            print('O oponente venceu 😿😥😭')
            return 1
        return 0
