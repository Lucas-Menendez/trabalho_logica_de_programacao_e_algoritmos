# Exibe uma mensagem de boas-vindas para o usuário.
print("\nSeja bem-vindo ao sistema de gerenciamento de colaboradores de Lucas Menezes Mendes!!! 💻")

# Inicializa uma variável global para rastrear o ID dos colaboradores e uma lista vazia para armazenar os colaboradores.
id_global = 0
lista_colaboradores = []

# Define uma função para cadastrar um novo colaborador.
def cadastrar_colaborador(id):
    # Solicita informações do usuário e cria um dicionário com os dados do colaborador.
    print("\nMENU - CADASTRAR COLABORADOR")
    lista_colaboradores.append({
        "id": id,
        "nome": input("Nome do colaborador: "),
        "setor": input("Setor do colaborador: "),
        "pagamento": input("Pagamento do colaborador: ")
    })
    # Exibe uma mensagem de confirmação do cadastro.
    print(f"Colaborador com Id ({id}) cadastrado com sucesso")

# Define uma função para consultar colaboradores.
def consultar_coladorador():
    while True:
        # Exibe opções de consulta para o usuário.
        print("\nMENU - CONSULTAR COLABORADOR")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Setor")
        print("4. Retornar ao Menu")

        alvos = []  # Lista para armazenar colaboradores encontrados.
        escolha = input()  # Obtém a escolha do usuário.

        if escolha == "1":
            alvos = lista_colaboradores  # Se o usuário escolher consultar todos, todos os colaboradores são selecionados.
        elif escolha == "2":
            # Se o usuário escolher consultar por ID, solicita o ID e busca colaboradores com esse ID.
            id = int(input("Digite o Id do colaborador: "))
            for colaborador in lista_colaboradores:
                if colaborador["id"] == id:
                    alvos.append(colaborador)
        elif escolha == "3":
            # Se o usuário escolher consultar por setor, solicita o setor e busca colaboradores com esse setor.
            setor = input("Digite o Setor do colaborador: ")
            for colaborador in lista_colaboradores:
                if colaborador["setor"] == setor:
                    alvos.append(colaborador)
        elif escolha == "4":
            break  # Se o usuário escolher retornar ao menu, sai do loop.
        else:
            print("Escolha inválida, tente novamente.")
            continue

        # Exibe os colaboradores encontrados.
        for alvo in alvos:
            print("\n")
            print("-" * 10)
            print(f"Id: {alvo['id']}")
            print(f"Nome: {alvo['nome']}")
            print(f"Setor: {alvo['setor']}")
            print(f"Pagamento: {alvo['pagamento']}")

# Define uma função para remover colaboradores.
def remove_colaborador():
    resultado = []  # Lista para armazenar colaboradores após a remoção.
    global lista_colaboradores  # Permite modificar a variável global lista_colaboradores.
    
    # Solicita o ID do colaborador a ser removido
    print("\nMENU - REMOVER COLABORADOR")
    id = int(input("\nDigite o Id do colaborador a ser removido: "))

    # Itera sobre os colaboradores e copia aqueles que não têm o ID especificado para a lista resultado.
    for colaborador in lista_colaboradores:
        if colaborador["id"] != id:
            resultado.append(colaborador)

    # Atualiza a lista de colaboradores com a lista resultado.
    lista_colaboradores = resultado
    # Exibe uma mensagem de confirmação da remoção.
    print(f"O colaborador com Id ({id}) foi removido com sucesso")

# Inicia um loop principal que permite ao usuário realizar várias operações.
while True:
    # Exibe opções do menu.
    print("\nMENU - PRINCIPAL")
    print("1. Cadastrar Colaborador")
    print("2. Consultar Colaborador")
    print("3. Remover Colaborador")
    print("4. Encerrar Programa")

    escolha = input()  # Obtém a escolha do usuário.

    if escolha == "1":
        id_global = id_global + 1  # Incrementa o ID global.
        cadastrar_colaborador(id_global)  # Chama a função para cadastrar um colaborador.
    elif escolha == "2":
        consultar_coladorador()  # Chama a função para consultar colaboradores.
    elif escolha == "3":
        remove_colaborador()  # Chama a função para remover um colaborador.
    elif escolha == "4":
        # Exibe uma mensagem de encerramento e sai do loop principal.
        print("🙋‍♂️💻 Obrigado por utilizar nossa ferramenta de gerenciamento, tenha um ótimo dia. 🙋‍♂️💻")
        print("\n")
        break
    else:
        print("Opção inválida, tente novamente.")  # Exibe uma mensagem de erro se a escolha for inválida.
