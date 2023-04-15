### Exception Handling ###

number_one, number_two=5,1
number_two="1"

if type(number_two)==int: #Esto es una manera de manejar un error
    print(number_one + number_two)
else:
    print("No se cumplió")

try:
    print(number_one+number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

#Try except else
try:
    print(number_one+number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:#Else se ejecuta sino se ejecuta una exepción 
    print("La ejecución continúa correctamente")

#Try except else finally
try:
    print(number_one+number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:#Else se ejecuta sino se produce una exepción 
    #Opcional
    print("La ejecución continúa correctamente")
finally:#Se ejecuta siempre
    #Opcional
    print("La ejecución continúa")


#print(number_one+number_two)#TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Exceptions por tipo
try:
    print(number_one+number_two)
    print("No se ha producido un error")
except ValueError:#ValueError también es otro tipo de error
    print("Se ha producido un error de ValueError")    
except TypeError:#Este bloque sólo se ejecuta para los errores de tipo TypeError    
    print("Se ha producido un error de tipo TypeError")

try:
    print(number_one+number_two)
    print("No se ha producido un error")    
except ValueError as error:#La variable error va a contener la información del error
    print("Se ha producido un ValueError")
    print(error)
except Exception as exception_error:#Exception captura cualquier otro tipo de error que no se haya puesto
    print(exception_error)
    