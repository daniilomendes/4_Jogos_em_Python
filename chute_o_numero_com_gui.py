# Projeto 4 - Criar interface para o chute um número

import random
import PySimpleGUI as sg

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        # Layout
        layout = [
            [sg.Text('Seu Chute', size=(20, 0))],
            [sg.Input(size=(18, 0), key='ValorChute')],
            [sg.Output(size=(20, 10))]
        ]
        # Criar janela
        self.janela = sg.Window('Chute o número!')

        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        try:
            while True:
                # Receber os valores
                self.evento, self.valores = self.janela.Read()
                self.valor_chute = self.valores['ValorChute']
                # Trabalhar com estes números
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
