import random
import assets.carta as Carta
import assets.baralho as Baralho
import assets.maos_jogadores.mao_jogador as MaoJogador
import assets.maos_jogadores.mao_computador as MaoComputador

class Jogo:
    @staticmethod
    def turnoJogador(baralho, mao_jogador, carta_atual):
        while True:
            
            carta_jogada_str = input('"C" para comprar uma carta ou escolha qual carta jogar: ').lower()
            
            try:
                if carta_jogada_str == 'c':
                    mao_jogador.adicionarCarta(baralho.distribuir(1))
                    mao_jogador.exibir()
                elif carta_jogada_str in ['+4', 'coringa']:
                    coringa = Carta.Carta.cartaDeString(carta_jogada_str)
                    mao_jogador.jogarCarta(coringa)
                    print('\n')
                    print('azul | vermelho | verde | amarelo')
                    cor_escolhida = input('Escolha uma cor: ').lower()
                    if cor_escolhida not in ['azul', 'vermelho', 'verde', 'amarelo']:
                        print('\nEscolha uma cor válida')
                        continue
                    carta_jogada_str += f' {cor_escolhida}'
                    carta_jogada = Carta.Carta.cartaDeString(carta_jogada_str)
                    break
                else:
                    carta_jogada = Carta.Carta.cartaDeString(carta_jogada_str)
                    if not mao_jogador.podeJogar(carta_atual, carta_jogada):
                        print('\nJogue uma carta válida\n')
                        continue
                    mao_jogador.jogarCarta(carta_jogada)
                    break
            except ValueError as e:
                print(f"\n{e}\n")
        return carta_jogada

    @staticmethod
    def turnoComputador(baralho, mao_computador, carta_atual):
        jogada_valida = None
        while jogada_valida is None:
            i = 0
            while i - 1 <= len(mao_computador.cartas_mao):
                if i < len(mao_computador.cartas_mao):
                    if mao_computador.podeJogar(carta_atual, mao_computador.cartas_mao[i]) is False:
                        i += 1
                    else:
                        break
                else:
                    mao_computador.adicionarCarta(baralho.distribuir(1))
                    i = 0
            if i <= len(mao_computador.cartas_mao):
                jogada_valida = 1
                carta_jogada = mao_computador.cartas_mao[i]
        mao_computador.jogarCarta(carta_jogada)
        if carta_jogada.tipo == '+4' or carta_jogada.tipo == 'coringa':
            lista_cores = ['azul', 'vermelho', 'verde', 'amarelo']
            cor_escolhida = random.choice(lista_cores)
            carta_jogada = carta_jogada.tipo + ' ' + cor_escolhida
            carta_jogada = Carta.Carta.cartaDeString(carta_jogada)
        return carta_jogada

    def iniciar(self):
        baralho = Baralho.Baralho()
        baralho.embaralhar()

        mao_jogador = MaoJogador.MaoJogador()
        mao_computador = MaoComputador.MaoComputador()

        mao_jogador.adicionarCarta(baralho.distribuir(7))
        mao_computador.adicionarCarta(baralho.distribuir(7))

        carta_atual1 = baralho.cartas.pop()
        while carta_atual1.tipo in ['+2', 'pular', '+4', 'coringa', 'reverter']:
            carta_atual1 = baralho.cartas.pop()

        print('*' * 35)
        
        print(f'A carta inicial é {carta_atual1} \n')

        carta_jogada1 = carta_atual1
        carta_inicial = carta_jogada1
        vencedor = None

        while vencedor is None:
            
            print('*' * 35)

            mao_computador.exibir()
            mao_jogador.exibir()

            
            print('*' * 35)
            

            carta_jogada2 = carta_inicial

            if carta_jogada1.tipo != 'pular':
                carta_jogada2 = Jogo.turnoJogador(baralho, mao_jogador, carta_atual1)
                carta_atual2 = carta_jogada2
            if carta_jogada1.tipo == 'pular':
                carta_atual2 = carta_jogada1

            if carta_jogada1.tipo != 'pular':
                print('*' * 35)
                
                print(f'A carta atual é {carta_atual2} \n')
                
                print('*' * 35)

            verifica = mao_jogador.venceu()
            if verifica == 1:
                break

            if carta_atual2.tipo == '+4':
                mao_computador.adicionarCarta(baralho.distribuir(4))
            elif carta_atual2.tipo == '+2':
                mao_computador.adicionarCarta(baralho.distribuir(2))

            

            if carta_jogada2.tipo != 'pular':
                carta_jogada1 = Jogo.turnoComputador(baralho, mao_computador, carta_atual2)

            carta_atual1 = carta_jogada1

            if carta_jogada2.tipo != 'pular':
                print(f'O oponente jogou {carta_atual1} \n')

            if carta_atual1.tipo == '+4':
                mao_jogador.adicionarCarta(baralho.distribuir(4))
            elif carta_atual1.tipo == '+2':
                mao_jogador.adicionarCarta(baralho.distribuir(2))

            verifica = mao_computador.venceu()
            if verifica == 1:
                break
