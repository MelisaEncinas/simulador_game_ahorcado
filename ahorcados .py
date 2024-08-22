import random
import string

palabras = ["elefante", "programacion", "tecnologia", "universo", "astronauta", 
            "microprocesador", "inteligencia", "artificial", "computadora", 
            "automovil", "desafiante", "matematicas", "ciudad", "fantasma", 
            "biblioteca", "volcan", "espejo", "misterio", "pirata", "selva"]

def palabras_aleatorias(palabras):
    palabra = random.choice(palabras)
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    return palabra.upper()  

def game_ahorcado():
    adivinar_palabra_aleatoria = palabras_aleatorias(palabras)
    letras_por_adivinar = set(adivinar_palabra_aleatoria)
    abecedario = set(string.ascii_uppercase)
    letras_adivinadas = set()
    intentos = 6  # Número de intentos permitidos

    while len(letras_por_adivinar) > 0 and intentos > 0:
        print(f"\nLetras adivinadas: {' '.join(letras_adivinadas)}")
        print(f"Palabra: {' '.join([letra if letra in letras_adivinadas else '-' for letra in adivinar_palabra_aleatoria])}")
        print(f"Intentos restantes: {intentos}")

        usuario_letra = input("Adivine una letra: ").upper()

        if usuario_letra in abecedario - letras_adivinadas:
            letras_adivinadas.add(usuario_letra)
            if usuario_letra in letras_por_adivinar:
                letras_por_adivinar.remove(usuario_letra)
                print(f"¡Correcto! La letra '{usuario_letra}' está en la palabra.")
            else:
                intentos -= 1
                print(f"¡Incorrecto! La letra '{usuario_letra}' no está en la palabra.")
        elif usuario_letra in letras_adivinadas:
            print("Ya adivinaste esa letra. Intenta con otra.")
        else:
            print("Letra inválida. Intenta nuevamente.")

    if len(letras_por_adivinar) == 0:
        print(f"\n¡Felicidades! Has adivinado la palabra '{adivinar_palabra_aleatoria}' correctamente.")
    else:
        print(f"\nTe has quedado sin intentos. La palabra era '{adivinar_palabra_aleatoria}'.")

if __name__ == '__main__':
    game_ahorcado()
