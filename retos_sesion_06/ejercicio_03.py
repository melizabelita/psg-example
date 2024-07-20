print("Imprime una tabla de verdad para la siguiente afirmación:")
print("Una puerta tiene dos interruptores que controlan dos luces")
print("la puerta sólo debe abrirse cuando las dos luces están apagadas")
print("o las dos están encendidas, caso contrario la puerta no se abre,")
print("¿qué operador lógico se puede utilizar?")
print()

print ("Abriendo la puerta")
print ("luz 1   ", "luz 2   ", "Abre Puerta") 
luz1 = True
luz2 = True
print (luz1, luz2, luz1 == luz2)
luz1 = True
luz2 = False
print (luz1, luz2, luz1 == luz2)
luz1 = False
luz2 = True
print (luz1, luz2, luz1 == luz2)
luz1 = False
luz2 = False
print (luz1, luz2, luz1 == luz2)

print ("Abriendo la puerta - Utilizando XNOR")
print ("luz 1   ", "luz 2   ", "Abre Puerta - XNOR") 
luz1 = True
luz2 = True
print (luz1, luz2, not((luz1 or luz2) and not (luz1 and luz2)))
luz1 = True
luz2 = False
print (luz1, luz2, not((luz1 or luz2) and not (luz1 and luz2)))
luz1 = False
luz2 = True
print (luz1, luz2, not((luz1 or luz2) and not (luz1 and luz2)))
luz1 = False
luz2 = False
print (luz1, luz2, not((luz1 or luz2) and not (luz1 and luz2)))
