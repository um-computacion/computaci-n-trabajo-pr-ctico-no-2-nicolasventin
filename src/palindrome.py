def limpiar_texto(texto):
    texto = texto.lower()
    texto = texto.replace(" ", "")
    return texto

def is_palindrome(texto):
    texto_limpio = limpiar_texto(texto)
    return texto_limpio == texto_limpio[::-1]
