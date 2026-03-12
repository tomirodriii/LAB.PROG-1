# 8.  crearemos un programa que verifica si un número ingresado por el usuario es positivo, 
# negativo o cero, y también si es un número par o impar.

numero = float(input("Ingrese un numero"))

if numero > 0:
    print(f"El numero {numero} es positivo")
else:
    print(f"El numero {numero} es negativo")

if numero == 0:
    print(f"El numero {numero} es cero")
else:
    print(f"El numero {numero} no es cero")
    
if numero % 2 == 0:
    print(f"El numero {numero} es par")     
else:
    print(f"El numero {numero} es impar")
    