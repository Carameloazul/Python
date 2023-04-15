### Loops ###


# While

my_condition=0

while my_condition <20:
    print(my_condition)
    my_condition +=1
    if my_condition==15:
        print("Mi condición es 15")
        break#Rompe el bucle, lo detiene
else:#Este else pertenece al while, es opcional claro, pero se puede usar
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")


#For

my_list=[35,64,12,15,16,94,65]

for element in my_list:
    print(element)


my_tuples=(35,1.77,"Brais","Moure","Brais")

for element in my_tuples:
    print("Tuples",element)

my_other_set = {"Brais", "Moure", 35}

for element in my_other_set:
    print("Set",element)

my_other_dict = {"Nombre":"Brais", "Apellido": "Moure", "Edad":35, 1:"Python"}

for element in my_other_dict:
    print("Dict",element)

    if element =="Edad":
       print("Se ejecuta")
       # break
       #continue lo que hace es saltarse la linea de codigo del, hace un salto para el proximo elemento de for
    
else:#Pertenece al for
    print("El bucle for para el diccionario a finalizado")





