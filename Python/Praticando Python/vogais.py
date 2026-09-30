def countVogais():
    
    try:
        count = 0
        vogais = ['a', 'e', 'i', 'o', 'u', 'é', 'ó', 'á']
        frase = input('\nInforme um texto: ').lower()
        
        for letra in frase:
            if letra in vogais:
                count += 1    
                
        print(f'A frase possui {count} vogais!\n')
                 
    except ValueError:
        print('\nError: Não foi informada a frase!\n')

countVogais()