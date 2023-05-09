# Importando el módulo random en Python, que proporciona acceso a funciones para
# generar números aleatorios y seleccionar elementos aleatorios de listas.
import random
# Importando el módulo de math, el cual proporciona acceso a funciones matemáticas
# y constantes en Python.
import math
# Importando el módulo pyplot de la biblioteca matplotlib y dándole el alias plt.
# Esto permite que el programa use el módulo pyplot para crear y mostrar gráficas.
import matplotlib.pyplot as plt

# La clase contiene cuatro métodos para jugar piedra, papel o tijera,
# adivinar un número generado aleatoriamente, lanzar un dado y graficar
# una función seno dentro de un rango especificado.
class Opcion:
    # Permite al usuario jugar el juego de piedra, papel o tijera contra
    # la computadora.
    class PiedraPapelTijera:
        def __init__(self):
            # Inicializa una variable de instancia opciones con una lista de
            # tres cadenas: "piedra", "papel" y "tijera".
            self.opciones = ["piedra", "papel", "tijera"]

        def jugar(self):
            print("Juguemos a piedra, papel o tijera")
            # El bucle while continuará solicitando al usuario que ingrese su
            # elección hasta que ingresen una opción válida (una de las opciones
            # en la lista self.opciones). Si el usuario ingresa una opción no
            # válida, el código imprimirá un mensaje indicando que la elección
            # no es válida y solicitará al usuario que lo intente nuevamente.
            # Si el usuario ingresa una opción válida, el bucle se romperá y el
            # código continuará ejecutándose.
            while True:
                usuario = input("Elige tu jugada (piedra, papel o tijera): ")
                if usuario not in self.opciones:
                    print("Jugada inválida. Inténtalo de nuevo.")
                else:
                    break

            # Selecciona una opción aleatoria (ya sea "piedra", "papel" o "tijera")
            # de la lista de opciones almacenada en el atributo self.opciones de
            # la clase PiedraPapelTijera.
            computadora = random.choice(self.opciones)
            print(f"Computadora juega: {computadora}")

            # Determina al ganador de un juego de piedra, papel o tijera entre el
            # usuario y la computadora. Si el usuario y la computadora eligen la
            # misma opción, se imprime "Empate". Si el usuario gana (eligiendo
            # "piedra" y la computadora eligiendo "tijera", o eligiendo "papel" y
            # la computadora eligiendo "piedra", o eligiendo "tijera" y la
            # computadora eligiendo "papel"), se imprime "Ganaste!". De lo
            # contrario, si la computadora gana, se imprime "Perdiste".
            if usuario == computadora:
                print("Empate")
            elif (
                usuario == "piedra" and computadora == "tijera"
                or usuario == "papel" and computadora == "piedra"
                or usuario == "tijera" and computadora == "papel"
            ):
                print("Ganaste!")
            else:
                print("Perdiste.")

    # Permite al usuario adivinar un número generado aleatoriamente entre
    # 1 y 100, y proporciona retroalimentación sobre si la suposición es
    # demasiado alta o demasiado baja hasta que se adivina el número correcto.
    class AdivinarNumero:
        def __init__(self):
            # Inicializa una variable de instancia
            # numero con un número entero aleatorio entre 1 y 100. Esta variable se utiliza
            # en la clase AdivinarNumero para generar un número aleatorio que el usuario
            # debe adivinar.
            self.numero = random.randint(1, 100)

        def adivinar(self):
            print("Adivina el número secreto (entre 1 y 100)!")
            # Implementa el juego de adivinar un número generado aleatoriamente
            # entre 1 y 100. La variable intentos se inicializa en 0 y se incrementa en 1
            # por cada intento. Se solicita al usuario que ingrese un número y, si la entrada
            # no es un número entero válido, se imprime un mensaje de error y se solicita al
            # usuario que ingrese otro número. Si el número ingresado es mayor que el número
            # generado aleatoriamente, se imprime un mensaje indicando que el número es
            # demasiado alto. Si el número ingresado es menor que el número generado
            # aleatoriamente, se imprime un mensaje indicando que el número es demasiado bajo.
            # Si el número ingresado es igual al número generado aleatoriamente, se imprime
            # un mensaje indicando que el usuario ha ganado y se muestra el número de intentos
            # que le tomó adivinar el número.
            intentos = 0
            while True:
                intentos += 1
                while True:
                    try:
                        guess = int(input("Introduce tu adivinanza: "))
                        break
                    except ValueError:
                        print("Ingresa un número válido.")
                if guess > self.numero:
                    print("Demasiado alto, inténtalo de nuevo.")
                elif guess < self.numero:
                    print("Demasiado bajo, inténtalo de nuevo.")
                else:
                    print(f"¡Felicidades, adivinaste en {intentos} intentos!")
                    break

    # Simula el lanzamiento de un dado y devuelve un número aleatorio entre 1 y 6.
    class TirarDado:
        def __init__(self):
            # Inicializa la lista de valores posibles para el lanzamiento de un dado.
            # Crea una variable de instancia caras que contiene los números del 1 al 6,
            # que representan las caras de un dado estándar de seis lados.
            self.caras = [1, 2, 3, 4, 5, 6]

        def tirar(self):
            print("Tirando el dado...")
            # Imprime un mensaje que incluye un número elegido al azar de la lista
            # de valores posibles para el lanzamiento de un dado (1 a 6). Se utiliza
            # el formato f-string para insertar el número elegido en el mensaje.
            print(f"Obtuviste un {random.choice(self.caras)}")

    # Grafica una función seno dentro de un rango especifico.
    class GraficarFuncion:
        def __init__(self):
            # Inicializando los valores mínimos y
            # máximos para los ejes x e y del gráfico que se graficará en la clase
            # GraficarFuncion. El eje x tendrá un rango de -10 a 10, y el eje y
            # también tendrá un rango de -10 a 10.
            self.x_min = -10
            self.x_max = 10
            self.y_min = -10
            self.y_max = 10

        def graficar(self):
            print("Graficando función...")
            # Creando una lista de valores de x desde self.x_min
            # hasta self.x_max usando una comprensión de lista, y luego creando
            # una lista de valores de y correspondientes aplicando la función
            # math.sin() a cada valor de x usando otra comprensión de lista. Luego,
            # estos valores de x e y se grafican usando plt.plot(), y los límites
            # de los ejes x e y se establecen utilizando plt.axis(). El gráfico
            # resultante muestra una gráfica de la función seno dentro de los rangos
            # de x e y especificados.
            x_vals = [i for i in range(self.x_min, self.x_max)]
            y_vals = [math.sin(x) for x in x_vals]
            plt.plot(x_vals, y_vals)
            plt.axis([self.x_min, self.x_max, self.y_min, self.y_max])
            plt.show()

