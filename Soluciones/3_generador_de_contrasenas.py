#3. **Generador de Contraseñas**: Crear contraseñas aleatorias seguras
# ### 3. Generador de Contraseñas
# **Descripción Cualitativa:**
# Debes crear un generador de contraseñas que sea útil para crear contraseñas seguras, donde el usuario pueda:
# - Especificar la longitud de la contraseña
# - Elegir qué tipos de caracteres incluir (mayúsculas, minúsculas, números, símbolos)
# - Generar múltiples contraseñas
# - Ver la fortaleza de la contraseña generada
# - Copiar la contraseña al portapapeles
# El programa debe ser una herramienta práctica para crear contraseñas seguras para diferentes servicios.

# **Conceptos a Aprender:**
# - Módulo random
# - Strings y listas
# - Bucles
# - Manipulación de caracteres

# **Implementación:**
# 1. Definir caracteres permitidos
# 2. Implementar generación aleatoria
# 3. Asegurar complejidad mínima
# 4. Permitir personalización

# **Salida Esperada:**
# ```
# Longitud de la contraseña: 12
# Contraseña generada: K9#mP2$vL5@n

### Proyecto 3: Generador de Contraseñas
# **Descripción Técnica:**
# - Introduce el módulo `random`
# - Requiere manejo de strings
# - Implementa validación de requisitos

# **Código Base:**
# ```python
# import random
# import string

# def generar_contraseña(longitud, usar_mayusculas=True, usar_numeros=True, usar_simbolos=True):
#     caracteres = string.ascii_lowercase
#     if usar_mayusculas:
#         caracteres += string.ascii_uppercase
#     if usar_numeros:
#         caracteres += string.digits
#     if usar_simbolos:
#         caracteres += string.punctuation
        
#     contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
#     return contraseña
# ```

# **Notas Técnicas:**
# - El módulo `string` proporciona constantes útiles para caracteres
# - La comprensión de lista `random.choice()` es más eficiente que un bucle
# - Considera usar un generador de números aleatorios criptográficamente seguro

# **Meora de los tips:**
# **Idea General para la Función Principal Generar()**

# Pasos clave para implementar la función:

# ***Definir conjuntos de caracteres:***
#         Crea strings para cada categoría: minúsculas, mayúsculas, números y símbolos.
#         Ejemplo: simbolos = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

# ***Construir el "alfabeto" válido:***
#         Combina solo los conjuntos de caracteres que el usuario activó (usando los parámetros min, may, sim, num).
#         Ejemplo: Si min=True y num=True, incluye minúsculas y números.

# ***Generar la contraseña base:***
#         Usa random.choice() en un bucle para seleccionar largo caracteres aleatorios del alfabeto construido.

# ***Garantizar complejidad (opcional pero recomendado):***
#         Verifica que la contraseña incluya al menos un carácter de cada tipo activado.
#         Si falta algún tipo:
#             Para cada tipo faltante, reemplaza un carácter aleatorio de la contraseña por uno de ese tipo.
#             Usa random.choice() para obtener el carácter de reemplazo.

# ***Calcular fortaleza:***
#         Criterios sugeridos:
#             Débil: Menos de 8 caracteres o solo 1 tipo de carácter.
#             Media: 8-12 caracteres con 2-3 tipos.
#             Fuerte: Más de 12 caracteres con todos los tipos activados.

# ***Retornar resultados:***
#         Devuelve la contraseña generada y su nivel de fortaleza.

# ***Sugerencias para Mejorar tu Código Actual***
# **luego de un primer planteamiento, una revision por AI determinó lo siguiente:**
#     Manejo de estados en el menú:
#         Problema: Reinicias min, may, etc. a True en cada iteración del menú interno.
#         Solución: Declara estas variables antes del while True principal e inicialízalas una sola vez.
#         _Esto es mencionado, dado que había un error de lógica al inicializar el estado de los bool que controlan que tipo de caracteres está encendido_
# ***Validación de entrada:***
#         Añade verificación para la longitud (ej. evitar valores negativos o menores a 4).
#         En el menú, valida que el usuario no desactive todos los caracteres (debe quedar al menos un tipo activo).

# ***Experiencia de usuario:***
#         Muestra un resumen de configuración antes de generar (ej: "Generando contraseña de 12 caracteres con [Min, May, Núm]").
#         Implementa la copia al portapapeles usando módulos como pyperclip (requiere instalación) o tkinter.

