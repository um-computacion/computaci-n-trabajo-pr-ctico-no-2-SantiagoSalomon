def clean_text(texto):
    texto = texto.lower()
    
    solo_letras = ""
    for caracter in texto:
        if caracter.isalnum():
            solo_letras += caracter
    
    return solo_letras

def is_palindrome(texto):
    texto_limpio = clean_text(texto)
    return texto_limpio == texto_limpio[::-1]

if __name__ == "__main__":
    texto_usuario = input("Introducir una palabra o una frase para verificar si es un palíndromo o no: ")
    if is_palindrome(texto_usuario):
        print(f'"{texto_usuario}" es un palíndromo')
    else:
        print(f'"{texto_usuario}" no es un palíndromo')