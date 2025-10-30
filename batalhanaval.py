'''
Disciplina: Programação em Python
Professor: Guido Pantuza
Aluno: Michael Todoroki
Data: 28/10/2024

A) JOGO DE BATALHA NAVAL
o Jogo de batalha naval do jogador contra o computador
o Deve haver dois tabuleiros: um do jogador e outro do computador, ambos de 10 x 10
  posições
o Cada um dos participantes possui 5 embarcações. Cada uma ocupa uma única posição
  no tabuleiro
o No início de cada partida, o jogador e o computador devem determinar as posições de
  suas embarcações
o Durante a partida deve ser mostrado o tabuleiro do adversário, indicando posições já
  utilizadas: água ou embarcação afundada
o Cada jogador tem direito a dar um tiro por vez. Caso acerte uma embarcação, tem
  direito a dar outro tiro
o O vencedor é aquele que conseguir afundar todas as embarcações do adversário
o O programa deve permitir, através de um comando especial, que o jogador veja o
  tabuleiro do computador (para testes)

'''

"""
class BatalhaNaval:
    def __init__(self, tamanho=5):
        self.tamanho = tamanho
        self.tabuleiro = [['~' for _ in range(tamanho)] for _ in range(tamanho)]

    def posicionar_navio(self, x, y, orientacao, tamanho):
        if orientacao == 'H':
            if y + tamanho > self.tamanho:
                print("Navio não cabe horizontalmente.")
                return False
            for j in range(y, y + tamanho):
                if self.tabuleiro[x][j] != '~':
                    print("Posição já ocupada.")
                    return False
            for j in range(y, y + tamanho):
                self.tabuleiro[x][j] = 'N'
        elif orientacao == 'V':
            if x + tamanho > self.tamanho:
                print("Navio não cabe verticalmente.")
                return False
            for i in range(x, x + tamanho):
                if self.tabuleiro[i][y] != '~':
                    print("Posição já ocupada.")
                    return False
            for i in range(x, x + tamanho):
                self.tabuleiro[i][y] = 'N'
        else:
            print("Orientação inválida. Use 'H' para horizontal ou 'V' para vertical.")
            return False
        print(f"Navio posicionado em ({x}, {y}) orientado {orientacao}.")
        return True

    def atacar(self, x, y):
        if self.tabuleiro[x][y] == 'N':
            self.tabuleiro[x][y] = 'X'
            print("Acertou um navio!")
        elif self.tabuleiro[x][y] == '~':
            self.tabuleiro[x][y] = 'O'
            print("Água!")
        else:
            print("Posição já atacada.")

    def exibir_tabuleiro(self):
        print("  " + " ".join(str(i) for i in range(self.tamanho)))
        for i in range(self.tamanho):
            print(f"{i} " + " ".join(self.tabuleiro[i]))


import random

if __name__ == "__main__":
    jogo = BatalhaNaval(tamanho=5)
    jogo.posicionar_navio(1, 1, 'H', 3)
    jogo.posicionar_navio(3, 0, 'V', 2)
    jogo.exibir_tabuleiro()
    
    ataques = [(1,1), (0,0), (1,2), (4,4), (3,0)]
    for x, y in ataques:
        jogo.atacar(x, y)
        jogo.exibir_tabuleiro()

"""