#Ejemplo de Argumentos predeterminados
def my_function(country = "Colombia"):
    print("I am from "+country)

#Invocar la funcion
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

######################
#Argumentos Arbitrarios

def mostrarEstudiantes(*args):
    print("El Estudiante: "+ args[2])

mostrarEstudiantes("Emil","Tobias","Linus")

##############
#Argumentos de Palabras claves

def mostrarCarros(carro1,carro2,carro3):
    print("El carro es: "+ carro2)
mostrarCarros(carro1 = "BMW", carro3 ="Ferrari", carro2 ="Ford")

#################################
#Argumento Arbitrario **kwargs

def mostrarCliente(**kwargs):
    print("Su apellido es: "+ kwargs["apellido"])

mostrarCliente(nombre = "Tobias", apellido = "Refsnes")
