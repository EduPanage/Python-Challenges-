def cleanText(frase):

    texto = frase.lower()
    caracteres = ".,!?:;\"'()[]{}-+="

    for char in caracteres:
        texto = texto.replace(char, " ")

    return texto


def contWords(frase):

    if not frase.strip():
        return {}
    palavras = cleanText(frase).split()
    contagem = {}
    
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1

    return contagem, palavras
    



