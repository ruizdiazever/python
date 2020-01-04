# 1) Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:
#       Mostrar una suma de los dos números
#       Mostrar una resta de los dos números (el primero menos el segundo)
#       Mostrar una multiplicación de los dos números
#       En caso de no introducir una opción válida, el programa informará de que no es correcta.

num_1 = float(input("1. Introduzca un numero: "))
num_2 = float(input("2. Introduzca un numero: "))

option = int(input("""Introduzca una opcion:
1. Suma.
2. Resta
3. Multiplicacion.
Ingrese: """))

if option == 1:
    print("Suma: ",num_1+num_2)
elif option == 2:
    print("Resta: ",num_1-num_2)
elif option == 3:
    print("Multiplicacion: ",num_1*num_2)
else:
    print("Opcion invalida, ingrese nuevamente.")


# 2) Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, 
# debe repetise el proceso hasta que lo introduzca correctamente.

impar = int(input("Ingrese un numero impar: "))
while impar % 2 == 0:
    print("Numero par, introduzca nuevamente.")
    impar = int(input("Ingrese un numero impar: "))
else:
    print("Numero impar ingresado correctamente.")