# La clase permite al usuario seleccionar opciones de un menú,
# incluyendo jugar piedra, papel o tijera, adivinar un número, lanzar un dado,
# graficar una función matemática o salir del programa
class Programa:
    def __init__(self):
        # Creando una variable de instancia juego de la clase Opcion. Esto
        # permite que la clase Programa acceda a los métodos de la clase Opcion
        self.juego = Opcion()

    def correr(self):
        print("¡Bienvenido al programa!")
        # Muestra un menú de opciones al usuario y le pide que seleccione una opción
        # ingresando un número correspondiente. Luego utiliza una serie de declaraciones
        # if/elif para llamar al método apropiado de la clase Opcion según la selección
        # del usuario. El bucle continuará mostrando el menú y solicitando la entrada
        # del usuario hasta que el usuario decida salir del programa seleccionando la
        # opción 5.
        while True:
            print("\nPor favor seleccione una opción:")
            print("1. Jugar a piedra, papel o tijera")
            print("2. Adivinar un número")
            print("3. Tirar un dado")
            print("4. Graficar una función matemática")
            print("5. Salir del programa")
            opcion = input("Ingrese el número correspondiente a la opción deseada: ")
            if opcion == "1":
                Opcion.PiedraPapelTijera().jugar()
            elif opcion == "2":
                Opcion.AdivinarNumero().adivinar()
            elif opcion == "3":
                Opcion.TirarDado().tirar()
            elif opcion == "4":
                Opcion.GraficarFuncion().graficar()
            elif opcion == "5":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor seleccione una opción válida.")

# Crea una instancia de la clase Programa y la asigna a la variable programa. Luego,
# llama al método correr() de la instancia de Programa.
programa = Programa()
programa.correr()