def remover_livro(lista_livros):
    while True:
        try:
            id_remover = int(input("Digite o ID do livro que deseja remover: "))
            encontrado = False
            for livro in lista_livros:
                if livro["id"] == id_remover:
                    lista_livros.remove(livro)
                    print("Livro removido com sucesso!\n")
                    encontrado = True
                    break
            if not encontrado:
                print("ID inválido. Livro não encontrado.\n")

            continuar = input("Deseja remover outro livro? (s/n): ").lower()
            if continuar != "s":
                break

        except:
            print("Entrada inválida. Digite um número válido.\n")