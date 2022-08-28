#Feito por lucas coutinho.
import platform
import os
from time import sleep


#função de limpar terminal
def limpar_terminal():
    sistema_operacional = platform.system().upper()

    if sistema_operacional == "WINDOWS":
        os.system("cls")

    else:
        os.system("clear")


# função de saber se pode ou não entrar
def min30():
    if tempo == horario-0.5:
        print("proibido a entrada")
    elif tempo> horario+0.5:
        print("proibido a entrada")
    else:
        print("permitido a entrada")


# entrada
print("insira as informações do filme")
filme = input("insira o nome do filme: ")
limpar_terminal()
horario = float(input("insira o horario do filme: "))
limpar_terminal()
tempo = float(input("insira o horario que você chegou: "))
limpar_terminal()
#saida
min30()
sleep(3)
limpar_terminal()