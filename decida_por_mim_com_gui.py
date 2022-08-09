# Projeto 6 - Criar a interface do projeto 5

import random
import PySimpleGUI as sg


class DecidaPorMin:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso',
            'Confia, vai da tudo certo',
            'Aí o senhor perdeu a razão',
            'RECEBA!, melhor do mundo'
        ]

    def Iniciar(self):
        # Layout
        layout = [
                [sg.Text('Faça sua pergunta:')],
                [sg.Input()],
                [sg.Output(size=(50, 10))],
                [sg.Button('Decida por mim')]
        ]
        # Criar janela
        self.janela = sg.Window('Decida por mim!', layout=layout)

        while True:
            # Ler os valores
            self.eventos, self.valores = self.janela.Read()

            # Trabalhar com esses valores
            if self.eventos == 'Decida por mim':
                print(random.choice(self.respostas))


decida = DecidaPorMin()
decida.Iniciar()
