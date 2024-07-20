print("¿El cuadrado de 123 se encuentra en el siguiente rango? [N > 0 & N < 20000]")
nro1 = 123
nro2 = nro1 * nro1
print(nro1, " Cuadrado: ", nro2)
resultado = nro2 > 0 and nro2 < 20000
print(nro2, "está en el rango especificado? ", resultado)