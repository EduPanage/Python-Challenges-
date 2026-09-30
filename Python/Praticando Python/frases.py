from wordFunctions import contWords

frase = input("\nInforme um frase: ")

try:
    count, palavras = contWords(frase)
    print(f"\nTotal de Palavras: {len(palavras)}")
    print(f"Total de Repetições: {count}")
    print(f"\n{palavras}\n")

except ValueError:
    print('\nError: Frase não foi digitada!\n')

