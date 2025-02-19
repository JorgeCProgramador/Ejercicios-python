numero = int(input("Elige un numero del 1 al 10: "))

if numero == 4:
    print("¡Has ganado! El número es correcto.")
elif 1<=numero < 4:
    print("Lo siento, perdiste. El número correcto era el 4.")
elif 4 < numero <=10:
    print("Lo siento, perdiste. El número correcto era el 4.")
else:
    print("No has elegido un numero valido")