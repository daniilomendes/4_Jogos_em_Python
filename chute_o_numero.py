# Projeto 3 - Chute o número
# Criar um algorítimo que gera um valor aleatório e o jogador deve advinhar qual número é

import random


class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()

        try:
            while self.tentar_novamente == True:
                if int(self.valor_chute) > self.valor_aleatorio:
                    print('Chute um valor MAIS BAIXO!')
                    self.PedirValorAleatorio()
                elif int(self.valor_chute) < self.valor_aleatorio:
                    print('Chute um valor MAIS ALTO!')
                    self.PedirValorAleatorio()
                if int(self.valor_chute) == self.valor_aleatorio:
                    self.tentar_novamente = False
                    print('Parabéns, Você acertou!')
        except:
            print('Por favor, digitar apenas números inteiros!')
            self.Iniciar()

    def PedirValorAleatorio(self):
        self.valor_chute = input('Chute um número: ')

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)


chute = ChuteONumero()
chute.Iniciar()
