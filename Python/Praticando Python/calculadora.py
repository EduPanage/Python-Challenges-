def sum (num1, num2):
    return num1 + num2

def sub (num1, num2):
    return num1 - num2

def mult (num1, num2):
    return num1 * num2

def div (num1, num2):
    if num2 == 0:
        raise ZeroDivisionError
    else:
        return num1 / num2

def calc():

    try:
        num1 = int(input('\nPrimeiro número: '))
        num2 = int(input('\nSegundo número: '))
        insertedOp = input('\nQual será a operação? Adição(+) Subtração (-) Multiplicação (*) ou Divisão (/)?\nOperação: ')
        
        if insertedOp == '+':
            print(f'\nResultado: {sum(num1, num2)}\n')
        elif insertedOp == '-':
            print(f'\nResultado: {sub(num1, num2)}\n')
        elif insertedOp == '*':
            print(f'\nResultado: {mult(num1, num2)}\n')
        elif insertedOp == '/':
            print(f'\nResultado: {div(num1, num2):.2f}\n')
        else:
            return 'Operação inválida!'
        
    except ValueError:
        print('\nError: Valor informado é inválido!\n')
    except ZeroDivisionError:
        print('\nError: Divisão por Zero!\n')
        
calc()