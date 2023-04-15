### Strings ###

my_string="Mi String"
my_other_string='Mi otro string'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string= "Esto es  un string \ncon salto de línea"
print(my_new_line_string)

my_tab_string= "\tEsto es  un string con\nTabulación"
print(my_tab_string)

my_scape_string= "\\tEsto es  un string con\n Escape"
print(my_scape_string)

### Formateo ###
name, surname, age = "Brais", "Moure", 35


print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))

print("Mi nombre es %s %s y mi edad es %d" %(name,surname, age))

print("Mi nombre es "+ name+ " " + surname +" y mi edad es " + str(age) )

# Inferencia de datos #
#La f es para inferir y fomatear los datos que van dentrode los parentesis(tuples)
print(f"Mi nombre es {name} {surname} y mi edad es {age}")


### Desempaquetado de caracteres ###

lenguage = "Python"
a, b,c,d,e,f = lenguage
print(a)
print(b)
print(c)
print(d)
print(e)


### División ###
language_slice = lenguage[1:3]
print("Devuelve desde elemento 1 hasta el elemento 2 de 'Python'",language_slice)

language_slice = lenguage[1:]
print("Desde el elemento 1 hasta el final: ",language_slice)

language_slice = lenguage[-2]
print("El segundo de atrás para adelante ",language_slice)

language_slice = lenguage[1:2:4]
print("Lo que devuelve [1:2:4]",language_slice)

language_slice = lenguage[0:6:2]
print("Lo que devuelve [0:6:2]",language_slice)

### Reverse ###
reversed_lenguage= lenguage[:2]
print("Lo que devuelve [:]",reversed_lenguage)

reversed_lenguage= lenguage[::]
print("Lo que devuelve [::]",reversed_lenguage)

reversed_lenguage= lenguage[::-1]
print("Devuelve el string invertido ",reversed_lenguage)


### Funciones o Métodos ###
lenguage="python"
print("Devuelve la primera letra en mayúscula",lenguage.capitalize())#Pone en mayúscula la primera letra
print(lenguage.upper())#Pone toda la palabra en mayúscula
print(lenguage.count("t"))#Count nos devuelve la cantidad de veces que se repite una letra
print(lenguage.isnumeric())#
print("1".isnumeric())#Me dice si es un número el string 
print(lenguage.lower())#Pone todas las letras en minúscula
print(lenguage.upper().isupper())#Primero la convierto en mayúscula y luego verifico si está en mayúscula

print(lenguage.lower().islower())#Primero la convierto en minúscula y luego verifico si está en minúscula

print(lenguage.startswith("P"))#Me devuelve false porque verifica que esté en minúscula o no
print(lenguage.startswith("pyt"))
print("Devuelve false porque tiene en cuenta la mayúscula: ","Py"=="py")