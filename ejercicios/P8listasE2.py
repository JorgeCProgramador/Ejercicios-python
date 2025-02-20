meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
numero = int(input("Introduce un muero del 1 al 12 para mostrarte tu mes: "))

if  0<numero<= 12:
    if numero == 6:
        print(" EL MEJOR MES")
    print("Su mes es el ", meses[numero - 1])
else:
    print("Número inválido, introduce un número entre 1 y 12")