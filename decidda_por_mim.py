# Projeto 5 - Decida por mim
# Faça uma pergunta para o programa e ele terá que responder

import random


class DecidaPorMin:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso',
            'Confia, vai da tudo certo',
            'Aí o senhor perdeu a razão',
            'RECEBA!, melhor do mundo'
        ]

    def Iniciar(self):
        input('Faça sua pergunta: ')
        print(random.choice(self.respostas))


decida = DecidaPorMin()
decida.Iniciar()
