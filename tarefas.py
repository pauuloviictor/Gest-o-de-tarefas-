# tarefas.py: responsável por manipular as tarefas (adicionar, listar, remover). 

#  Cada tarefa deve ser representada como um dicionário no formato: {"nome": "descrição da tarefa", "concluida": False} Ou seja, toda tarefa tem um nome e um status de conclusão (booleano: True ou False).

#  No módulo tarefas.py, implemente funções para: Adicionar tarefa → cria uma nova tarefa com "concluida": False.
 
#  Listar tarefas → exibe todas as tarefas numeradas, mostrando se estão concluídas ou não.
 
#  Remover tarefa → recebe o índice da tarefa na lista e a exclui.
 
#  Concluir tarefa → recebe o índice da tarefa e altera o campo "concluida" para True.


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
