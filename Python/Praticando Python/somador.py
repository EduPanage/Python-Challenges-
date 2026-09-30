def sumNums():
    try:
        num1 = int(input("\n\nPrimeiro número: "))
        num2 = int(input("Segundo número: "))
        
        sum = num1 + num2
        print(f"\nA soma dos valores é {sum}!\n")
    except ValueError:
        print("\nError: O valor informado é inválido!\n")
        
sumNums()