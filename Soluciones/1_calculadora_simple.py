#1. **Calculadora Simple**: Operaciones básicas (suma, resta, multiplicación, división)

print("Bienvenido a la calculadora simple")

while True:
    #menu de operaciones
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    operation = int(input("Seleccione la operación a realizar:"))
    #condiciones ramificadas para cada operación
    if operation == 1:
        num1 = float(input("Ingrese el primer número:"))
        num2 = float(input("Ingrese el segundo número:"))
        result = num1 + num2
        print(f"El resultado de la suma es: {result}")
    elif operation == 2:
        num1 = float(input("ingrese el primer numero:"))
        num2 = float(input("ingrese el segundo numero:"))
        result = num1 - num2
        print(f"El resultado de la resta es: {result}")
    elif operation == 3:
        num1 = float(input("ingrese el primer numero:"))
        num2 = float(input("ingrese el segundo numero:"))
        result = num1 * num2
        print(f"El resultado de la multiplicacion es: {result}")
    elif operation == 4:
        num1 = float(input("ingrese el primer numero:"))
        num2 = float(input("ingrese el segundo numero:"))   
        if num2 == 0:
            print("Error: No se puede dividir por cero")
        else:
            result = num1 / num2
            print(f"El resultado de la division es: {result}")
    else:
        print("Operación no válida")
    #condicion para continuar o salir del bucle
    continuar = input("¿Desea realizar otra operación? (s/n): ")
    if continuar != "s":
        break


