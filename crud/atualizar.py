
def atualizar_livro(lista_livros):
    while True:
        try:
            id_atualizar = int(input("Digite o ID do livro que deseja atualizar: "))
            livro = next((l for l in lista_livros if l["id"] == id_atualizar), None)

            if livro:
                print(f"Livro encontrado: {livro['titulo']} - {livro['autor']} ({livro['ano']}) [{livro['genero']}]")
                print("O que deseja atualizar?")
                print("1 - Título")
                print("2 - Autor")
                print("3 - Ano")
                print("4 - Gênero")
                opcao = input(">> ")

                if opcao == "1":
                    livro["titulo"] = input("Novo título: ")
                elif opcao == "2":
                    livro["autor"] = input("Novo autor: ")
                elif opcao == "3":
                    livro["ano"] = input("Novo ano: ")
                elif opcao == "4":
                    livro["genero"] = input("Novo gênero: ")
                else:
                    print("Opção inválida.\n")
                    continue

                print("Livro atualizado com sucesso!\n")
            else:
                print("Livro não encontrado.\n")
        except ValueError:
            print("Digite um número válido.\n")

        continuar = input("Deseja atualizar outro livro? (s/n): ").lower()
        if continuar != "s":
            break
