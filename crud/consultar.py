def consultar_livros(lista_livros):
    while True:
        print("--------------------------------------------------")
        print("---------------CONSULTA DE LIVROS-------------------")
        print("1 - Consultar todos os livros")
        print("2 - Consultar livro por ID")
        print("3 - Consultar livro(s) por autor")
        print("4 - Voltar ao menu principal")
        opcao = input(">> ")

        if opcao == "1":
            if lista_livros:
                for livro in lista_livros:
                    print(f"{livro['id']} - {livro['titulo']} - {livro['autor']} ({livro['ano']}) [{livro['genero']}]")
            else:
                print("Nenhum livro cadastrado.\n")

        elif opcao == "2":
            try:
                id_busca = int(input("Digite o ID do livro: "))
                encontrado = False
                for livro in lista_livros:
                    if livro["id"] == id_busca:
                        print(f"{livro['id']} - {livro['titulo']} - {livro['autor']} ({livro['ano']}) [{livro['genero']}]")
                        encontrado = True
                        break
                if not encontrado:
                    print("Livro não encontrado.\n")
            except ValueError:
                print("Digite um número válido.\n")

        elif opcao == "3":
            autor_busca = input("Digite o nome do autor: ")
            encontrados = [l for l in lista_livros if l["autor"].lower() == autor_busca.lower()]
            if encontrados:
                for livro in encontrados:
                    print(f"{livro['id']} - {livro['titulo']} - {livro['autor']} ({livro['ano']}) [{livro['genero']}]")
            else:
                print("Nenhum livro encontrado para esse autor.\n")

        elif opcao == "4":
            break
        else:
            print("Opção inválida.\n")

        continuar = input("Deseja fazer outra consulta? (s/n): ").lower()
        if continuar != "s":
            break