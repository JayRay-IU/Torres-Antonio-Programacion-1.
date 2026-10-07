# --- Ejercicio: ¿Es par o impar? --- 01

# -- Test #01 --
numero = 95
es_par = (numero % 2 == 0)
print("El numero", numero, "¿es par?", es_par)

# -- Test #02 --

numero = 66
es_par = (numero % 2 == 0)
print("El numero", numero, "¿es par?", es_par)

# --- Ejercicio concatenar vs sumar -- 02

# -- Test #01 --
texto_A = "8"
texto_B = "9"
print("Concatenacion:", texto_A + texto_B)
print("Suma numerica:", int(texto_A) + int(texto_B))

# -- Test #02 --

texto_A = "7"
texto_B = "2"
print("Concatenacion:", texto_A + texto_B)
print("Suma numerica:", int(texto_A) + int(texto_B))

# --- Ejercicio operadores racionales --- 03

num_x = 1230
num_y = 687

num_a = 332
num_b = 4785

# -- Test #01 --

mayor_que = (num_x > num_y)
menor_que = (num_x < num_y)
es_igual = (num_x == num_y)
es_diferente = (num_x != num_y)
print("¿Es mayor?:", mayor_que)
print("¿Es menor?:", menor_que)
print("¿Es igual?:", es_igual)
print("¿Es diferente?:", es_diferente)

# -- Test #02 --

mayor_que = (num_a > num_b)
menor_que = (num_a < num_b)
es_igual = (num_a == num_b)
es_diferente = (num_a != num_b)
print("¿Es mayor?:", mayor_que)
print("¿Es menor?:", menor_que)
print("¿Es igual?:", es_igual)
print("¿Es diferente?:", es_diferente)

# --- Ejercicio operadores logicos --- 04

# -- Test #01 --

y = (num_x > num_y) and (num_x < 2000)
o = (num_x > num_y) or (num_x < 1000)
condicion_not = not (num_x == num_y)
print("Resultado AND:", y)
print("Resultado OR:", o)
print("Resultado NOT:", condicion_not)

# -- Test #02 --

y = (num_a > num_b) and (num_a < 2000)
o = (num_a > num_b) or (num_a < 1000)
condicion_not = not (num_a == num_b)
print("Resultado AND:", y)
print("Resultado OR:", o)
print("Resultado NOT:", condicion_not)


# --- Ejercicio Promedio y aprobación --- 05

# -- Test #01 --

calif_1 = 7.5
calif_2 = 6.7
calif_3 = 8.9
promedio = (calif_1 + calif_2 + calif_3) / 3
aprobado = (promedio >= 6)
print("Promedio obtenido:", promedio)
print("¿Está aprobado?:", aprobado)

# -- Test #02 -- 

calif_1 = 7.1
calif_2 = 6.0
calif_3 = 9.8
promedio = (calif_1 + calif_2 + calif_3) / 3
aprobado = (promedio >= 6)
print("Promedio obtenido:", promedio)
print("¿Está aprobado?:", aprobado)

# --- Ejercicio Validación de elegibilidad --- 06

# -- Test #01 --

edad_persona = 24
nacionalidad = "mexicana"
es_elegible = (edad_persona > 17) and (nacionalidad == "mexicana")
print("¿Es elegible?:", es_elegible)
es_elegible_or = (edad_persona > 17) or (nacionalidad == "mexicana")
print("Extra:", es_elegible_or)

# -- Test #02 --

edad_persona = 32
nacionalidad = "peruana"
es_elegible = (edad_persona > 17) and (nacionalidad == "mexicana")
print("¿Es elegible?:", es_elegible)
es_elegible_or = (edad_persona > 17) or (nacionalidad == "mexicana")
print("Extra:", es_elegible_or)

# --- Ejercicio Mini reporte de un perfil --- 07

# -- Test #01 --

nombre = "Sofia"
edad = 21
estatura = 1.50
es_estudiante = True
print("Reporte de perfil:")
print("Nombre:", nombre, "-> Tipo:", type(nombre))
print("Edad:", edad, "-> Tipo:", type(edad))
print("Estatura:", estatura, "-> Tipo:", type(estatura))
print("¿Es estudiante?:", es_estudiante, "-> Tipo:", type(es_estudiante))
mensaje_extra = nombre + " mide " + str(estatura) + " metros"
print("Extra:", mensaje_extra)

# -- Test #02 --

nombre = "Osvaldo"
edad = 20
estatura = 1.67
es_estudiante = True
print("Reporte de perfil:")
print("Nombre:", nombre, "-> Tipo:", type(nombre))
print("Edad:", edad, "-> Tipo:", type(edad))
print("Estatura:", estatura, "-> Tipo:", type(estatura))
print("¿Es estudiante?:", es_estudiante, "-> Tipo:", type(es_estudiante))
mensaje_extra = nombre + " mide " + str(estatura) + " metros"
print("Extra:", mensaje_extra)

# --- Ejercicio Operadores aritmeticos basicos --- 08

# -- Test #01 --

num_x = 1230
num_y = 687
print("Aritmética:")
print("Suma:", num_x + num_y)
print("Resta:", num_x - num_y)
print("Multiplicación:", num_y * num_y)
print("División:", num_x / num_y)

# -- Test #02 --

num_a = 332
num_b = 4785
print("Aritmética:")
print("Suma:", num_a + num_b)
print("Resta:", num_a - num_b)
print("Multiplicación:", num_a * num_b)
print("División:", num_a / num_b)

# --- Ejercicio División entera y modulo --- 09

# -- Test #01 --

print("División entera (//):", num_x // num_y)
print("Módulo o residuo (%):", num_x % num_y)

# -- Test #02 --

print("División entera (//):", num_a // num_b)
print("Módulo o residuo (%):", num_a % num_b)