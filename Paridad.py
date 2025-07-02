"""Dada una lista de números numeros = [1, 2, 3, 4, 5],
genera un diccionario donde las claves sean los
números y los valores sean "par" o "impar" según corresponda.
 Imprime el resultado.
Ejemplo esperado:
Entrada: numeros = [1, 2, 3, 4, 5]
Salida: {1: "impar", 2: "par", 3: "impar", 4: "par", 5: "impar"}"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

dic_nuevo = {}

for num in numeros:
    #clave = num
    if num % 2 == 0:
        clave = num
        valor = "par"
        dic_nuevo[clave] = valor
    if num % 2 == 1:
        clave = num
        valor = "impar"
        #print(num, valor)
        dic_nuevo[clave] = valor

print(dic_nuevo)



print("simplificando el codigo")

for num in numeros:
    #clave = num
    if num % 2 == 0:
        clave = num
        valor = "par"
        dic_nuevo[clave] = valor
    else:
        valor = "impar"


print(dic_nuevo)