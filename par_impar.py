def par_impar(num):
    if num %2== 0:
        return "par"
    else:
        return "impar"

continuar= True

while continuar == True:

    print("bienvenido a Par o impar")
    print("Escriba un numero y le diremos si es par o impar")
    numero= int(input("Escriba el numero: "))
    result= par_impar(numero)

    print("---------------------------------------------------------")
    print(f"El numero {numero} es {result}")

    print("---------------------------------------------------------")
    print("PARA SALIR escribe 1, para seguir definiendo escribe 2")
    decision=int(input("Escribe 1 o 2: "))

    print("---------------------------------------------------------")
    if decision == 1:
        continuar= False
