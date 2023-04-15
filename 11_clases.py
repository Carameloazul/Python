### Classes ###

class MyPerson:#Los nombres de las clases se escriben con CamelCase
    pass#De esta manera no le agregamos más nada a la clase

print(MyPerson)
print(MyPerson())


class Person:
    def __init__(self, name, surname) -> None:
        self.name= name
        self.surname=surname

my_person= Person("Brais","Moure")
print(my_person.name)
print(my_person.surname)

class OtherPerson:
    def __init__(self, name, surname, alias=" Sin alias") -> None:
        self.full_name= f"{name} {surname} alias"
        self.__name=name        #__name ahora es privado y no puede ser accedido directamente cuando se crea el objeto
        self.__surname=surname  #Lo mismos para __surname, con 2 guiones bajo lo hago privado

    def get_name(self):
        return self.__name   
    
    def get_surname(self):
        return self.__surname     
    
    def walk(self):
        print(f"{self.full_name} Está caminando")

my_person= OtherPerson("Brais","Moure")
print(my_person)
print(my_person.walk())

my_other_person = OtherPerson("Brais", "Moure", "MoureDev")
print(my_other_person.full_name)
my_other_person.full_name="Hector de Leon El loco de los perros"
print(my_other_person.full_name)
print(my_other_person.get_name())