num1 = int(input("ingresa num1: "))
num2 = int(input("ingresa num2: "))

print(num1+num2)


#extra
while True:
    print("1. Resta")
    print("2. Multiplicacion")
    print("3. Division")
    print("4. Modulo")
    print("5. Sumar 3 números")
    print("6. Expresión mixta")
    print("0. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print(f"la resta es: {num1 - num2}\n")
    elif opcion == "2":
        print(f"la multiplicacion es: {num1 * num2}\n")
    elif opcion == "3":
        print(f"la division es: {num1 / num2}\n")
    elif opcion == "4":
        print(f"el modulo es: {num1 % num2}\n")
    elif opcion == "5":
        num3 = int(input("Tercer numero: "))
        print(f"la suma de los 3 numeros es: {num1 + num2 + num3}\n")
    elif opcion == "6":
        expresion = input("Expresion: ")
        print(f"el resultado de la expresion es: {eval(expresion)}\n")
    elif opcion == "0":
        break
    else:
        print("Opción no valida, intenta de nuevo.\n")