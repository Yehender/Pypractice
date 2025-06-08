#2. **Conversor de Temperatura**: Celsius a Fahrenheit y viceversa
### 2. Conversor de Temperatura
# **Descripción Cualitativa:**
# Debes crear un programa que funcione como un conversor de temperatura práctico, donde el usuario pueda:
# - Elegir entre convertir de Celsius a Fahrenheit o viceversa
# - Ingresar la temperatura a convertir
# - Ver el resultado formateado con el símbolo de grados
# - Convertir múltiples temperaturas sin reiniciar el programa
# - Ver una tabla de conversiones comunes
# El programa debe ser útil para situaciones cotidianas como verificar el clima o cocinar.

# **Conceptos a Aprender:**
# - Funciones
# - Fórmulas matemáticas
# - Redondeo de números
# - Validación de entrada

# **Implementación:**
# 1. Definir las fórmulas de conversión
# 2. Crear funciones para cada conversión
# 3. Implementar validación de entrada
# 4. Formatear la salida con decimales

# **Salida Esperada:**
# ```
# Ingrese la temperatura: 32
# Ingrese la unidad (C/F): F
# 32°F = 0°C
# ```
while True:
    print("Bienvenido al conversor de temperatura")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Tabla de conversiones")
    print("4. Salir")
    opcion = int(input("Ingrese la opcion: "))
    if opcion == 4:
        break;
    elif opcion == 1:
        temp=float(input("ingrese Celsius: "))
        f=(temp*(9/5))+32
        print(f"{temp}°C = {f}°F")
    elif opcion == 2:
        temp=float(input("ingrese Fahrenheit: "))
        c=(temp-32)*(5/9)
        print(f"{temp}°F = {c}°C")
    elif opcion == 3:
        print("Tabla de conversiones")
        print("Celsius\tFahrenheit")
        for c in range(0,101,10):
            f=(c*(9/5))+32
            print(f"{c}\t{f}")
    else:
        print("Opcion no valida")
    print("--------------------------------")
    print("desea continuar? (s/n)")
    continuar = input().lower()
    if continuar == "n":
        break;
    print("--------------------------------")