# Adalab-proyecto-da-promo-63-modulo-1-team-3

## Juegos desarrollados

## 🌍 Juego de Preguntas y Respuestas de Geografía

Este proyecto es un juego de preguntas y respuestas enfocado en geografía, donde el jugador pone a prueba sus conocimientos sobre países, capitales, continentes y elementos geográficos.

El juego está desarrollado en Python y se ejecuta dentro de un Jupyter Notebook, mostrando la interacción directamente en la consola del notebook.

🎮 ¿Cómo funciona el juego?

- El juego muestra una pregunta de geografía
- El jugador debe escribir la respuesta cuando se le solicita
- Cada pregunta solo se responde una vez

🏆 Condiciones del juego

- ✅ El jugador gana al responder 5 preguntas correctamente
- ❌ El jugador pierde al responder 3 preguntas incorrectamente
- El juego termina automáticamente cuando se cumple alguna de estas condiciones.

🛠️ Tecnologías utilizadas

- Python 3
- Jupyter Notebook

▶️ Cómo ejecutar el juego

- Asegúrate de tener Python 3 instalado
- Abre VS Code o Jupyter Notebook
- Abre el archivo del juego (.ipynb)
- Ejecuta las celdas del notebook en orden
- Responde las preguntas escribiendo tu respuesta cuando se te solicite

🎯 Objetivo del proyecto

- Este proyecto fue creado con fines educativos, con el objetivo de practicar:
- Uso de diccionarios en Python
- Condicionales (if / else)
- Bucles (while)
- Entrada de datos por consola
- Lógica básica de juegos

🚀 Posibles mejoras futuras

- Evitar que se repitan preguntas
- Agregar niveles de dificultad

------------------------------------------------------------------------------------------------------------

# Ahorcado (2 jugadores) – Python (Jupyter Notebook)

Juego clásico del **ahorcado** hecho en **Python** dentro de un **Jupyter Notebook**.  
Está pensado para **2 jugadores**: uno escribe la palabra secreta y el otro la adivina letra por letra.

## Cómo se juega

- **Jugador 1** introduce una palabra secreta (se limpia y se pasa a minúsculas).
- **Jugador 2** intenta adivinar la palabra ingresando **una letra por turno**.
- Cada fallo suma un intento y se dibuja una parte del ahorcado.
- El juego termina cuando:
  - Jugador 2 adivina toda la palabra ✅
  - Se completa el ahorcado ❌
  - Jugador 2 escribe **`salir`** 👋

## Requisitos

- Python 3.x
- (Opcional) Jupyter Notebook / Jupyter Lab

## Ejecutar

1. Abre el notebook.
2. Ejecuta las celdas en orden.
3. Sigue las instrucciones en pantalla.

## Notas

- Solo se aceptan letras (a-z).
- Si repites una letra, el programa avisa y no cuenta como fallo.

------------------------------------------------------------------------------------------------------------
## Piedra, Papel o Tijeras

🎮 Piedra, Papel o Tijera en Python Este proyecto implementa el juego clásico Piedra, Papel o Tijera en Python, con dos modos de juego: Jugador contra el ordenador. Modo multijugador para dos personas. El juego se ejecuta en la consola y permite jugar varias rondas hasta que uno de los jugadores alcanza el número de puntos necesarios para ganar.

📌 Funcionalidades Menú interactivo para seleccionar el modo de juego. Validación de entradas del usuario. Generación aleatoria de la elección del ordenador. Marcador visible después de cada ronda. Fin automático del juego cuando un jugador alcanza 3 puntos. Uso de emojis para mejorar la experiencia visual.

🧠 Reglas del juego Piedra vence a Tijera. Tijera vence a Papel. Papel vence a Piedra. Si ambos jugadores eligen lo mismo, es empate. El ganador de cada ronda obtiene 1 punto. El primero en llegar a 3 puntos gana la partida.

⚙️ Tecnologías utilizadas Python 3 Librería estándar random Librería opcional emoji para los iconos visuales VS Code como entorno de desarrollo

👩‍💻 Conceptos de Python aplicados Funciones (def) Bucles while Condicionales if / elif / else Validación de datos con in, not in Uso de listas y tuplas Entrada de usuario con input() Control de flujo con continue y break

🚀 Posibles mejoras futuras Añadir interfaz gráfica. Guardar resultados en un archivo. Permitir cambiar el número de puntos para ganar. Añadir más modos de juego.

------------------------------------------------------------------------------------------------------------

## ✨ Tres en Raya (Tic‑Tac‑Toe) en Python

Proyecto sencillo e interactivo del clásico Tres en Raya, ideal para practicar estructuras de datos, funciones y control de flujo en Python.

🎮 Funcionalidades

- Tablero 3×3 representado con listas de listas.
- Dos modos de juego:
- 👥 Jugadora vs jugadora
- 🤖 Jugadora vs máquina
- Entrada interactiva de jugadas.
- Turno máquina inteligente
- Actualización del tablero en cada turno.
- Detección automática de victoria o empate.
- Reinicio del tablero al finalizar la partida.

🧩 Conceptos aplicados

Estructuras de datos

- Uso de listas de listas y valores "X", "O" y " ".

Funciones para conseguir:

- Mostrar tablero.
- Iniciar juego
- Pedir y validar jugadas.
- Torno máquina inteligente para intentar ganar y bloquear al jugador si se elige modo de juego contra la máquina.
- Comprobar ganadora o empate.
- Controlar el flujo principal del juego.
- Reiniciar tablero

Control de flujo

- Bucles while y for.
- Condicionales if, elif, else.
- Uso de break para finalizar la partida.

Interacción

- input() para selección de modo de juego y jugadas.
- Mensajes claros para guiar a la usuaria.

🎓 Objetivo del proyecto

Aprender Python de forma práctica combinando lógica, funciones, estructuras de datos e interacción con la usuaria mediante un juego clásico.

Gracias por leer este README
