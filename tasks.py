# Lista de tarefas (inicialmente vazia)
tarefas = []

# Função para adicionar uma tarefa
def adicionar_tarefa(nome_tarefa):
    tarefas.append({"tarefa": nome_tarefa, "concluida": False})
    print(f'Tarefa "{nome_tarefa}" adicionada com sucesso!')

# Função para editar uma tarefa
def editar_tarefa(indice, nova_tarefa):
    if 0 <= indice < len(tarefas):
        tarefas[indice]["tarefa"] = nova_tarefa
        print(f'Tarefa #{indice} editada para: "{nova_tarefa}"')
    else:
        print("Índice inválido. Não foi possível editar a tarefa.")

# Função para remover uma tarefa
def remover_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefa_removida = tarefas.pop(indice)
        print(f'Tarefa "{tarefa_removida["tarefa"]}" removida com sucesso!')
    else:
        print("Índice inválido. Não foi possível remover a tarefa.")

# Função para marcar uma tarefa como concluída
def concluir_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        print(f'Tarefa #{indice} marcada como concluída.')
    else:
        print("Índice inválido. Não foi possível marcar a tarefa como concluída.")

# Função para exibir a lista de tarefas
def exibir_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        print("\nLista de Tarefas:")
        for i, tarefa in enumerate(tarefas):
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f'{i}. {tarefa["tarefa"]} - {status}')
        print()

#Interação do usuário
def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1. adicionar tarefa")
        print("2. Editar tarefa")
        print("3. Remover tarefa")
        print("4. Concluir tarefa")
        print("5. Exibir tarefas")
        print("6. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            nome_tarefa = input("Digite o nome da tarefa: ")
            adicionar_tarefa(nome_tarefa)
        elif opcao == "2":
            indice = int(input("Digite o índice da tarefa a ser editada: "))
            nova_tarefa = input("Digite o novo nome da tarefa: ")
            editar_tarefa(indice, nova_tarefa)
        elif opcao == "3":
            indice = int(input("Digite o índice da tarefa a ser removida: "))
            remover_tarefa(indice)
        elif opcao == "4":
            indice = int(input("Digite o índice da tarefa a ser concluída: "))
            concluir_tarefa(indice)
        elif opcao == "5":
            exibir_tarefas()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()