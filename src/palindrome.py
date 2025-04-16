def is_palindrome(texto):
    texto = texto.lower()
    
    solo_letras = ""
    for caracter in texto:
        if caracter.isalnum(): 
            solo_letras += caracter
    
    return solo_letras == solo_letras[::-1]

texto_usuario = input("Introducir una palabra o una frase para verificar si es un palíndromo o no: ")

if is_palindrome(texto_usuario):
    print(f'"{texto_usuario}" es un palíndromo')
else:
    print(f'"{texto_usuario}" no es un palíndromo')