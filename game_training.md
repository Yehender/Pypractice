# 10 Juegos para Practicar Python 🎮

Esta colección de juegos está diseñada para practicar diferentes conceptos de Python, desde lo más básico hasta proyectos más elaborados.

## 1. Adivina el Número 🟢
**Descripción Cualitativa:**
Debes crear un juego clásico y entretenido donde:
- La computadora piensa un número secreto
- El jugador intenta adivinarlo
- Cada intento da una pista (mayor/menor)
- Se cuenta cada intento
- Se puede jugar una y otra vez
El juego debe ser adictivo y hacer que el jugador quiera mejorar su puntuación.

**Descripción del Juego:**
Un juego clásico donde el jugador debe adivinar un número secreto generado aleatoriamente por la computadora. El juego debe:
- Generar un número aleatorio entre 1 y 100
- Dar pistas si el número es mayor o menor
- Contar los intentos del jugador
- Permitir reiniciar el juego
- Mostrar la puntuación basada en intentos

**Explicación de Conceptos Técnicos:**
1. **Variables:**
   - Almacenar el número secreto
   - Guardar el intento del jugador
   - Contar intentos
   - Ejemplo:
   ```python
   numero_secreto = random.randint(1, 100)
   intento = 0
   contador_intentos = 0
   ```

2. **Bucles:**
   - While para mantener el juego activo
   - For para mostrar historial de intentos
   - Ejemplo:
   ```python
   while intento != numero_secreto:
       intento = int(input("Ingrese un número: "))
       contador_intentos += 1
   ```

3. **Condicionales:**
   - Comparar intento con número secreto
   - Dar pistas mayor/menor
   - Ejemplo:
   ```python
   if intento > numero_secreto:
       print("El número es menor")
   elif intento < numero_secreto:
       print("El número es mayor")
   ```

4. **Random:**
   - Generar número aleatorio
   - Ejemplo:
   ```python
   import random
   numero_secreto = random.randint(1, 100)
   ```

**Interfaz de Usuario:**
- Mensaje de bienvenida y reglas
- Entrada para el número del jugador
- Pistas claras (mayor/menor)
- Contador de intentos
- Opción de reinicio
- Puntuación final

**Nivel**: Básico
**Conceptos**: Variables, bucles, condicionales, random
**Características**:
- Generar número aleatorio entre 1-100
- Dar pistas (mayor/menor)
- Contar intentos
- Opción de reiniciar
- Puntuación basada en intentos

## 2. Piedra, Papel o Tijera 🟢
**Descripción Cualitativa:**
Debes crear un juego clásico de turnos donde:
- El jugador elige su jugada
- La computadora elige al azar
- Se muestra quién ganó
- Se lleva la cuenta de victorias
- Se puede jugar al mejor de 3 o 5
El juego debe ser rápido y divertido, perfecto para jugar en cualquier momento.

**Descripción del Juego:**
Un juego de turnos donde el jugador compite contra la computadora. El juego debe:
- Permitir al jugador elegir su jugada
- Generar una jugada aleatoria para la computadora
- Determinar el ganador según las reglas clásicas
- Mantener un registro de victorias
- Permitir jugar múltiples rondas

**Explicación de Conceptos Técnicos:**
1. **Listas:**
   - Almacenar opciones de jugada
   - Guardar historial de partidas
   - Ejemplo:
   ```python
   opciones = ["piedra", "papel", "tijera"]
   historial = []
   ```

2. **Random:**
   - Seleccionar jugada de la computadora
   - Ejemplo:
   ```python
   jugada_computadora = random.choice(opciones)
   ```

3. **Funciones:**
   - Determinar ganador
   - Validar entrada
   - Ejemplo:
   ```python
   def determinar_ganador(jugador, computadora):
       if jugador == computadora:
           return "Empate"
       elif (jugador == "piedra" and computadora == "tijera") or \
            (jugador == "papel" and computadora == "piedra") or \
            (jugador == "tijera" and computadora == "papel"):
           return "Jugador"
       return "Computadora"
   ```

**Interfaz de Usuario:**
- Menú de selección de jugada
- Visualización de jugadas
- Resultado de cada ronda
- Puntuación acumulada
- Opción de nueva partida

**Nivel**: Básico
**Conceptos**: Listas, random, funciones
**Características**:
- Jugada del usuario vs computadora
- Validación de entrada
- Puntuación acumulada
- Mejor de 3/5 partidas
- Estadísticas de jugadas

## 3. Ahorcado 🟢
**Descripción Cualitativa:**
Debes crear un juego de palabras donde:
- Se elige una palabra al azar
- El jugador adivina letra por letra
- Se dibuja el ahorcado progresivamente
- Se muestran las letras usadas
- Se cuenta con vidas limitadas
El juego debe ser desafiante y hacer que el jugador piense en las palabras.

