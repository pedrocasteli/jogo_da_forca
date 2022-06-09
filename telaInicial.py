from limparTela import limparTela

def telaPrincipal():
    while True:
        limparTela()
        print("Histórico de Jogos:\n")
        try:
            f = open("historico.txt", "r")
            linhas = f.readlines()
            for item in linhas:
                print(item.rstrip())
            f.close()
        except:
            print("=> Nenhum jogo efetuado ainda...")
        
        print("\n1 - Jogar")
        print("2 - Sair")
        print("=> Sua escolha: ", end=" ")

        op = input()
        if op == "1":
            return True
        elif op == "2":
                print("\nFIM DO JOGO...")
                return False
        else:
            print("Escolha inválida!", end=" ")
            input()   
   
