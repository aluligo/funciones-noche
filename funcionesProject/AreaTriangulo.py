#Ejemplo para calcular el area del triangulo

#Identificar las entradas (variables)
base = int(input("Ingrese la base del triangulo: "))
altura = int(input("Ingrese la Altura del triangulo: "))

#colocar el proceso, se hace mediante una funcion

def calcularAreaTriangulo(b,a):
    area = (b*a)/2
    #print("El area del triangulo es: ",area)
    return area
#invocar la funcion
#calcularAreaTriangulo(base,altura)
resultado = calcularAreaTriangulo(base,altura)
print("El area del triangulo es: ",resultado)

