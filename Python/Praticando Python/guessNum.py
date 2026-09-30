import random

def guessNum():
    
    count = 0
    secretNumber = random.randint(1, 100)
    
    while True:
        
        try:
            guess = int(input('\nChute um número: '))
            
            if guess == secretNumber:
                print(f'\nVocê ganhou!\nSeu chute: {guess} - Número Secreto: {secretNumber}\nTentativas: {count}\n')
                break
            elif guess < secretNumber:
                print(f'O número secreto é maior que {guess}')
            else:
                print(f'O número secreto é menor que {guess}')
                
            count += 1
        
        except ValueError:
            print(f'\nError: Entrada inválida! Informe um número!\n')
            

guessNum()
        