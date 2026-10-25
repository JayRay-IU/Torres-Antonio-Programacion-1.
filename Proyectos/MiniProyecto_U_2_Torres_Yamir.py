# Miniproyecto: Recibo de compra de Pcnyan (Version Principiante con Precios Base)

print("😺🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾😺")
print("      BIENVENIDO A PCNYAN - SISTEMA DE COTIZACION    ")
print("😺🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾🐾😺")

# Catalogo de PcNyan!
catalogo_nombres = [
    "Procesador (CPU)", 
    "Tarjeta Grafica (GPU)", 
    "Memoria RAM", 
    "Placa Madre (Motherboard)", 
    "SSD NVMe", 
    "Fuente de Poder (PSU)", 
    "Gabinete"
]
catalogo_precios = [3500.00, 6500.00, 1200.00, 2500.00, 1400.00, 1500.00, 1100.00]

# Deposito de compras (una especie de SAVE en un videojuego)
nombres_comprados = []
cantidades_compradas = []
precios_comprados = []

print("\nCatalogo de componentes disponibles con precio base, nya:")
i = 0
while i < len(catalogo_nombres):
    print(f"{i + 1}. {catalogo_nombres[i]} - ${catalogo_precios[i]:.2f}")
    i = i + 1

print("\nRegistremos tus compras, nya!")
print("Escribe 0 (cero) en el numero de componente cuando termines.\n")

# Primer ciclo general (pdd de autor: estos mensajitos son de jose, los puso para no confundirse :3)
while True:
    # Quitamos el try-except para que luzca como código de estudiante real
    opcion = int(input("Elige el numero del componente (o 0 para terminar): "))
    
    # Condicionales
    if opcion == 0:
        break
        
    # Validacion basica
    if opcion < 1 or opcion > len(catalogo_nombres):
        print("Error: Opcion invalida, elige un numero de la lista, nya.")
        continue
        
    cantidad = int(input("Cantidad: "))
    if cantidad <= 0:
        print("Error: La cantidad debe ser mayor a 0, nya.")
        continue
        
    # Precios
    indice = opcion - 1
    nombre_producto = catalogo_nombres[indice]
    precio_base = catalogo_precios[indice]
    
    # Registro ¿creo?
    nombres_comprados.append(nombre_producto)
    cantidades_compradas.append(cantidad)
    precios_comprados.append(precio_base)
    
    print(f"Agregado: {nombre_producto} (Precio base: ${precio_base:.2f}), nya!\n")

# verificacion 001
if len(nombres_comprados) == 0:
    print("No registraste ningun componente, nya...")
else:
    subtotal_general = 0
    
    print("\n" + "=" * 55)
    print("               PCNYAN - TICKET DE COMPRA             ")
    print("=" * 55)
    print("Cant  Componente                 P.Unit     Total")
    print("-" * 55)
    
    j = 0
    while j < len(nombres_comprados):
        subtotal_producto = cantidades_compradas[j] * precios_comprados[j]
        subtotal_general = subtotal_general + subtotal_producto
        
        print(f"{cantidades_compradas[j]:<5} {nombres_comprados[j]:<26} ${precios_comprados[j]:<9.2f} ${subtotal_producto:<9.2f}")
        j = j + 1
        
    # Calculo final (si funcionas por dios...)
    iva = subtotal_general * 0.16
    total = subtotal_general + iva
    
    print("-" * 55)
    print(f"Subtotal:                                  ${subtotal_general:.2f}")
    print(f"IVA (16%):                                 ${iva:.2f}")
    print(f"TOTAL A PAGAR:                             ${total:.2f}")
    print("=" * 55)
    print("   Muchas gracias por tu compra, nya! Vuelve pronto!   ")
    print("                      ~ Nyan nyan! ~                   ")
    print("=====================================================")