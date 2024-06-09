# Escribe un programa en Python que convierta las siguientes 
# temperaturas de grados Celsius a grados Fahrenheit:
# 30 ºC
# -273.99 ºC
# 100 ºC
# Fórmula de conversion: (0 °C × 9/5) + 32 = 32 °F

# Definiendo las variables
celsius1 = 30
celsius2 = -273.99
celsius3 = 100
f1 = 0
f2 = 0
f3 = 0

# Utilizando la fórmula de conversión para la primera temperatura celsius:
print("1. Primera Temperatura 30 grados Celsius")
f1 = (celsius1 * 9/5) + 32
print("Grados Fahrenheit")
print(f1)

print("2. Segunda Temperatura -273.99")
f2 = (celsius2 * 9/5) + 32
print("Grados Fahrenheit")
print(f2)

print("3. Tercera Temperatura 100")
f3 = (celsius3 * 9/5) + 32
print("Grados Fahrenheit")
print(f3)
