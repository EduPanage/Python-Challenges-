import random

def game():
    
    try:
        choice = input("\nEscolha: pedra, papel ou tesoura\n")
        options = ['pedra', 'papel', 'tesoura']  
        
        sortChoice = random.choice(options)
        
        print(f"\nComputador escolheu: {sortChoice}!")
        
        if choice == sortChoice:
            print(f"\nEmpate!\n")
        elif (choice == 'pedra' and sortChoice == 'tesoura' or
              choice == 'tesoura' and sortChoice == 'papel' or
              choice == 'papel' and sortChoice == 'pedra'):
            print(f"\nParabéns! Você venceu!\n")
        else:
            print(f"\nF...Você perdeu!\n")
        
    except ValueError:
        print("\nError: Não foi informada nenhuma opção!\n")
        
        
game()