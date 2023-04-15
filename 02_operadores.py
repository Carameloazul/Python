### Operadores Aritméticos###

print("La suma da:",3+4)
print("La resta da:",3-4)
print("La división es:",3/4)
print("La multiplicación da:",3*4)
print("El resto es:",10%3)
print("Floor división:",10//3)#La división acaba aproximada a un número entero
print("El exponete da:", 2**3)#** Es exponente
print("Hola" + "Python")#Concatenación con el signo más
#print("Hola" - "Pythn")#El signo menos no funciona en str(String)
#print("Hola" + 5)#str no se puede concatenar con str
print("Hola" + str(5))#Se convierte el 5 primero a string para luego concatenar o también con comillas
print(2**3+3-7/1//4) #Se puede combinar los signos que no hay ningún problema
print("Hola "*5)#Se repite 5 veces la cadena de caractereres anterior, no puede multiplcarse por un tipo float

### Operadores comparativos ###

print(3>4)
print(3<4)
print(3<=4)
print(3>=4)
print(3==4)
print(3!=4)

#Con string
print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Python")
print("Hola" <= "Python")
print("Hola" != "Python")
print("Hola" == "Python")
print("Hola"=="Hola")
print("Hola"=="aloH")
print("aaa">="abaaa")#Compara ordenación alfabetica por ASCII
print(len("aaaaa")>=len("aabca"))#Cuenta de caracteres


### Operadores comparativos logísticos ###

print(3 > 4 and "Hola" != "Python")#&& Si una sola condición no se cumple devuelve false
print(3 < 4 or "Hola" == "Python")#|| Si se cumple 1 sola condición devuelve true
print(3 < 4 and "Hola" < "Python")
print(3 > 4 or "Hola" < "Python")
print(3 > 4 or ("Hola" < "Python" and 5>10))#Evalua and antes de evaluar or

print(not (3 > 4)  )