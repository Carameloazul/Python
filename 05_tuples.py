### Tuples ###

my_tuples = tuple()
my_other_tuple = ()

my_tuples=(35,1.77,"Brais","Moure","Brais")
my_other_tuple=(30,60,30)

print(my_other_tuple)

print(my_tuples)
print(type(my_tuples))

print(my_tuples[0])
print(my_tuples[-1])
print(my_tuples[3])
#print(my_tuples[4])#IndexError, out of range 
# #print(my_tuples[-6])#IndexError, out of range     

print(my_tuples.count("Brais"))
print(my_tuples.index("Moure"))

"""
my_tuples[1] = 1.80#Las tuplas son inmutables
my_tuples[5] = 1.80#TypeError: 'tuple' object does not support item assignment

"""
print(my_other_tuple+my_tuples) 

my_sum_tuple= my_other_tuple+my_tuples
print(my_sum_tuple)
print(my_sum_tuple[3:6])#Nos devuelve una parte de la tuple pero no muta o modifica la tupla

#Si quiero que una tupla se mutable tengo que crear una lista con esa tupla

my_tuple= list(my_tuples)
print(my_tuple)
my_tuple[1] = 1.80
print(my_tuple)
my_tuple[4]= "MoureDev"
my_tuple.insert(1,"Azul")
print(tuple(my_tuple))
my_tuple=tuple(my_tuple)

#del my_tuple[3]#TypeError: 'tuple' object doesn't support item deletion

del my_tuple#Elimina la variable
#print(my_tuple)#NameError: name 'my_tuple' is not defined.