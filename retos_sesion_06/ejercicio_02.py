print("Construir el operador XNOR en Python")
print()
print ("Operador XNOR")
print ("a   ", "b   ", "a XNOR b") 
a = True
b = True
print (a, b, not((a or b) and not (a and b)))
a = True
b = False
print (a, b, not((a or b) and not (a and b)))
a = False
b = True
print (a, b, not((a or b) and not (a and b)))
a = False
b = False
print (a, b, not((a or b) and not (a and b)))
