lista_de_tarefas = []

def adicionar_tarefa(nome):
    lista_de_tarefas.append({'Nome': nome, 'Concluída': False})

def listar_tarefas():
    for i, tarefa in enumerate(lista_de_tarefas):
        print(f"{i} - {tarefa['Nome']} (Concluída: {tarefa['Concluída']})")

def remover_tarefa(indice):
    print(f'{indice} Tarefa foi removido com sucesso.')
    if 0 <= indice < len(lista_de_tarefas):
        lista_de_tarefas.pop(indice)
    

def concluir_tarefa(indice):
    if 0 <= indice < len(lista_de_tarefas):
        lista_de_tarefas[indice]['Concluída'] = True
    else:
        print('Índice Inválido')
