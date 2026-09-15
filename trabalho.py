import time

def ler_voto():
    while True:
        try:
            while True:
                opc = int(input("Digite o número do seu voto:\n"))
                if opc < 0 or opc > 6:
                    print("Digite um valor entre 0 e 6!")
                else:
                    break
            break
        except ValueError:
            print("Apenas um número entre 0 e 6 é permitido!")
    return opc

def cont_voto(opc):
    paulo = 0
    polvo = 0
    gusto = 0
    marcio_malonaro = 0
    nulo = 0
    branco = 0
    match opc:
        case 1:
            print("Votando em Paulo Matagal...")
            time.sleep(0.5)
            while True:
                print("------- Confirmar voto? (y/n)")
                conf = input().lower()
                if conf == "y" or conf == "n":
                    break
                else:
                    print("Opção inválida...\n")
            if conf == "y":
                paulo += 1
            print("\nVoto concluído!\n")
        case 2:
            print("Votando em Finâncio Polvo...")
            time.sleep(0.5)
            while True:
                print("------- Confirmar voto? (y/n)")
                conf = input().lower()
                if conf == "y" or conf == "n":
                    break
                else:
                    print("Opção inválida...\n")
            if conf == "y":
                polvo += 1
            print("\nVoto concluído!\n")
        case 3:
            print("Votando em Gusto Cuty Cuty...")
            time.sleep(0.5)
            while True:
                print("------- Confirmar voto? (y/n)")
                conf = input().lower()
                if conf == "y" or conf == "n":
                    break
                else:
                    print("Opção inválida...\n")
            if conf == "y":
                gusto += 1
            print("\nVoto concluído!\n")
        case 4:
            print("Votando em Márcio Malonaro...")
            time.sleep(0.5)
            while True:
                print("------- Confirmar voto? (y/n)")
                conf = input().lower()
                if conf == "y" or conf == "n":
                    break
                else:
                    print("Opção inválida...\n")
            if conf == "y":
                marcio_malonaro += 1
            print("\nVoto concluído!\n")
        case 5:
            while True:
                print("Tem certeza que deseja ANULAR seu voto? (y/n)")
                conf = input().lower()
                if conf == "y" or conf == "n":
                    break
                else:
                    print("Opção inválida...\n")
            if conf == "y":
                nulo += 1
            print("\nVoto concluído!\n")
        case 6:
            while True:
                print("Tem certeza que deseja votar em BRANCO? (y/n)")
                conf = input().lower()
                if conf == "y" or conf == "n":
                    break
                else:
                    print("Opção inválida...\n")
            if conf == "y":
                branco += 1
            print("\nVoto concluído!\n")

def urna():
    dc = 0
    while True:
        if dc == 0:
            print("+=======================+")
            print("|   - Urna de votação   |")
            print("|=======================|")
            print("|  - Opções de voto:    |")
            print("| - - - - - - - - - - - |")
            print("| 1- Paulo Matagal      |")
            print("| 2- Finâncio Polvo     |")
            print("| 3- Gusto Cuty Cuty    |")
            print("| 4- Márcio Malonaro    |")
            print("| 5- Voto Nulo ###      |")
            print("| 6- Voto em Branco ### |")
            print("| 0- Sair da votação    |")
            print("|                       |")
            print("|=======================|\n")
            dc = 1
        voto = ler_voto()