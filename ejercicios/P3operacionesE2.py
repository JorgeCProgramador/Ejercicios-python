camiseta = 10
sudadera = 20.5
gorra = 5.5

numero_cami = int(input("Cuantas camisetas quieres: "))
numero_suda = int(input("Cuantas sudaderas quieres: "))
numero_gorra= int(input("Cuantas gorras quieres: "))

total = (camiseta * numero_cami) + (sudadera * numero_suda) + (gorra * numero_gorra)
total_iva = total * 0.21
precio_total = total + total_iva

print("El total es con iva: ", precio_total)