nombre=input("Escribe un nombre: ")
fruta= input("Escribe una fruta: ")
animal=input("Escribe un animal: ")
random=input("Escribe un final random (5 palabras min): ").split()
print(random)


while len(random) <5:
    random=input("introduce un final random de mas de 5 palabras: ").split()
print(" Esta es tu hermosa historia")
random= " ".join(random)
print(f"Habia una vez un pequeño {animal} que le encantaba hablar con {nombre}, cada que iba a su casa, le daba  {fruta} para que se alimentara, ninguno se quejaba de la compañia hasta que {random}")