**Descripción del Juego:**
Un juego de palabras donde el jugador debe adivinar una palabra letra por letra. El juego debe:
- Seleccionar una palabra aleatoria de una lista
- Mostrar guiones para cada letra
- Permitir al jugador adivinar letras
- Mostrar el progreso del ahorcado
- Dar pistas sobre letras incorrectas

**Interfaz de Usuario:**
- Palabra oculta con guiones
- Dibujo ASCII del ahorcado
- Lista de letras usadas
- Contador de vidas
- Mensajes de resultado

**Nivel**: Básico-Intermedio
**Conceptos**: Strings, listas, funciones
**Características**:
- Lista de palabras predefinidas
- Mostrar progreso con guiones
- Dibujo ASCII del ahorcado
- Letras ya usadas
- Vidas restantes

## 4. Tres en Raya 🟢
**Descripción Cualitativa:**
Debes crear un juego de estrategia donde:
- Dos jugadores se turnan
- Se marca X u O en el tablero
- Se verifica si hay ganador
- Se puede jugar contra la computadora
- Se muestra el historial de partidas
El juego debe ser estratégico y hacer que el jugador piense sus movimientos.

**Descripción del Juego:**
Tres en Raya es un juego de estrategia donde dos jugadores se turnan para marcar X u O en un tablero 3x3. El objetivo es conseguir una línea recta (horizontal, vertical o diagonal) de sus marcas.

**Nivel**: Básico-Intermedio
**Conceptos**: Matrices, funciones, validación
**Características**:
- Tablero 3x3
- Turnos alternados
- Validación de movimientos
- Detección de ganador
- Opción de jugar vs computadora

## 5. Snake 🟡
**Descripción Cualitativa:**
Debes crear un juego clásico donde:
- La serpiente se mueve continuamente
- El jugador controla la dirección
- La serpiente crece al comer
- La velocidad aumenta con el tiempo
- El juego termina al chocar
El juego debe ser adictivo y desafiante, con controles suaves y responsivos.

**Descripción del Juego:**
Snake es un juego clásico donde la serpiente se mueve continuamente por el tablero. El jugador controla la dirección de la serpiente para comer manzanas y crecer. La velocidad de la serpiente aumenta con el tiempo, y el juego termina cuando la serpiente choca contra los bordes del tablero o contra su propio cuerpo.

**Nivel**: Intermedio
**Conceptos**: Pygame, bucles, colisiones
**Características**:
- Control con flechas
- Crecimiento al comer
- Puntuación
- Velocidad progresiva
- Game over al chocar

## 6. Pong 🟡
**Nivel**: Intermedio
**Conceptos**: Pygame, física básica, colisiones
**Características**:
- Dos jugadores
- Puntuación
- Rebote de pelota
- Controles personalizables
- Efectos de sonido

## 7. Tetris 🟡
**Nivel**: Intermedio
**Conceptos**: Pygame, matrices, rotaciones
**Características**:
- Piezas clásicas
- Rotación de piezas
- Puntuación por líneas
- Niveles de dificultad
- Preview de siguiente pieza

## 8. Buscaminas 🟡
**Nivel**: Intermedio
**Conceptos**: Matrices, recursividad, lógica
**Características**:
- Diferentes tamaños de tablero
- Diferentes niveles de dificultad
- Marcador de minas
- Tiempo de juego
- Mejores puntuaciones

## 9. Breakout 🟡
**Nivel**: Intermedio-Avanzado
**Conceptos**: Pygame, física, colisiones
**Características**:
- Múltiples niveles
- Power-ups
- Efectos de sonido
- Puntuación
- Vidas extra

## 10. RPG Simple 🔴
**Nivel**: Avanzado
**Conceptos**: POO, Pygame, estados
**Características**:
- Personaje jugable
- Sistema de combate
- Inventario
- NPCs
- Misiones simples
- Sistema de guardado
- Mapa con colisiones
- Enemigos básicos
- Sistema de experiencia
- Objetos coleccionables

## Consejos para Implementación
1. Comienza con la lógica básica del juego
2. Agrega características una por una
3. Prueba cada nueva funcionalidad
4. Mejora la interfaz de usuario
5. Agrega efectos de sonido y gráficos
6. Implementa sistema de puntuación
7. Agrega opciones de configuración
8. Documenta el código
9. Optimiza el rendimiento
10. Agrega características extra

## Recursos Necesarios
- Python 3.x
- Pygame (para juegos gráficos)
- Editor de código
- Imágenes y sonidos (opcional)
- Documentación de Pygame

## Notas
- Los juegos 1-4 son en consola
- Los juegos 5-10 requieren Pygame
- Cada juego puede ser expandido con más características
- Se recomienda seguir el orden de dificultad
- Personaliza los juegos según tus necesidades 