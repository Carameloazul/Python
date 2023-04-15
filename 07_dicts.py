### Dictionaries ###

my_dict = dict()
my_other_dict= {}
print(type(my_dict))#<class 'dict'>
print(type(my_other_dict))

my_other_dict = {"Nombre":"Brais", "Apellido": "Moure", "Edad":35, 1:"Python"}
print(my_other_dict)

my_dict = {
    "Nombre":"Brais",
    "Apellido": "Moure",
    "Edad":35, 
    "Lenguajes":{"Python", "Swift", "Kotlin"},
    1:1.77
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Apellido"])
print(my_dict[1])

my_dict["Nombre"]="Pedro"
print(my_dict["Nombre"])

my_dict["Calle"]="MoureDev"
print(my_dict["Calle"])

del my_dict["Calle"]#Elimina la clave
print(my_dict)

print("Edad" in my_dict)
print("Edades" in my_dict)

print("Tipo que devuelve items",type(my_dict.items()))
print("Las keys del dict:",my_dict.keys())
print("Los valores del dict:",my_dict.values())
print(dict.fromkeys(("Nombre",1, "Piso")))#Me crea un nuevo diccionario con los valores en none por defecto
#print(my_dict.clear())#Vaciamos la variable

my_list=["Nombre", 1, "Piso"]
my_new_dict= dict.fromkeys(my_list)
print(my_new_dict)
my_new_dict= dict.fromkeys(my_dict,["Brais", "Moure"])#Me agrega las key de my_dict a my_new_dict
print(my_new_dict)

print(type(my_new_dict.values()))
print(list(my_new_dict))#Me crea una lista con todas las claves de primer nivel
print(tuple(my_new_dict))
print(set(my_new_dict))