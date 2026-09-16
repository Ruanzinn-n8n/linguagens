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
    candidatos = {
        "paulo": 0,
        "polvo": 0,
        "gusto": 0,
        "marcio_malonaro": 0,
        "nulo": 0,
        "branco": 0
        }
    sair = 0
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
                candidatos["paulo"] += 1
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
                candidatos["polvo"] += 1
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
                candidatos["gusto"] += 1
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
                candidatos["marcio_malonaro"] += 1
        case 5:
            while True:
                print("Tem certeza que deseja ANULAR seu voto? (y/n)")
                conf = input().lower()
                if conf == "y" or conf == "n":
                    break
                else:
                    print("Opção inválida...\n")
            if conf == "y":
                candidatos["nulo"] += 1
        case 6:
            while True:
                print("Tem certeza que deseja votar em BRANCO? (y/n)")
                conf = input().lower()
                if conf == "y" or conf == "n":
                    break
                else:
                    print("Opção inválida...\n")
            if conf == "y":
                candidatos["branco"] += 1
        case 0:
            sair = 1
    return candidatos, sair

def calculo(dic):
    total = 0
    #total de x em dic = dic[x]
    for i in dic:
        total += dic[i]

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
        resul, sair = cont_voto(voto)
        if sair == 1:
            print("Votação encerrada! Aguarde o resultado...")
            time.sleep(1)
            print("#############################")
            print("##        Resultado        ##")
            print("#############################")
            print(f"## Paulo Matagal: {resul["paulo"]}")
            print(f"## Finâncio Polvo: {resul["polvo"]}")
            print(f"## Gusto Cuty Cuty: {resul["gusto"]}")
            print(f"## Márcio Malonaro: {resul["marcio_malonaro"]}")
            print(f"## Voto Nulo: {resul["nulo"]}")
            print(f"## Voto em Branco: {resul["branco"]}")
            print(f"## % de votos nulos: ")
            print(f"## % de votos em branco:")
            print(f"## Total:")
            print(f"##### Candidato Vencedor: ")
            break
        else:
            print("\nVoto concluído!")
            print("...\n")
            time.sleep(0.5)
            print("Deseja ver as opções novamente? (y/n)")
            ver = input().lower()
            while True:
                if ver == "y" or ver == "n":
                    break
                else:
                    print("Opção inválida...\n")
            if ver == "y":
                dc = 0
            else:
                print("Próximo a votar...")