# Realiza un programa que pida al usuario que ingrese un texto, Luego, el programa le va a pedir al usuario que
# también ingrese tres letras a su elección y a partir de ese momento nuestro código va a procesar esa información
# para hacer cinco tipos de análisis y devolverle al usuario la siguiente información:
from os.path import split


# Primero: ¿cuántas veces aparece cada una de las letras que eligió? Para lograr esto, te
# recomiendo almacenar esas letras en una lista y luego usar algún método propio de string
# que nos permita contar cuantas veces aparece un sub string dentro del string. Algo que
# debes tener en cuenta es que al buscar las letras pueden haber mayúsculas y minúsculas
# y esto va a afectar el resultado. Lo que deberías hacer para asegurarte de que se
# encuentren absolutamente todas las letras es pasar, tanto el texto original como las
# letras a buscar, a minúsculas.

# Segundo: le vas a decir al usuario cuántas palabras hay a lo largo de todo el texto. Y
# para lograr esta parte, recuerda que hay un método de string que permite transformarlo
# en una lista y que luego hay una función que permite averiguar el largo de una lista.

# Tercero: nos va a informar cuál es la primera letra del texto y cuál es la última. Aquí
# claramente echaremos mano de la indexación.

# Cuarto: el sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de
# las palabras. ¿Acaso hay algún método que permita invertir el orden de una lista, y otro
# que permita unir esos elementos con espacios intermedios? Piénsalo.

# Y por último: el sistema nos va a decir si la palabra “Python” se encuentra dentro del
# texto. Esta parte puede ser algo complicada de imaginársela, pero te voy a dar una pista:
# puedes usar booleanos para hacer tu averiguación y un diccionario para encontrar la
# manera de expresarle al usuario tu respuesta.

# Solo se puede usar metodos y propiedades de los strings, inexar, conjuntos de datos y boleanos.
# No se puede usar condiciones ni bucles.




def main():

    text = input("Introduce un texto: ")
    letras = input("Ahora introduce 3 letras separadas por espacios: ")
    primera, segunda, tercera = letras.split()

    # Primer ejercicio

    print(f'La letra "{primera}" que has puesto se repite {text.lower().count(primera.lower())}.')
    print(f'La letra "{segunda}" que has puesto se repite {text.lower().count(segunda.lower())}.')
    print(f'La letra "{tercera}" que has puesto se repite {text.lower().count(tercera.lower())}.')

    # Segundo ejercicio

    print(f"En el texto hay {len(text.split())} palabras.")

    # Tercer ejercicio

    print(f'El primer caracter del texto es "{text[0]}" y la ultima caracter es "{text[-1]}".')

    # Cuarto ejercicio

    print(f"Si invertimos las palabras del texto queda de la siguiente manera:\n{" ".join(text.split()[::-1])}")

    # Quinto ejercicio

    word_in_text = "python" in text.lower()

    text_word = {
        True: 'La palabra "python" se encuentra en el texto',
        False: 'La palabra "python" no se encuentra en el texto'
    }

    print(text_word[word_in_text])


if __name__ == "__main__":
    main()