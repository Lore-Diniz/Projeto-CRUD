from crud.cadastrar import cadastrar_livro
from crud.consultar import consultar_livros
from crud.atualizar import atualizar_livro
from crud.remover import remover_livro
from crud.ver import ver_livros_disponiveis

def menu_principal():
    lista_livros = []
    id_global = 1

    while True:
        print("--------------------------------------------------")
        print("--------------- BIBLIOTECA TECH GIRLS -------------")
        print("Escolha a opção desejada:")
        print("1 - Cadastrar Livro")
        print("2 - Consultar Livro(s)")
        print("3 - Atualizar Livro")
        print("4 - Remover Livro")
        print("5 - Ver livros disponíveis")
        print("6 - Sair")
        opcao = input(">> ")

        if opcao == "1":
            id_global = cadastrar_livro(lista_livros, id_global)

        elif opcao == "2":
            consultar_livros(lista_livros)

        elif opcao == "3":
            atualizar_livro(lista_livros)

        elif opcao == "4":
            remover_livro(lista_livros)

        elif opcao == "5":
            ver_livros_disponiveis(lista_livros)

        elif opcao == "6":
            print("Programa encerrado. Até logo!")
            break

        else:
            print("Opção inválida. Escolha de 1 a 6.\n")


if __name__ == "__main__":
    menu_principal()
