# --- RETO JUEGO PAPEL, PIEDRA O TIJERA ----
# El usuario debe poder ingresar la eleccion de que con quiere jugar (piedra, papel o tijera)
# Se debe evaluar la entrada de 2 jugadores
# Utiliza las estructuras condicionales para devolver quien es el ganador


print('''*********** BIENVENIDO ***************
-----JUEGA PIEDRA, PAPEL O TIJERA ----
      ''')
jugador_1 = int(input('''Jugador 1: Escoge:
      1. Piedra
      2. Papel
      3. Tijera
>>> ''')
)

jugador_2 = int(input('''Jugador 2: Escoge:
      1. Piedra
      2. Papel
      3. Tijera
>>> ''')
)

if jugador_1 == jugador_2:
    print("Empate")
elif (jugador_1 == 1 and jugador_2 == 3) or (jugador_1 == 2 and jugador_2 == 1) or (jugador_1 == 3 and jugador_2 == 2):
    print("Jugador 1 GANA!!!")
elif (jugador_1 == 1 and jugador_2 == 2) or (jugador_1 == 2 and jugador_2 == 3) or (jugador_1 == 3 and jugador_2 == 1):
    print("Jugador 2 GANA!!!")
else:
    print("Alguien ingreso un numero incorrecto")
  