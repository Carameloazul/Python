### Conditionals ###

my_conditional = False

if my_conditional:#Esto es lo es mismo que my_conditional==True
    print("Se ejecuta la condicional del if")

print("La ejecución continúa")

my_conditional = 5*3

if my_conditional==10:
    print("Se ejecuta la condicional del segundo if")

if my_conditional>10 and my_conditional<20:
    print("Es mayor que 10 y menor que 20")
elif my_conditional==1:
    print("Es mayor que 10 y menor que 20")
else:
    print("Es menor o igual que 10 o mayor igual que 20")


    print("Es menor o igual que 10 o mayor igual que 20")
print("La ejecución continúa")

my_string="Tiene texto"

if my_string:#No entra porque la cadena de texto vacía no es True
    print("Mi candena de texto no está vacío")

my_string=""

if not my_string:
    print("Negando la cadena de texto")