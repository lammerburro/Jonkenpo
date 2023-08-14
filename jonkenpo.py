##################################
import random
import os
from rich import print 
from time import sleep
from rich.progress import track 
from rich.console import Console 
##################################
def menu():
    while True:
        console = Console() 

        print("""[red]
     ______  _  ____ _______  _____  ____
 __ / / __ \/ |/ / //_/ __/ |/ / _ \/ __ ]
/ // / /_/ /    / ,< / _//    / ___/ /_/ /
\___/\____/_/|_/_/|_/___/_/|_/_/   \____/
        50: limpar tela 
        99: sair
          """)
        print("1. [red]PAPEL")
        print("2. [red]PEDRA")
        print("3. [red]TESOURA")
        print("99.[red]exit")
        sleep(2)

        n2 = int(input("jogar: "))

        def loading():
            console.log("calma là")
            sleep(1)
            console.log("[on yellow]ui")
            sleep(1)
            console.log("[on red]vai perder :) ")
            sleep(1)
            console.log("[on green]kkkk fim")
        with console.status ("[blue]carregando....") as status:
            loading()

        machine = random.randint(1,3)

        if n2 == 1:
            if machine == 1:
                print("[green]machine: papel jogador: papel")
                print("resultado: [yellow]empate")
            elif machine == 2:
                print("[green]machine: pedra jogador: papel")
                print("resultado: [blue]jogador win")
            elif machine == 3:
                print("[green]machine: tesoura jogador: papel")
                print("resultado: [red]machine win")

        elif n2 == 2:
            if machine == 1:
                print("[green]machine: papel jogador: pedra")
                print("resultado: [red]machine win")
            elif machine == 2:
                print("[green]machine: pedra jogador: pedra")
                print("resultado: [yellow]empate!")
            elif machine == 3:
                print("[green]machine: tesoura jogador: pedra")
                print("resultado: [blue]jogador win! ")

        elif n2 == 3:
            if machine == 1:
                print("[green]machine: papel jogador: tesoura")
                print("resultado: jogador win! ")
            elif machine == 2:
                print("[green]machine: pedra jogador: tesoura")
                print("resultado: [red]machine win! ")
            elif machine == 3:
                print("[green]machine: tesoura jogador: tesoura")
                print("resultado: [yellow] empate!")

        elif n2 == 99:
            print("[red] sair...")
            os.system("clear")
            sleep(1)
            return

        else:
            os.system("termux-vibrate -d 100")
            print("[red][!][blue]erro valor invalido :( ")
menu()
