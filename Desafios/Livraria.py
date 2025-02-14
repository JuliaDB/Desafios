# Mensagem de boas-vindas
print('Bem-vindo a Livraria de Julia Brancher')

id_global = 1
lista_livro = []


# Função para cadastar livro
def cadastrar_livro(id: int):
    print('-' * 39)
    print('-------- MENU CADASTRAR LIVRO ---------')
    print("Id do livro: " + str(id))
    nome = input("Por favor entre com o nome do livro: ")
    autor = input("Por favor entre com o autor do livro: ")
    editora = input("Por favor entre com a editora do livro: ")
    livro = {
        "id": id,
        "nome": nome,
        "autor": autor,
        "editora": editora
    }
    lista_livro.append(livro)


# Função para consultar os livros
def consultar_livro():
    while True:
        print('-' * 39)
        print('-------- MENU CONSULTAR LIVRO ---------')
        print('1 - Consultar Todos os Livros')
        print('2 - Consultar Livro por Id')
        print('3 - Consultar Livro(s) por Autor')
        print('4 - Retornar ao Menu')
        escolha_opcao = input("Escolha a opção desejada: ")

        # Consultar todos os livros
        if escolha_opcao == "1":
            print('Consultar todos os livros cadastrados')
            for livro in lista_livro:
                print("id: {}".format(livro["id"]))
                print("nome: {}".format(livro["nome"]))
                print("autor: {}".format(livro["autor"]))
                print("editora: {}\n".format(livro["editora"]))

        # Consultar livros por Id
        elif escolha_opcao == "2":
            id_cadastrado = int(input('Digite o Id do livro: '))
            for livro in lista_livro:
                if livro['id'] == id_cadastrado:
                    print("id: {}".format(livro["id"]))
                    print("nome: {}".format(livro["nome"]))
                    print("autor: {}".format(livro["autor"]))
                    print("editora: {}\n".format(livro["editora"]))

        # Consultar livros por autor
        elif escolha_opcao == "3":
            autor_desejado = input('Digite o autor do(s) livro(s): ')
            print(f"Livros do autor: {autor_desejado} ")
            for livro in lista_livro:
                if livro['autor'].lower() == autor_desejado.lower():
                    print("id: {}".format(livro["id"]))
                    print("nome: {}".format(livro["nome"]))
                    print("autor: {}".format(livro["autor"]))
                    print("editora: {}\n".format(livro["editora"]))

        elif escolha_opcao == "4":
            # Retornar ao menu principal
            break
        else:
            print("Opção inválida, tente novamente.")


# Função para remover um livro
def remover_livro():
    while True:
        print('-' * 39)
        print('-------- MENU REMOVER LIVRO ---------')
        livro_excluido = False
        deletar = int(input('Digite o Id do livro a ser removido: '))

        for livro in lista_livro:
            if livro['id'] == deletar:
                lista_livro.remove(livro)
                print('Livro removido com sucesso!')
                livro_excluido = True
                break

        if not livro_excluido:
            print("Id inválido")
        else:
            break


# Função principal (menu, opção desejada)
def main():
    global id_global

    while True:
        print('-' * 39)
        print('---------- MENU PRINCIPAL -------------')
        print('1. Cadastrar Livro')
        print('2. Consultar Livro(s)')
        print('3. Remover Livro')
        print('4. Encerrar Programa')
        opcao = input('Escolha a opção desejada: ')

        if opcao == "1":
            cadastrar_livro(id_global)
            id_global += 1
        elif opcao == "2":
            consultar_livro()
        elif opcao == "3":
            remover_livro()
        elif opcao == "4":
            print('Encerrando o programa.')
            break
        else:
            print('Opção inválida, tente novamente.')


if __name__ == '__main__':
    main()
