from string import ascii_lowercase

letras = ascii_lowercase
intentos = 0
adivinanza = ''

password = input("Ingrese la contraseña a evaluar: ")

for char in password:
    for letra in letras:
        intentos+=1
        if letra == char:
            adivinanza+=letra
            break

print(f'cantidad de intentos:{intentos}, contaseña a evaluar: {password}')