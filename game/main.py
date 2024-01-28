# HACER UN CÓDIGO PARA JUGAR A PIEDRA, PAPEL TIJERA CONTRA EL Ordenador

import random
options = ["PIEDRA","PAPEL", "TIJERA"]
valid_options = ["0","1","2"]
print("SELECCIONA UNA OPCIÓN ")

for i in range(3):
  print(f"PRESIONA {i} PARA ELEGIR {options[i]} ")
#PEDIMOS AL USUARIO ESCOGER UNA OPCIÓN ESPERANDO QUE INGRESE UN NÚMERO

user = (input())
validation = user in valid_options
# """ESTE BUCLE WHILE SE AEGURA DE QUE EL PROGRAMA NO FALLE EN CASO DE QUE
# EL USUARIO INGRESE UN CARACTER NO NUMÉRICO

while validation == False:
   print("ESCOJA UNA OPCIÓN VÁLIDA")
   user=input()
   validation = user in valid_options

if user.isnumeric:
  user = int(user)

machine = random.randint(0,2)

U = "LA HUMANIDAD HA GANADO"
M = "LAS MÁQUINAS HAN GANADO"
E = "EMPATE"

print(f"LA MÁQUINA HA SELECCIONADO '{options[machine]}' ")
print(f"TU HAS SELECCIONADO '{options[user]}' " )

if options[user] == "PIEDRA" and options[machine] == "PAPEL":
  print(f"{M}")
elif options[user] == "PIEDRA" and options[machine] == "TIJERA":
  print(f"{U}")
elif options[user] == "PIEDRA" and options[machine] == "PIEDRA":
  print(f"{E}")

elif options[user] == "PAPEL" and options[machine] == "PAPEL":
  print(f"{E}")
elif options[user]== "PAPEL" and options[machine] == "TIJERA":
  print(f"{M}")
elif user == "PAPEL" and options[machine] == "PIEDRA":
  print(f"{U}")

elif options[user]== "TIJERA" and options[machine] == "PAPEL":
  print(f"{U}")
elif options[user] == "TIJERA" and options[machine] == "TIJERA":
  print(f"{E}")
elif options[user] == "TIJERA" and options[machine] == "PIEDRA":
  print(f"{M}")