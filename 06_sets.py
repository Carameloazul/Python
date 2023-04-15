### Sets ###

my_set=set()
my_other_set= {}

print(type(my_set))#tipo <class 'set'>
print(type(my_other_set))
my_other_set = {"Brais", "Moure", 35}
print(type(my_other_set))

print(len(my_other_set))

#print(my_other_set[1])#TypeError: 'set' object is not subscriptable

my_other_set.add("MoureDev")

print(my_other_set)#Un set no es una estructura ordenada


my_other_set.add("MoureDev")#Un set no admite repetidos

print(my_other_set)

print("Moure" in my_other_set)#Para saber si un elemento existe en un sets
print("Mouri" in my_other_set)


my_other_set.remove("Moure")
print("Eliminando Moure",my_other_set)

my_other_set.clear()#La vacía
print("La variable está vací y len devuelve 0",len(my_other_set))

del my_other_set# Se carga la variable: NameError: name 'my_other_set' is not defined
#print(len(my_other_set))

my_set = {"Brais", "Moure", 35}
my_list= list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set= my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union(my_new_set))#No se une así mismo porque no se duplica los elementos en los sets
print(my_new_set.union(my_new_set).union(my_other_set).union({"Javascript", "C#"}))

print(my_new_set.difference(my_set))



