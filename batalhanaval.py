'''
Disciplina: Programação em Python
Professor: Guido Pantuza
Aluno: Michael Todoroki
Data: 28/10/2024

A) JOGO DE BATALHA NAVAL
Requisitos:
- Jogo de batalha naval do jogador contra o computador
- Deve haver dois tabuleiros: um do jogador e outro do computador, ambos de 10 x 10
  posições
- Cada um dos participantes possui 5 embarcações. Cada uma ocupa uma única posição
  no tabuleiro
- No início de cada partida, o jogador e o computador devem determinar as posições de
  suas embarcações
- Durante a partida deve ser mostrado o tabuleiro do adversário, indicando posições já
  utilizadas: água ou embarcação afundada
- Cada jogador tem direito a dar um tiro por vez. Caso acerte uma embarcação, tem
  direito a dar outro tiro
- O vencedor é aquele que conseguir afundar todas as embarcações do adversário
- O programa deve permitir, através de um comando especial, que o jogador veja o
  tabuleiro do computador (para testes)

'''

## Implementação da classe BatalhaNaval

class BatalhaNaval:
    def __init__(self, tamanho=10):
        '''
        Inicializa o tabuleiro do jogador e do computador
        ### Entrada:
           tamanho (int): tamanho do tabuleiro (padrão é 10)
        ### Saída:
           Nenhuma / inicializa os tabuleiros e contadores de embarcações
        '''
        self.tamanho = tamanho # Tamanho do tabuleiro (tamanho x tamanho)
        # Tabuleiros do jogador e do computador
        self.tabuleiro_jogador = [['~' for _ in range(tamanho)] for _ in range(tamanho)]
        self.tabuleiro_computador = [['~' for _ in range(tamanho)] for _ in range(tamanho)]
        # Contadores de embarcações posicionadas
        self.embarcacoes_jogador = 0
        self.embarcacoes_computador = 0

    def posicionar_embarcacao(self, tabuleiro, x, y):
        '''
        Verifica se a posição está livre e posiciona a embarcação
        ### Entrada: 
           tabuleiro (matriz), x (int), y (int)
        ### Saída: 
           True se a embarcação foi posicionada, 
           False caso contrário
        '''
        # Verifica se a posição está dentro do tabuleiro e livre
        if 0 <= x < self.tamanho and 0 <= y < self.tamanho and tabuleiro[x][y] == '~':
            tabuleiro[x][y] = 'N'
            return True
        return False

    def atacar(self, tabuleiro, x, y):
        '''
        Realiza um ataque na posição (x, y) do tabuleiro
        ### Entrada:
           tabuleiro (matriz), x (int), y (int)
        ### Saída:
           "Acertou!" se a posição (x, y) for um navio, 
           "Água!" se for água, 
           "Posição já atacada." se já foi atacada,
           "Coordenadas fora do tabuleiro." se for inválido
        '''
        # Verifica se as coordenadas estão dentro do tabuleiro
        if not (0 <= x < self.tamanho and 0 <= y < self.tamanho):
            return "Coordenadas fora do tabuleiro."
        # Verifica o resultado do ataque
        if tabuleiro[x][y] == 'N':
            tabuleiro[x][y] = 'X'
            return "Acertou!"
        # Água
        elif tabuleiro[x][y] == '~':
            tabuleiro[x][y] = 'O'
            return "Água!"
        # Posição já atacada
        else:
            return "Posição já atacada."

    def exibir_tabuleiro(self, tabuleiro):
        '''
        Exibe o tabuleiro do jogador ou do computador.
        ### Entrada:
           tabuleiro (matriz)
        ### Saída:
           Exibição do tabuleiro
        '''
        # Cabeçalho do tabuleiro
        print("  " + " ".join(str(i) for i in range(self.tamanho)))
        # Linhas do tabuleiro
        for i in range(self.tamanho):
            print(f"{i} " + " ".join(tabuleiro[i]))

    def exibir_tabuleiro_ataque(self, tabuleiro):
        '''
        Exibe o tabuleiro do oponente escondendo navios não atingidos.
        ### Entrada:
           tabuleiro (matriz)
        ### Saída:
           Exibição do tabuleiro com navios escondidos
        '''
        # Cabeçalho do tabuleiro
        print("  " + " ".join(str(i) for i in range(self.tamanho)))
        # Linhas do tabuleiro
        for i in range(self.tamanho):
            linha_para_exibir = []
            for j in range(self.tamanho):
                if tabuleiro[i][j] == 'N':
                    linha_para_exibir.append('~') # Esconde o navio
                else:
                    linha_para_exibir.append(tabuleiro[i][j])
            print(f"{i} " + " ".join(linha_para_exibir))

    def verificar_vitoria(self, tabuleiro):
        '''
        Verifica se todas as embarcações em um tabuleiro foram afundadas.
        ### Entrada:
           tabuleiro (matriz)
        ### Saída:
           True se todas as embarcações foram afundadas, False caso contrário.
        '''
        # Conta o número de acertos
        acertos = 0
        # Percorre o tabuleiro para contar os 'X'
        for linha in tabuleiro:
            for celula in linha:
                if celula == 'X':
                    # Contabiliza as embarcações afundadas
                    acertos += 1
        # O jogo usa 5 embarcações
        return acertos == 5