# ***Optimización:***
#         Evita repetir lógica similar para cada tipo de carácter (puedes usar listas/diccionarios para los menús).
#         Separa la lógica de fortaleza en una función auxiliar (ej: calcular_fortaleza(contraseña, min, may, sim, num)).

# ***Manejo de errores:***
#         Usa try-except para entradas inválidas (ej: si el usuario ingresa texto en lugar de números).
    
# **Flujo de la Función Generar() (Pseudocódigo)**
# ```python
# FUNCIÓN Generar(largo, min, may, sim, num):
#     SI min, may, sim y num son TODOS False:
#         Mostrar error "Debe seleccionar al menos un tipo de carácter"
#         Retornar None

#     # 1. Construir alfabeto
#     alfabeto = ""
#     SI min: alfabeto += minúsculas
#     SI may: alfabeto += mayúsculas
#     SI num: alfabeto += números
#     SI sim: alfabeto += símbolos

#     # 2. Generar contraseña inicial
#     contraseña = ""
#     PARA i en rango(largo):
#         contraseña += random.choice(alfabeto)

#     # 3. Forzar inclusión de tipos activos
#     lista_contraseña = list(contraseña)
#     SI min y no hay minúsculas en contraseña:
#         reemplazar un carácter aleatorio con minúscula
#     REPETIR PARA may, num, sim...

#     contraseña_segura = unir(lista_contraseña)

#     # 4. Calcular fortaleza
#     fortaleza = calcular_fortaleza(contraseña_segura, min, may, sim, num)

#     RETORNAR contraseña_segura, fortaleza

# ```
# ***Tips Finales***

#     Usa random.SystemRandom() para mayor seguridad (en lugar de random estándar).
#     Considera permitir que el usuario excluya caracteres ambiguos (ej: 1, l, O, 0).
#     ¡Implementa primero la versión básica y luego añade mejoras incrementalmente!

# Con esta estructura mantendrás el equilibrio entre aprendizaje y funcionalidad. ¡Te animo a implementarlo paso a paso!

import string
import secrets

def Generar(l,m,mm,s,n):
    diccionario =""
    # num="1234567890"
    # min="abcdefghijklmnopqrstuvxyz"
    # may="ABCDEFGHIJKLMNOPQRSTUVXYZ"
    # sim="!@#$%^&*()_+-=[]{|;:,.<>?/"
    
    if m==True:
    #     diccionario=diccionario+min
        diccionario=diccionario+string.ascii_lowercase
    if mm==True:
    #     diccionario=diccionario+may
        diccionario=diccionario+string.ascii_uppercase
    if s==True:
    #     diccionario=diccionario+sim
        diccionario=diccionario+string.digits
    if n==True:
    #     diccionario=diccionario+num
        diccionario=diccionario+string.punctuation
    
    pasw="".join(secrets.choice(diccionario) for _ in range(l))
    return pasw
  
    

    


print("Generador de contraseñas")
while True:

    largo=int(input("Indique la longitud de la contraseña "))

    print("seleccione los caracteres validos ")
    min=True
    may=True
    num=True
    sim=True
    while True:
        
        if min== True:
            print("1_ Apagar Minusculas status actual:(ON) ")
        else:
            print("1_ Encender Minusculas status actual:(OFF) ")
        
        if may== True:
            print("2_ Apagar Mayusculas status actual:(ON) ")
        else:
            print("2_ Encender Mayusculas status actual:(OFF) ")
        
        if num== True:
            print("3_ Apagar Numeros status actual:(ON) ")
        else:
            print("3_ Encender Numeros status actual:(OFF) ")
        
        if sim== True:
            print("4_ Apagar Simbolos status actual:(ON) ")
        else:
            print("4_ Encender Simbolos status actual:(OFF) ")
        
        print("5_ generar contraseña ")
        menu=int(input("seleccione una opcion "))
        if menu==1:
            if(min==True):
                min=False
            else:
                min=True
        elif menu==2:
            if(may==True):
                may=False
            else:
                may=True
        elif menu==3:
            if(num==True):
                num=False
            else:
                num=True
        elif menu==4:
            if(sim==True):
                sim=False
            else:
                sim=True
        elif menu==5:
            break
        else:
            print(" Opcion no valida ")

    pasw=Generar(largo,min,may,sim,num)
    print(f" la contraseña generada es {pasw} ")
    ans=input("Desea genera una nueva? y/n").lower()
    if ans != "y":
        break
    

            