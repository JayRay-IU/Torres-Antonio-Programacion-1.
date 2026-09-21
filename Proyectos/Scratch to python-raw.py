import time

print("[Variable 'HP' oculta]")
print("[Objeto mostrado en posición x: 73, y: -26]")
time.sleep(0.21)

print("[Fondo cambiado a: fondo1]")
print("Kasane Teto: Hello, world! i am, Kasane Teto!!!")
time.sleep(2.3)

nombre = input("Kasane Teto: What's your name?\nTu respuesta: ")
print("Kasane Teto: [Pensando 'Hmm...']")
time.sleep(0.5)
print(f"Kasane Teto: Hello, {nombre}")
time.sleep(5)

edad = input("Kasane Teto: how old are you?\nTu respuesta: ")
print(f"Kasane Teto: so, you're {edad}")
time.sleep(2)

gusto_tacos = input("Kasane Teto: Do you like tacos de carnitas with a cold and fr...\nTu respuesta: ")
if gusto_tacos.strip().lower() == "yes":
    print("Kasane Teto: Oh yeeeeahhh!")
    time.sleep(7)
else:
    print("Kasane Teto: Kys.")
    time.sleep(5)
    
print("[Desplazando en 0.5 segundos a x: 0, y: 85]")
time.sleep(0.5)
time.sleep(1)
print("[Objeto escondido]")
print("[Siguiente fondo]")
time.sleep(0.2)
print("[Siguiente fondo]")
time.sleep(0.2)
print("[Siguiente fondo]")
print("[Objeto mostrado]")
print("Kasane Teto: Let's dance buddy... press space when you ready...")
time.sleep(3.5)

hp = 0
time.sleep(5)
hp = 25
print(f"[Variable 'HP' mostrada] HP actual: {hp}")

respuesta_1 = input("Kasane Teto: Am I red?\nTu respuesta: ")
if respuesta_1.strip().lower() == "yes":
    hp = 20
    print(f"¡Correcto! HP fijado a: {hp}")
else:
    print("[Reproduciendo sonido: hit hasta que termine]")
    print(f"Incorrecto. HP se mantiene en: {hp}")
    
time.sleep(1)
respuesta_2 = input("Kasane Teto: Am I better than Miku?\nTu respuesta: ")
if respuesta_2.strip().lower() == "yes":
    hp = 15
    print(f"¡Correcto! HP fijado a: {hp}")
else:
    print("[Reproduciendo sonido: hit hasta que termine]")
    print(f"Incorrecto. HP se mantiene en: {hp}")
    
time.sleep(1)
respuesta_3 = input("Kasane Teto: do you like the music?\nTu respuesta: ")
if respuesta_3.strip().lower() == "yes":
    hp = 5
    print(f"¡Correcto! HP fijado a: {hp}")
else:
    print("[Reproduciendo sonido: hit hasta que termine]")
    print(f"Incorrecto. HP se mantiene en: {hp}")
    
time.sleep(1)
respuesta_4 = input("Kasane Teto: Am I overreacting to all this?\nTu respuesta: ")
if respuesta_4.strip().lower() == "no":
    hp = 0
    print(f"¡Correcto! HP fijado a: {hp}")
else:
    print("[Reproduciendo sonido: hit hasta que termine]")
    print(f"Incorrecto. HP se mantiene en: {hp}")
    
time.sleep(1)
print("[Variable 'HP' oculta]")
time.sleep(1)
print("[Detener todos los sonidos]")
print("--- Fin del juego ---")