## Programa principal para rodar a classe BatalhaNaval
# Importa a biblioteca random para posicionamento aleatório
import random

# Executa o jogo
if __name__ == "__main__":
    # Cria uma instância do jogo
    jogo = BatalhaNaval(tamanho=10)  # Tabuleiro 10x10 

    # Exibir cabeçalho do jogo
    print("***** Início do Jogo de Batalha Naval *****")
    print("Trabalho da Disciplina de Programação em Python")
    print("Professor: Guido Pantuza")
    print("Aluno: Michael Todoroki")
    print("Data: 28/10/2024")
    print("********************************************\n")

    # Instruções iniciais
    print("Início do jogo. \n")
    # Posicionar embarcações do jogador
    while jogo.embarcacoes_jogador < 5:
        # Exibir tabuleiro do jogador
        print("\n--- Seu Tabuleiro ---")
        jogo.exibir_tabuleiro(jogo.tabuleiro_jogador)

        # Loop até o jogador posicionar uma embarcação válida
        try:
            # Solicitar posição da embarcação
            print(f"Posicione sua embarcação Nº {jogo.embarcacoes_jogador + 1} de 5 (formato: x y): ")
            # Lê as coordenadas x e y
            # x e y são inteiros representando as coordenadas no tabuleiro
            x, y = map(int, input().split())
            
            # Tenta posicionar a embarcação
            if jogo.posicionar_embarcacao(jogo.tabuleiro_jogador, x, y):
                # Incrementa o contador de embarcações do jogador
                jogo.embarcacoes_jogador += 1
                print("Embarcação posicionada com sucesso!")
            else:
                # Posição inválida ou já ocupada
                print("Posição inválida ou já ocupada. Tente novamente.")
        except (ValueError, IndexError):
            # Tratamento de erro para entrada inválida
            print("Entrada inválida. Por favor, insira dois números (de 0 a 9) separados por espaço.")
            continue

    # Posicionar embarcações do computador
    while jogo.embarcacoes_computador < 5:
        # Gera coordenadas aleatórias dentro dos limites do tabuleiro
        x, y = random.randint(0, 9), random.randint(0, 9)
        # Tenta posicionar a embarcação do computador se não estiver ocupada
        if jogo.posicionar_embarcacao(jogo.tabuleiro_computador, x, y):
            # Incrementa o contador de embarcações do computador
            jogo.embarcacoes_computador += 1

    # Primeira parte do jogo concluída

    # Exibir tabuleiro final do jogador
    print("\nSeu tabuleiro final:")
    jogo.exibir_tabuleiro(jogo.tabuleiro_jogador)
    print("\nPosicionamento das embarcações concluído. Que comece a batalha!\n")

    # set para armazenar posições já atacadas pelo computador
    posicoes_atacadas_comp = set()

    # Menu de opções com tratamento de exceção para o loop principal
    try:
        while True:
            # Exibe o menu de opções
            print("Menu de Opções:")
            print("1. Atacar posição")
            print("2. Ver tabuleiro do computador (para testes)")
            print("3. Sair do jogo")

            # Lê a opção do jogador
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                # Loop para garantir que o jogador insira coordenadas válidas para o ataque
                while True:
                    try:
                        # Exibe o tabuleiro do computador com navios escondidos
                        print("\n--- Tabuleiro do Computador ---")
                        jogo.exibir_tabuleiro_ataque(jogo.tabuleiro_computador)

                        # Solicita as coordenadas para o ataque
                        ataque_str = input("Digite as coordenadas para atacar (formato: x y): ")
                        x, y = map(int, ataque_str.split())
                        
                        # Realiza o ataque
                        resultado = jogo.atacar(jogo.tabuleiro_computador, x, y)
                        print(f"Resultado do ataque: {resultado}")

                        # Se o ataque foi em água ou já acertada, sai do loop de ataque
                        if resultado == "Acertou!" or resultado == "Água!":
                            # Se o jogador acertou, ele joga de novo
                            if resultado == "Acertou!":
                                print("Você acertou! Jogue novamente.")
                                # Verifica a vitória imediatamente após o acerto
                                if jogo.verificar_vitoria(jogo.tabuleiro_computador):
                                    break # Sai do loop de ataque para o loop principal finalizar o jogo
                                continue # Pula para a próxima iteração do loop de ataque do jogador
                            break # Se foi água, sai do loop e passa a vez
                        else:
                            # Informa o erro (posição já atacada ou fora do tabuleiro) e pede para tentar de novo
                            print("Tente novamente.")

                    except (ValueError, IndexError):
                        print("Entrada inválida. Por favor, insira dois números separados por espaço.")
                        continue

                # Verifica se o jogador venceu
                if jogo.verificar_vitoria(jogo.tabuleiro_computador):
                    # Se o jogador venceu, exibe mensagem de fim de jogo
                    print("\n***** PARABÉNS! *****")
                    print("Você afundou todas as embarcações do computador e venceu a batalha!")
                    break

                # Vez do computador atacar
                print("\nVez do computador atacar.")
                while True:
                    # Gera coordenadas aleatórias para o ataque no tabuleiro 10x10
                    x_comp, y_comp = random.randint(0, 9), random.randint(0, 9)
                    # Verifica se a posição já foi atacada ou não
                    if (x_comp, y_comp) not in posicoes_atacadas_comp:
                        # Adiciona a posição ao conjunto de posições atacadas
                        posicoes_atacadas_comp.add((x_comp, y_comp))
                        
                        # Ataca a posição escolhida
                        resultado_comp = jogo.atacar(jogo.tabuleiro_jogador, x_comp, y_comp)
                        print(f"Computador atacou em ({x_comp}, {y_comp}): {resultado_comp}")

                        # Se o computador acertou, ele joga de novo
                        if resultado_comp == "Acertou!":
                            print("O computador acertou! Ele vai jogar novamente.")
                            # Verifica se o computador venceu
                            if jogo.verificar_vitoria(jogo.tabuleiro_jogador):
                                break # Sai do loop de ataque do computador
                            continue # Continua no loop de ataque do computador
                        
                        break # Se foi água, sai do loop e termina a vez do computador

                # Verifica se o computador venceu
                if jogo.verificar_vitoria(jogo.tabuleiro_jogador):
                    # Se o computador venceu, exibe mensagem de fim de jogo
                    print("\n***** FIM DE JOGO *****")
                    print("O computador afundou todas as suas embarcações. Você perdeu!")
                    break

                # Exibir tabuleiros após a rodada
                print("\n--- Seu Tabuleiro ---")
                jogo.exibir_tabuleiro(jogo.tabuleiro_jogador)
                
                print("\n--- Tabuleiro do Computador ---")
                jogo.exibir_tabuleiro_ataque(jogo.tabuleiro_computador)
                print("-" * 30)

            elif opcao == "2":
                # Modo de Teste: Exibe o tabuleiro do computador completo
                print("Tabuleiro do Computador (Modo de Teste):")
                jogo.exibir_tabuleiro(jogo.tabuleiro_computador)
                continue
            elif opcao == "3":
                # Encerrar o jogo
                print("\nObrigado por jogar Batalha Naval! Até a próxima, marujo!")
                jogo.exibir_tabuleiro(jogo.tabuleiro_jogador)
                jogo.exibir_tabuleiro_ataque(jogo.tabuleiro_computador)
                print("-" * 30)
                print("***** Fim do Jogo de Batalha Naval *****")
                break
            else:
                # Opção inválida
                print("Opção inválida.")
                continue
    except KeyboardInterrupt:
        # Tratamento para interrupção do jogo pelo usuário Ctrl+C
        print("\n\nJogo interrompido pelo usuário. Saindo...")
    except Exception as e:
        # Tratamento genérico de exceções
        print(f"\nOcorreu um erro inesperado: {e}")
        print("Encerrando o jogo.")


