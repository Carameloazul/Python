### Lists ###

#La lista es parecido a un array pero tiene más funcionalidades
my_list= list()

my_other_list=[]
print(my_list)
print(len(my_list))#Nos devuelve la longitud de la lista(cuantos elementos tiene)

my_list = [33,35,40,25,24,62,52,30,30,17]

print(my_list)
print(len(my_list))

my_other_list=[35, 1.77, "Brais", "Moure",35]
print(my_other_list)
print(type(my_other_list))

my_new_list = list([5])
print(my_new_list)

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])

"""
print(my_other_list[4]) Esto va a dar error porque está fuera de rango
print(my_other_list[-5]) Y esto también

"""

print(my_other_list.count(35))

edad, altura, apellido,nombre,number= my_other_list;

print(edad)
print(altura)
print(apellido)
print(nombre)

print(my_other_list + my_list) #Concatenacisón de lista

my_other_list.append("Nuevo Elemento")#Agregando un elemento al final de la lista
print(my_other_list)

my_other_list.insert(1,"rojo")
print(my_other_list)

my_other_list.remove("rojo")
print(my_other_list)

my_list.remove(30)#Elimina el primer elemento que coincide con el argumento
print(my_list)

print(my_list.pop())#El pop devuelve el número eliminado
print(my_list)#Elimina el ultimo elemento de la lista

print(my_list.pop(2))#Elimina un elemento específico de la lista
print(my_list)

del my_list[1] #Puedo eliminar un elemento específico usando la keyword "del"
print(my_list)

#my_list.insert(1, "Fuego con todo esto")
print(my_list)

my_new_list = my_list.copy() #Crea un copia poca profunda de la lista

my_list.clear()
print(my_list)
print("copia de my new list:",my_new_list)

my_new_list.reverse()#Invierte todos los elementos de la lista, muta la lista
print(my_new_list)


print(my_new_list[::-1])#No muta la lista

my_new_list.sort()#Me ordena la lista de menor a mayor
print(my_new_list)

print(my_new_list.index(30))
