# Projeto 1 - Simulador de dados
# Simular o uso de um dado, gerando um valor de 1 até 6
# Projeto 2 - Criar interface para o simulador de dados

import random
import PySimpleGUI as sg


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado? '

        # Layout
        self.layout = [
            [sg.Text('Jogar o Dado?')],
            [sg.Button('sim'), sg.Button('não')]
        ]

    def Iniciar(self):
        # Criar uma janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        # Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # Fazer uso dos valores
        try:
            if self.eventos == 'sim':
                self.GerarValorDoDado()
            elif self.eventos == 'não':
                print('Agradecemos sua participação')
            else:
                print('Por favor, digitar sim ou não.')
        except:
            print('Ocorreu um erro ao receber sua resposta!')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDeDado()
simulador.Iniciar()
