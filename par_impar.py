def par_impar(num):
    if num %2== 0:
        return "par"
    else:
        return "impar"
print("bienvenido a Par o impar")
print("Escriba un numero y le diremos si es par o impar")
numero= int(input("Escriba el numero: "))
result= par_impar(numero)

print(f"El numero {numero} es {result}")