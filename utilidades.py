import datetime
import math
import random

def menu():
    print("=== MENU ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Concluir tarefa")
    print("5 - Mostrar porcentagem concluída")
    print("6 - Sortear tarefa")
    print("0 - Sair")

def data_atual():
    return datetime.datetime.today()

def porcentagem_concluida(lista):
    if len(lista) == 0:
        return 0

    total = len(lista)
    concluidas = sum(1 for t in lista if t["Concluída"])
    
    porcentagem = (concluidas / total) * 100
    return math.floor(porcentagem)

def sortear_tarefa(lista):
    if len(lista) == 0:
        print("Não há tarefas para sortear.")
        return None
    return random.choice(lista)

