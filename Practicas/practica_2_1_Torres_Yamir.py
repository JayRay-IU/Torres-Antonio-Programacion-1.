# Ejercicio: Datos Personales

# -- Test 01 --
Name= "Kim"
Age= 18
City= "Guadalajara"
print(Name, Age, City)

# -- Test 02 --
Nombre= "Yamir"
Edad= 19
Ciudad= "Guadalajara"
print(Nombre, Edad, Ciudad)

# Ejercicio: Actualizar un contador

# -- Test 01 --
counter = 0

counter = counter + 1
print(counter)

counter = counter + 1
print(counter)

counter = counter + 1
print(counter)

# -- Test 02 --
contador = 0

contador = contador + 7
print(contador)

contador = contador + 7
print(contador)

contador = contador + 7
print(contador)

# Ejercicio: Constante de conversión

# -- Test 01 --
INCHES_TO_CM = 2.54

Inches = 67

centimeters = Inches * INCHES_TO_CM
print(centimeters)

# -- Test 02 -- 
PULGADAS_A_CM = 2.54

Pulgadas = 76 

Centimetros = Pulgadas * PULGADAS_A_CM
print(Centimetros)

#Ejercicio :Área de un rectángulo

# -- Test 01 --

Base = 6

Height = 7

Area = Base * Height
print("The area is", Area)

# -- Test 02 --

Base = 45

Altura = 32

Área = Base * Altura
print("El área es", Área)

#Ejercicio :Total con IVA

# -- Test 01 --
VAT = 0.16

Price = 636

Total = Price + (Price * VAT)
print("The total amount due is:", Total)
# -- Test 02 --
IVA = 0.16

Precio = 430

Total = Precio + (Precio * IVA)
print("El precio final es:", Total)

#Ejercicio :Intercambio de valores

# -- Test 01 --
A = 6
B = 7

print("before swap:")
print("A =", A, "| B =", B)

# Swap using auxiliary variable
Temp = A
A = B
B = Temp

print("After swap:")
print("A =", A, "| B =", B)

# -- Test 02 --
A = 9
B = 6

print("Antes del intercambio:")
print("A =", A, "| B =", B)

# Swap using auxiliary variable
Temp = A
A = B
B = Temp

print("Despues del intercambio:")
print("A =", A, "| B =", B)

#Ejercicio : Identificar tipos con type()

# -- Test 01 --
Age = 18
Height = 1.52
Name: "Kim"
is_student = True

print(type(Age))
print(type(Height))
print(type(Name))
print(type(is_student))

# -- Test 02 --
Edad = 19
Altura = 1.70
Nombre: "Jay"
es_estudiante = True

print(type(Edad))
print(type(Altura))
print(type(Nombre))
print(type(es_estudiante))

#Ejercicio :Convertir tipos

# -- Test 01 --
text_number = "67"

integer_converted = int(text_number)

original_number = 99

string_converted = str(original_number)

print(integer_converted, type(integer_converted))
print(string_converted, type(string_converted))

# -- Test 02 --
texto_numero = "76"

entero_convertido = int(texto_numero)

numero_original = 88

cadena_convertida = str(numero_original)

print(entero_convertido, type(entero_convertido))
print(cadena_convertida, type(cadena_convertida))

#Ejercicio :Booleanos y comparaciones

# -- Test 01 --
a = 76

b = 67

# Comparison result stored in a variable (evaluates to True)
is_greater = a > b

print(is_greater, type(is_greater))

# -- Test 02 --
a = 69

b = 96

# Resultado de la comparacion guardado en una variable (evalua a False)
es_mayor = a > b

print(es_mayor, type(es_mayor))