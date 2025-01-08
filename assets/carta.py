class Carta:
    def __init__(self, cor, tipo):
        self.cor = cor
        self.tipo = tipo

    def __str__(self):
        return f'{self.tipo} {self.cor}'

    @staticmethod
    def cartaDeString(carta_jogada_str):
        try:
            if carta_jogada_str in ['coringa', '+4']:
                return Carta('', carta_jogada_str)
            else:
                tipo, cor = carta_jogada_str.split()
                return Carta(cor, tipo)
        except ValueError:
            raise ValueError("Entrada inválida. Certifique-se de digitar a carta no formato 'tipo cor' (exemplo: '2 azul').")