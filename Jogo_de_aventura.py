# Projeto 7 - Jogo de aventura
# Criar um jogo de decisões onde deverá ter varios finais
# diferentes de acordo com as respostas dadas


class JogoDeAventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no norte ou no sul? (n/s) '
        self.pergunta2 = 'Você prefere a espada ou o machado? (espada/machado) '
        self.pergunta3 = 'Qual é sua especialidade? (linha de frente/tatico) '
        self.finalHistoria1 = 'Você será um heroi na linha de frente!'
        self.finalHistoria2 = 'Você será um heroi protegendo todas as nossas tropas!'
        self.finalHistoria3 = 'Você irá se sacrificar na batalha!'
        self.finalHistoria4 = 'Você não é capaz de lutar nessa batalha!'

    def Iniciar(self):
        resposta1 = input(self.pergunta1)
        if resposta1 == 'n':
            resposta1B = input(self.pergunta2)
            if resposta1B == 'espada':
                print(self.finalHistoria1)
            if resposta1B == 'machado':
                print(self.finalHistoria2)
        if resposta1 == 's':
            resposta1B = input(self.pergunta3)
            if resposta1B == 'linha de frente':
                print(self.finalHistoria3)
            if resposta1B == 'tatico':
                print(self.finalHistoria4)


jogo = JogoDeAventura()
jogo.Iniciar()
