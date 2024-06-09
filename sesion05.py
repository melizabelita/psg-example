print ( type (1) )

# Valor 10 Entero
print (10)
print ( type (10) )

# Variable 100 Entero
variable = 100
print (variable)
print ( type (variable) )

# Variable 20 Entero
variable_2 = int (20)
print (variable_2)
print ( type (variable_2) )

# Valor 10 en base decimal
print ("Base decimal")
print (10)
# Valor 10 en binario
print ("Base binaria")
print (0b1010)
# Valor 10 en octal
print ("Base octal")
print (0o12)
# Valor 10 en hexadecimal
print ("Base hexadecimal")
print (0xa)

# Entero con 60 dígitos
variable_3 = 123456789012345678901234567890123456789012345678901234567890
print (variable_3)
print ( type (variable_3) )

# Valor 0.5 Flotante
print (0.5)
print ( type (0.5) )

# Variable 0.100546 Flotante
variable_4 = 0.100546
print (variable_4)
print ( type (variable_4) )

# Variable 1 Flotante
variable_7 = float (1)
print(variable_7)
print ( type (variable_7) )

# Precisión de 17 decimales
variable_5 = 0.9999999999999999
print(variable_5)
print ( type (variable_5) )

# Precisión de 18 decimales, por exceder el limite se redondea
variable_5_1 = 0.99999999999999999
print(variable_5_1)
print ( type (variable_5_1) )

# Verifiquemos si 0.99999999999999999=1
variable_5_2 = 0.99999999999999999
print(variable_5_2)
print(variable_5_2 == 1)
print ( type (variable_5_2) )

# Valor 2.0e-3 Flotante
variable_6 = 2.0e-3
print(variable_6)
print ( type (variable_6) )

# Operadores aritméticos
a = 10
b = 3
# Suma
print ("Suma")
print (a + b)
# Resta
print ("Resta")
print (a - b)
# Multiplicación
print ("Multiplicación")
print (a * b)
# División
print ("División")
print (a / b)
# Potencia
print ("Potencia")
print (a ** b)
# Módulo o residuo
print ("Módulo o residuo")
print (a % b)
# División entera
print ("División entera")
print (a // b)

# Un contador tiene 300 minutos y se le suman 3600 segundos, ¿Cuántas horas en total son?
contador = 300
contador = contador + 3600/60
horas = contador // 60
print ("el resultado en horas")
print (horas)

# Operaciones más complejas - Solucion
minutos = 300
tiempo_extra_segundos = 3600
horas = (minutos + tiempo_extra_segundos / 60) / 60
print ("solucion")
print (horas)

print ("Operadores de comparación")
comparar = 10
print (comparar < 10)
print (comparar > 10)
print (comparar == 10)
print (comparar <= 10)
print (comparar >= 10)
print (comparar != 10)

print ("Número par o impar")

numero_1 = 10
numero_2 = 5
print ((numero_1 % 2) == 0)
print ((numero_1 % 2) == 1)