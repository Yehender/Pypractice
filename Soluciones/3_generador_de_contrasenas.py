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


def Generar(l,m,mm,s,n):
    print("hola")


print("Generador de contraseñas")
while True:

    largo=int(input("Indique la longitud de la contraseña"))

    print("seleccione los caracteres validos")
    while True:
        min=True
        may=True
        num=True
        sim=True
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
        menu=int(input("seleccione una opcion"))
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
            print("Opcion no valida")

    Generar(largo,min,may,sim,num)
    
    ans=input("Desea genera una nueva? y/n").lower()
    if ans != "y":
        break
    

            