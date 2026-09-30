taskList = []

def addTask(list):
    
    try:
        task = input('\nDigite a tarefa: ')
        taskList.append(task)
        print('\nTarefa Adicionada com Êxito!\n')
        return taskList
    
    except ValueError:
        print('\nError: Nenhuma tarefa informada!\n')
    
def removeTask(list):
    
    try:
        taskR = input('\nDIgite a tarefa: ')
        for task in taskList:
            if task == taskR:
                taskList.remove(task)
                print('\nTarefa Removida com Êxito!\n')
                
        return taskList    

    except ValueError:
        print('\nError: Tarafa não encontrada!\n')
        
def listList(list):
    
    index = 1
    
    if taskList:
        print('\nTarefas: \n')
        for task in taskList:
            print(f'{index}. {task}')
            index += 1

    else:
        print('\nSem tarefas cadastradas!\n')

def menu():
    
    option = 0
    
    while option != 4:
        
        print('\n1. Adicionar tarefa\n2. Visualizar tarefas\n3. Remover tarefas\n4. Sair')
        option = int(input('Escolha uma opção: '))
        
        if option == 1:
            addTask(taskList)
        elif option == 2:
            listList(taskList)
        elif option == 3:
            removeTask(taskList)
        elif option == 4:
            print('\nSistema Encerrado!\n')
            break
        else:
            print('\nError: Opção inexistente!\n')

menu()