def cadastrar_livro(lista_livros, id_global):
    while True:
        print("--------------------------------------------------")
        print(f"Cadastro do Livro ID: {id_global}")
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = input("Digite o ano de publicação: ")
        genero = input("Digite o gênero do livro: ")

        livro = {
            "id": id_global,
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "genero": genero
        }

        lista_livros.append(livro)
        print(" Livro cadastrado com sucesso!\n")
        id_global += 1

        continuar = input("Deseja cadastrar outro livro? (s/n): ").lower()
        if continuar != "s":
            break

    return id_global
