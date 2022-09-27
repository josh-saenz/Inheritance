from unicodedata import name


class Person:
    def __init__(self, name, address, number):
        self.__name = name
        self.__address = address
        self.__number = number

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_number(self):
        return self.__number
    
    def print_person(self):
        print('Name: ', self.__name )
        print('Address: ', self.__address)
        print('Telephone Number: ', self.__number)

class Customer(Person):
    def __init__(self, name, address, number, customernumber, mail):
        Person.__init__(self, name, address, number)
        self.__customernumber = customernumber
        self.__mail = mail
    
    def print_person(self):
        print('Name: ', Person.get_name(self) )
        print('Address: ', Person.get_address(self))
        print('Telephone Number: ', Person.get_number(self))

        Person.print_person(self)
        print('Customer Number: ', self.__customernumber)
        if self.__mail:
            print('On Mailing List: YES')
        else:
            print('On Mailing List: NO')



