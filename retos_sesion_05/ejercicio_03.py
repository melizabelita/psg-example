# 3. Convertir a cuantos días, horas, minutos y segundos corresponde 
# la siguiente cantidad de segundos: 288325.

# Definir el número total de segundos
total_segundos = 288325
print("Total Segundos: 288325")

# 1ro. Calculamos los dias
# 1 dia = 86400 segundos
# Utilizando división entera //

dias = total_segundos // 86400
print("Dias:")
print(dias)

# 2do. Calculamos los segundos restantes
# Utilizando módulo o residuo %
# 3600 segundos en una hora

horas_restantes = total_segundos % 86400
horas = horas_restantes // 3600  
print("Horas")
print(horas)

# 3ro. Calculamos los minutos restantes utilizando las horas restantes
# 60 segundos en un minuto

minutos_restantes = horas_restantes % 3600
minutos = minutos_restantes // 60  
print("Minutos")
print(minutos)

# 4to. Calculamos los segundos restantes
segundos_restantes = minutos_restantes % 60
print("Segundos")
print(segundos_restantes)