def lenNum(value):

    if len(value) == 11:
        print('\nCPF válido!\n')
        
    else:
        print('\nError: CPF não possui 11 digitos!\n')

def isNum(value):
    if not value.isdigit():
        print("\nError: CPF não possui somente números!\n")
    else:
        lenNum(value)

cpf = input("\nInforme seu CPF: ")
isNum(cpf)
