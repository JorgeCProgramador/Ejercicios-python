planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Urano", "Neptuno"]
numero = int(input("Introduce un muero del 1 al 8 para asignarte un planeta: "))

if  0<numero<= 8:
    print("Su planeta es ", planetas[numero - 1])
else:
    print("Número inválido, introduce un número entre 1 y 8")