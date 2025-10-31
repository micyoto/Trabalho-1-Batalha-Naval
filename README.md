
# Trabalho 1 - Batalha Naval em Python 🏞️🛥️⚓

## Descrição
Este repositório contém uma implementação em Python de um jogo simples de Batalha Naval (versão baseada em posições unitárias): jogador vs computador. O jogo foi desenvolvido como exercício de programação (estruturas de dados básicas, interação por terminal e controle de fluxo).

O arquivo principal é `batalhanaval.py`, que implementa a classe `BatalhaNaval` e um loop de jogo interativo via terminal.

## Índice
- [Descrição](#descrição)
- [Trabalho Proposto](#trabalho-proposto)
- [Implementação](#️-implementação)
- [Opções Oferecidas](#opcoes-oferecidas)
- [Principais Telas](#principais-telas)
- [Como iniciar / finalizar o jogo](#como-iniciar-finalizar)
- [Conclusão](#conclusão)
- [Contribuição](#contribuição)

- [Visão geral do jogo](#visão-geral-do-jogo)
- [Requisitos](#requisitos)
- [Como executar](#como-executar)
- [Estrutura do código](#estrutura-do-código)
- [Descrição das funções principais](#descrição-das-funções-principais)
- [Fluxo do jogo e regras](#fluxo-do-jogo-e-regras)
- [Modo de teste](#modo-de-teste)
- [Limitações conhecidas](#limitações-conhecidas)
- [Possíveis melhorias](#possíveis-melhorias)
- [Conclusão (modelo)](#conclusão-modelo)



## 📋 Trabalho Proposto 🏞️🛥️⚓
**Jogo de Batalha Naval** 
1. Jogo de batalha naval do jogador contra o computador
2. Deve haver dois tabuleiros: um do jogador e outro do computador, ambos de 10 x 10
posições
3. Cada um dos participantes possui 5 embarcações. Cada uma ocupa uma única posição
no tabuleiro
4. No início de cada partida, o jogador e o computador devem determinar as posições de
suas embarcações
5. Durante a partida deve ser mostrado o tabuleiro do adversário, indicando posições já
utilizadas: água ou embarcação afundada
6. Cada jogador tem direito a dar um tiro por vez. Caso acerte uma embarcação, tem
direito a dar outro tiro
7. O vencedor é aquele que conseguir afundar todas as embarcações do adversário
8. O programa deve permitir, através de um comando especial, que o jogador veja o
tabuleiro do computador (para testes)

**Observações importantes:**
- O trabalho deve ser realizado individualmente por cada aluno.
- O trabalho deverá ser entregue, única e exclusivamente, por meio de um repositório no
GitHub.
- Abuse dos comentários para explicar o código.
- É responsabilidade do aluno garantir que o programa compile e execute corretamente,
corrigindo eventuais erros.
- Em caso de erro de sintaxe (compilação), o peso final do trabalho pode sofrer uma
redução de até 50% do peso inicial.
- Em caso de redução do peso final, a documentação adicional, como
comentários adicionais no programa fonte pode acrescer o peso final em até
50% do peso reduzido.
- Todos os trabalhos estão sujeitos a apresentação individual caso seja solicitada.
- Em caso de comprovação de fraude escolar, os pesos de todos os envolvidos serão
automaticamente anulados.
- A documentação explicativa do projeto (README) é obrigatória .

## 🛠️ Implementação
- Tabuleiros: 2 (jogador e computador), tamanho padrão 10x10.
- Embarcações: 5 por jogador. Cada embarcação ocupa exatamente 1 célula.
- Turnos: jogador e computador atiram alternadamente. Se quem atira acerta, tem direito a jogar novamente.
- Vitória: quem afundar as 5 embarcações do adversário vence.


## 👨‍💻💻 Opções Oferecidas
**Descrição das funções principais (em `BatalhaNaval`)**
- __init__(tamanho=10): Inicializa os tabuleiros (matriz com `~` para água) e contadores de embarcações.
- posicionar_embarcacao(tabuleiro, x, y): Tenta colocar uma embarcação na posição (x,y). Retorna True se posicionou, False caso já ocupado ou inválido.
- atacar(tabuleiro, x, y): Realiza um ataque nas coordenadas fornecidas. Retorna mensagens:
  - "Acertou!" (marca como `X`),
  - "Água!" (marca como `O`),
  - "Posição já atacada." ou "Coordenadas fora do tabuleiro." conforme o caso.
- exibir_tabuleiro(tabuleiro): Mostra o tabuleiro por completo (útil para ver seu próprio tabuleiro ou no modo teste).
- exibir_tabuleiro_ataque(tabuleiro): Mostra o tabuleiro do adversário escondendo navios não atingidos (substitui `N` por `~`).
- verificar_vitoria(tabuleiro): Conta as células `X` e considera vitória quando atingir 5 (número de embarcações do jogo).

**Fluxo do jogo e regras (implementadas)**
1. O jogador posiciona 5 embarcações manualmente informando coordenadas `x y` (0-9).
2. O computador posiciona aleatoriamente 5 embarcações.
3. Inicia o loop principal com menu:
   - Atacar posição — jogador informa `x y`. Se acertar, joga novamente; se errar, passa a vez ao computador.
   - Ver tabuleiro do computador (modo de teste) — exibe todas as posições do computador (útil para depuração).
   - Sair do jogo.
4. Computador ataca em coordenadas aleatórias não repetidas; se acertar, indica e joga novamente.
5. O jogo termina quando todas as 5 embarcações de um dos lados forem afundadas.

**Modo de teste / Apresentar o mapa do computador**
No menu, escolher a opção 2 — o jogo exibe o tabuleiro completo do computador (com `N` nas posições de embarcações). Isso é intencional para facilitar testes e depuração.


## 📊 Principais Telas

Abaixo seguem exemplos das principais telas/saídas do jogo no terminal (posicionamento, menu, ataques, resposta do computador e final de partida).

1) Posicionamento das embarcações (exemplo de interação):

```text
--- Seu Tabuleiro ---
  0 1 2 3 4 5 6 7 8 9
0 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
1 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
2 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
3 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
4 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
5 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
6 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
7 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
8 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
9 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Posicione sua embarcação Nº 1 de 5 (formato: x y): 0 0
Embarcação posicionada com sucesso!
Posicione sua embarcação Nº 2 de 5 (formato: x y): 3 5
Embarcação posicionada com sucesso!
...
Seu tabuleiro final:
  0 1 2 3 4 5 6 7 8 9
0 N ~ ~ ~ ~ ~ ~ ~ ~ ~
1 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
2 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
3 ~ ~ ~ ~ ~ ~ N ~ ~ ~
...
```

2) Menu principal (após posicionamento):

```text
Menu de Opções:
1. Atacar posição
2. Ver tabuleiro do computador (para testes)
3. Sair do jogo
Escolha uma opção: 1
```

3) Ataque do jogador — visualizando o tabuleiro do oponente (navios ocultos):

```text
--- Tabuleiro do Computador ---
  0 1 2 3 4 5 6 7 8 9
0 ~ ~ ~ O ~ ~ ~ ~ ~ ~
1 ~ ~ X ~ ~ ~ ~ ~ ~ ~
2 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
3 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
...
Digite as coordenadas para atacar (formato: x y): 1 1
Resultado do ataque: Acertou!
Você acertou! Jogue novamente.
```

4) Ataque do jogador — exemplo de água / posição já atacada:

```text
Digite as coordenadas para atacar (formato: x y): 0 3
Resultado do ataque: Água!
```

5) Vez do computador (exemplo):

```text
Vez do computador atacar.
Computador atacou em (4, 2): Água!
Computador atacou em (1, 1): Acertou!
O computador acertou! Ele vai jogar novamente.
```

6) Fim de jogo (exemplos):

Jogador vence:
```text
***** PARABÉNS! *****
Você afundou todas as embarcações do computador e venceu a batalha!
```

Computador vence:
```text
***** FIM DE JOGO *****
O computador afundou todas as suas embarcações. Você perdeu!
```

Esses exemplos refletem o comportamento atual do programa.

## 📈 Conclusão

Este projeto implementa uma versão funcional da Batalha Naval em Python com foco em conceitos básicos de programação: manipulação de matrizes, tratamento de entrada do usuário, controle de fluxo e estruturação em classe. Apesar das simplificações (cada embarcação ocupa uma célula), o jogo cobre a maior parte da lógica central de um jogo por turnos: posicionamento, ataque, exibição de estado e verificação de vitória.

**Limitações:** 
- Cada embarcação ocupa apenas uma célula;
- A interface é por terminal;
- Não há IA avançada;
- Posicionamento do jogador é manual;
- A verificação de vitória assume exatamente 5 acertos para declarar vencedor.

**Melhorias possíveis:** 
- Suportar navios multi-célula com validação de orientação/ocupação;
- Implementar uma IA com estratégia de perseguição após acertos;
- Adicionar testes automatizados para aumentar a confiabilidade do código;
- Suporte a salvar/carregar partidas e modo multiplayer local ou por rede;
- Melhora na interface: GUI (Tkinter, PySimpleGUI) ou web (Flask/Streamlit).

## 📂 Estrutura de Arquivos
- `batalhanaval.py`: Código-fonte principal do projeto.
- `README.md`: Este arquivo, com a descrição do projeto.

## Estrutura do código
- `BatalhaNaval` (classe): contém tabuleiros, métodos de posicionamento, ataque, exibição e verificação de vitória.
- Bloco `if __name__ == "__main__":`: código do jogo interativo — leitura de entradas, loop principal, movimentação do computador e menu de opções.

## 🚀 Como inicializar finalizar
**Requisitos**
- Python 3.8+ (qualquer versão moderna do Python 3 deve funcionar).
- Biblioteca padrão apenas (usa `random`).

**Passo a passo**
1. Abra um terminal na pasta do projeto (`c:\Users\micha\Downloads\Python\BatalhaNaval`).
2. Execute:

```powershell
python .\batalhanaval.py
```

Siga as instruções exibidas no terminal para posicionar embarcações e atacar.

## Contribuição
Contribuições são bem-vindas! Siga as etapas abaixo para contribuir:
1. Faça um fork deste repositório.
2. Crie uma branch para sua contribuição: `git checkout -b minha-contribuicao`.
3. Envie um pull request.

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).## Contribuição
Contribuições são bem-vindas! Siga as etapas abaixo para contribuir:
1. Faça um fork deste repositório.
2. Crie uma branch para sua contribuição: `git checkout -b minha-contribuicao`.
3. Envie um pull request.

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).
