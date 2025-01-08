class MaoJogador:
    def __init__(self):
        self.cartas_mao = []

    def adicionarCarta(self, lista_cartas):
        self.cartas_mao.extend(lista_cartas)

    def exibir(self):
        
        print(f'Você tem {len(self.cartas_mao)} cartas: \n')
        
        print(' | '.join(map(str, self.cartas_mao)))
        

    def podeJogar(self, carta_atual, carta_jogada):
        carta_na_mao = None
        for carta in self.cartas_mao:
            if carta.cor == carta_jogada.cor and carta.tipo == carta_jogada.tipo:
                carta_na_mao = carta
                break

        if carta_na_mao is None:
            print("Você não tem essa carta na mão \n")
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
            
            print('VOCÊ VENCEU!!!!😁🤩🎇')
            return 1
        return 0
