cantidad_euro = float(input("Cuantos euros quieres convertir: "))

#Cambio a libras
def libra(cantidad_euro):
    libras_total = cantidad_euro * (87/100)
    return libras_total
#cambio a dolares
def dolar(cantidad_euro):
    dolar_total = cantidad_euro * (110/100)
    return dolar_total
dolares = dolar(cantidad_euro)
libras = libra(cantidad_euro)

print("Estos euros: ", cantidad_euro, ",equivalen a estos doalres: ", dolares )
print("Estos euros: ", cantidad_euro, ",equivalen a estas libras: ", libras )