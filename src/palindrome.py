def is_palindrome(texto):
    texto = texto.lower()
    texto = texto.replace(" ", "")
    return texto == texto[::-1]
