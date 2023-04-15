"""
Variables
Por convecciones de Python no estás bien usar mayúscula en las variables
No debería comenzar con un número
Una variable puede solo sólo contener alpha-numeric characters and underscores (A-z,0-9,and _)
Los nombres de las Variables son sensible (firstname, FirstName,   FIRSTNAME) son diferentes variables
Las variables se pueden reasignar
Python no es fuertemente tipado
Pero se puede tipar: nombre_de_variable: tipo_de_datos= asignación_de_datos
"""
Myvariable ="My string variable"
print(Myvariable)

#Lo más recomendable es usar snake-case
my_variable="String de la variable"
print(my_variable)

_int_variable=5
print(_int_variable)

my_bool_variable=False
print(my_bool_variable)

#Concatenación de cadenas en un print
print(_int_variable, my_bool_variable, my_variable)
"""
Print puede llevar diferentes argumentos                                                                                               
Por detrás Python los convierte a texto
Sería algo como esto implicitamente
print(str(_int_variable), my_bool_variable, my_variable)
"""

str_int_variable=str(_int_variable)
print(type(_int_variable),type(str_int_variable),str_int_variable)
#Tipo de dato de print es 'Nonetype'
print("Este es el valor de:",my_bool_variable)
#Funciones del sistema
print(len(my_variable)) #Len nos devuelve la longitud de la cantidad de caracteres que tiene una cadena de texto

"""
Variables en una sola línea
Puedo declarar y asinar varias variables en una sola línea de cualquier tipo de datos
La desventaja que tiene es puedes agregar un valor a otra variable no querida
"""
name, surname, alias, age = "Brais", "Moure", "MoureDev", 35

print("Me llamo:",name,"", surname,"Edad:", age,"Y mi alias es:",alias)

"""
#Obtener la entrada de información de un usuario
name= input("What is your name:")
age= input("How old are you:")
print("Te llamas",name, "Que edad tienes?", age)
#Aquí le estoy reasignando los datos a las variabls name y age
"""
name= 35
age= "Brais"
#Cambiamos el tipo de datos que tenia la variable
print("Te llamas",name, "Que edad tienes?", age)
#Python es debilmente tipado, es decir, puedo cambiar el tipo de datos luego de ser asignado

#Forzando el tipo? 
address:str="Mi dirección"
address= 32
print(type(address))
address= True
print(type(address))
address= 32.7
print(type(address))
#Se puede asignar otro tipo, aunque se ponga el tipo de datos que queremos.
#Pero en los inputs tiene más sentido