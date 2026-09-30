def longWords():
    try:
        longas = []
        texto = input("\nInforme um texto: ")
        textoSep = texto.split()
        print(textoSep)
        
        for palavra in textoSep:
            if len(palavra) > 10:
                longas.append(palavra)
        
        print(f"\nTotal de Palavras Longas: {len(longas)}\n")
        if longas:
            print(f'{longas}\n')
                    
    except ValueError:
        print("\nError: Nenhuma frase informada!\n")
        

longWords()