### Functions ###

def my_function():
    print("Esto es una función")

my_function()


def sum_two_values(first_number:int, second_number):
    #print(first_number + second_number)
    print(first_number + second_number)

sum_two_values(1,2)
sum_two_values(52335,432444)
sum_two_values("1","2")#Si le pasamos strings los va a concatenar
sum_two_values(2.55,6.43)

def return_sum_two_values(first_number:int, second_number):
    return first_number + second_number


var_return =return_sum_two_values(10,5)
print(var_return)

var_return =return_sum_two_values(11.6,5.12)
#var_return =return_sum_two_values(10,5)
print(var_return)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname="Moure",name= "Brais")

def print_name_with_default(name,surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Brais", "Moure")
print_name_with_default("Brais", "Moure","MoureDev")

def print_texts(*text):
    print(type(text))
    print(text)
print_texts("Hola", "Python", "MoureDev")

def print_text(*texts):
    for text in texts:
        print(text.capitalize())
        print(text.upper())

print_text("Hola", "Python", "MoureDev")
print_text("Hola")