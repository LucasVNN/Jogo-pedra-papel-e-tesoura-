listajogadas = ['PEDRA', 'PAPEL', 'TESOURA']
import random

while True:
    jogador_jogada = input("Faça sua jogada: [PEDRA | PAPEL | TESOURA]").upper()
    if 'PEDRA' in jogador_jogada or 'PAPEL' in jogador_jogada or 'TESOURA' in jogador_jogada:
        break
    else:
        print()
        print("\033[41m\033[34mOpção incorreta. Escolha somente[PEDRA | PAPEL | TESOURA]\033[m\033[m")
        print()
pc_jogada = random.choice(listajogadas)
vitoria_pc= f"\033[41mVOCÊ PERDEU!! E O COMPUTADOR VENCEU!!\033[m\033[34m jogada do PC: {pc_jogada}\033[m"
vitoria_jogador = f"\033[42mVOCÊ GANHOU!\033[m\033[31m jogada do pc: {pc_jogada}\033[m"
# print(f"PC{pc_jogada} jogador{jogador_jogada}")
#Jogadas PC:
if pc_jogada == "PEDRA" and jogador_jogada == "PAPEL":
    print(vitoria_jogador.center(65, ' '))
if pc_jogada == "PEDRA" and jogador_jogada == "TESOURA":
    print(vitoria_pc.center(65, ' '))
if pc_jogada == "PAPEL" and jogador_jogada == "TESOURA":
    print(vitoria_jogador.center(65, ' '))
if pc_jogada == "TESOURA" and jogador_jogada == "PAPEL":
    print(vitoria_pc.center(65, ' '))
if pc_jogada == "TESOURA" and jogador_jogada == "PEDRA":
    print(vitoria_jogador.center(65, ' '))
elif pc_jogada == jogador_jogada:
    print(f"Deu empate. Você jogou \033[31m{jogador_jogada}\033[m e o pc \033[31m{pc_jogada}\033[m")