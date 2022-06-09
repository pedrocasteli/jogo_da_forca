from limparTela import limparTela
from telaInicial import telaPrincipal 

    
# ------------------------------------- PEDE INFOS DOS JOGADORES
def main():
    while True:
        limparTela()
        try:
            desafiante = input("Nome do desafiante: ")
            if (not desafiante) or (len(desafiante.replace(" ", "")) == 0):
                raise ValueError("=> Nomes em branco não são válidos!")
            competidor = input("Nome do competidor: ")
            if (not competidor) or (len(competidor.replace(" ", "")) == 0):
                raise ValueError("=> Nomes em branco não são válidos!")
            break
        except ValueError as e:
            limparTela()
            print("*** ERRO ***")
            print(e, end=" ")
            input()

# -------------------------------------- PEDE PALAVRAS E DICAS

    while True:
        limparTela()
        try:
            palavraChave  = input("Informe a palavra-chave: ")
            if (not palavraChave) or (len(palavraChave.replace(" ", "")) == 0):
                raise ValueError("=> A palavra-chave não pode ser vazia!")
            break
        except ValueError as e:
            limparTela()
            print("*** ERRO ***")
            print(e)
            input()

    while True:
            limparTela()
            dicas = []
            try:
                print("=> Palavra-chave: {}".format(palavraChave.upper()),"\n")
                for i in range(3):
                    dica = input("Informe a dica {}: ".format(i+1))
                    if (not dica) or (len(dica.replace(" ", "")) == 0):
                        raise ValueError("Todas dicas devem ter conteúdo!")
                    dicas.append(dica)
                break
            except ValueError as e:
                limparTela()
                print("*** ERRO ***")
                print(e)
                input()

    limparTela()

    erros = 0
    indiceDicas = -1
    digitadas = []
    palavraChaveAux = ""

# ------------------------------------------------------ MENU

    while True: 
        limparTela() 
        print("1 - Jogar")
        print("2 - Solicitar dica")
        print("=> Sua escolha: ", end=" ")

        op = input()
        if op == "1":
            limparTela()
            letra = input("Informe uma letra: ")
            secreto_temporario = ""
            digitadas.append(letra)
            if letra not in palavraChave:
                print("\nA letra '{}' não está na palavra.".format(letra))
                erros += 1
                print("Erros: {}".format(erros), end=" ")
                input()

            for letra in palavraChave:
                if letra in digitadas:
                    secreto_temporario += letra
                else:
                    secreto_temporario += "_ "

            if secreto_temporario == palavraChave:
                print("\n=> Ganhou =)\n")
                print("PALAVRA: {}".format(palavraChave.upper()),"\n")
                f = open("historico.txt", "a")
                f.write("PALAVRA: {} - VENCEDOR: {}, PERDEDOR: {}\n".format(palavraChave, competidor, desafiante))
                f.close()
                input()
                break    

            if erros >= 5:
                limparTela()
                print("Limite de erros atingido!")
                f = open("historico.txt", "a")
                f.write("PALAVRA: {} - VENCEDOR: {}, PERDEDOR: {}\n".format(palavraChave, desafiante, competidor))
                f.close()
                input()
                break

            limparTela()
            print("PALAVRA: {}".format(secreto_temporario.upper()), "\n")  
            input()
        elif op == "2":
            limparTela()
            if(indiceDicas < 2):
                indiceDicas += 1
                print("Dica: {}".format(dicas[indiceDicas]), "\n")
                letra = input("Informe uma letra: ")
                secreto_temporario = ""
                digitadas.append(letra)     
                if letra not in palavraChave:
                    print("\nA letra '{}' não está na palavra.".format(letra))
                    erros += 1
                    print("Erros: {}".format(erros), end=" ")
                    input()

                for letra in palavraChave:
                    if letra in digitadas:
                        secreto_temporario += letra
                    else:
                        secreto_temporario += "_ "

                if secreto_temporario == palavraChave:
                    print("\n=> Ganhou =)\n")
                    print("PALAVRA: {}".format(palavraChave.upper()),"\n")
                    f = open("historico.txt", "a")
                    f.write("PALAVRA: {} - VENCEDOR: {}, PERDEDOR: {}\n".format(palavraChave, competidor, desafiante))
                    f.close()
                    input()
                    break    

                limparTela()
                print("PALAVRA: {}".format(secreto_temporario.upper()), "\n")
                input()
            else:
                print("*** ERRO ***")
                print("Você já pediu todas as dicas disponíveis!", end=" ")
                input()
                limparTela()
        else:
            print("\nOpção inválida!")
            input()



#if __name__ == "__main__":
while telaPrincipal():
    main()