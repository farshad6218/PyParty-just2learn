class Person:
    count = 0
    # self hamish hast
    # self hamishe khode person hastesh
    def __init__(self , name , age):
        self.name = name
        self.age = age
        Person.count = Person.count + 1
    def get_name(self):
        print('Name is %s' % self.name)
    def get_age(self):
        print('Age is %i' % self.age)
    def get_count(self):
        return Person.count


somebody = Person('Farshad',39)
somebody.get_name()
somebody.get_age()

print('Number of object(s) = %i ' % somebody.get_count())

somebody = Person('Sahra',36)
somebody.get_name()
somebody.get_age()

print('Number of object(s) = %i ' % somebody.get_count())


class boy(Person):
    # pass is not implemented yet
    # pass
     def get_name(self):
        print('Name is %s , Son of %s' % (self.name , self.fatherName))



boy1 = boy('Ali',4)
boy1.fatherName = 'Mohsen'
boy1.get_name()