def calcGorjeta():
 
    try:
        value = float(input("\nDigite o valor da conta: R$ "))
        percent = float(input(f"\nDigite a % da gorjeta: "))
        
        gorjeta = value * (percent/100)
        total = value + gorjeta
        print(f"\nPagamento: R$ {value:.2f}\nGorjeta: R$ {gorjeta:.2f}\nTotal: R$ {total:.2f}\n")
        
    except ValueError:
        print("\nError: Valor informado é inválido!\n")

calcGorjeta()