counts = [0, 0, 0, 0, 0, 0]
cedulas = [100, 50, 20, 10, 5, 2]

def showCedulas():

    print('\n')
    
    for index, cedula in enumerate(cedulas):
        
        if counts[index] > 0:
            print(f'{counts[index]} nota(s) de R$ {cedula}')
        
    print('\n')

def calcSaque(value):

    for index, cedula in enumerate(cedulas):
        
        while value >= cedula:
            counts[index] += 1
            value -= cedula
                

    showCedulas()
        

def verifSaque():
        
    try:
        saque = int(input('\nDigite o valor do saque: '))
        
        if saque <= 0:
            print('\nError: Valor igual a zero!\n')
        
        elif saque % 2 == 0:
            calcSaque(saque)
            
        else:
            print('\nError: Valor deve ser par!\n')
    
    except ValueError:
        print(f'\nError: Valor de Saque inválido!\n')

verifSaque()