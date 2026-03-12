#7. Crear un programa que le pida al usuario nombre, edad y ciudad de residencia, realizar cálculos basados en la edad, 
# y luego mostrará la información en pantalla 
    # Pedir al usuario que ingrese su nombre
    # Pedir al usuario que ingrese su edad
    # Pedir al usuario que ingrese su ciudad de residencia
    # Calcular el año de nacimiento
    # Saludar al usuario y mostrar la información
    # Comprobar si la edad es mayor de 18 años
    # Comprobar si la edad es un múltiplo de 5.
    
import os
os.system('cls')

nombre = input("Ingrese su nombre:")
edad = int(input("Ingrese su edad:"))
residencia = input("Ingrese donde vive:")
año_nacimiento = 2026 - edad

print(f"Hola {nombre}, todo bien?. Te he investigado un poco: Tienes {edad} años, osea que naciste en {año_nacimiento}, vives en {residencia} con tus padres")

if edad < 18:
    print("Lamentablemente no tienes 18 años, osea que todavia no puedes ingresar a los boliches de mayores")
    
else:
    print("Felicitaciones, cumpliste la legalidad!")