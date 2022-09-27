import PersonClass as pc

def main():
    name = 'Josh'
    address = '1234 Main st'
    number = 123456789
    customernum = 98765432
    mail = True

    person1 = pc.Person(name, address, number)

    customer1 = pc.Customer(name, address, number, customernum, mail)

    person1.print_person()
    print()
    print()
    print()
    customer1.print_person()

main()

