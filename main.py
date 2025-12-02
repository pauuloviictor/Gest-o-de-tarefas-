# main.py: script principal que usa os dois módulos acima. No módulo tarefas.py, crie uma lista para armazenar as tarefas.
# Mude para esta importação simples (assumindo que main.py e tarefas.py estão no mesmo nível)
from agenda import tarefas
import agenda.utilidades as utilidades
from agenda import tarefas, utilidades

from agenda import tarefas
from agenda import utilidades


def main():
    while True:
        utilidades.menu()

        opcao = input("Escolha uma opção: ")

        # 1 - Adicionar
        if opcao == '1':
            nome = input('Qual o nome da tarefa? ')
            tarefas.adicionar_tarefa(nome)
            print(f'Tarefa "{nome}" adicionada com sucesso!')

        # 2 - Listar
        elif opcao == '2':
            tarefas.listar_tarefas()

        # 3 - Remover
        elif opcao == '3':
            try:
                indice = int(input('Qual número tarefa deseja remover? '))
                tarefas.remover_tarefa(indice)
            except ValueError:
                print("Digite um número válido!")

        # 4 - Concluir
        elif opcao == '4':
            try:
                indice = int(input('Qual número tarefa deseja concluir? '))
                tarefas.concluir_tarefa(indice)
            except ValueError:
                print("Digite um número válido!")

        # 5 - Porcentagem concluída
        elif opcao == '5':
            resultado = utilidades.porcentagem_concluida(tarefas.lista_de_tarefas)
            print(f'Você já concluiu {resultado}% das tarefas!')

        # 6 - Sortear tarefa
        elif opcao == '6':
            resultado = utilidades.sortear_tarefa(tarefas.lista_de_tarefas)
            if resultado:
                print(f"Tarefa sorteada: {resultado['Nome']}")

        # 0 - sair
        elif opcao == '0':
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
