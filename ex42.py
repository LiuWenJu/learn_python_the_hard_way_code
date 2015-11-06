## Animal is-a object (yes, sort of confusing ) look at the extra credit
class Animal(object):
    #def __init__(self, bark):
     #   self.bark = bark
    def foo(self, p):
        print "I can bark!"
## is-a
class Dog(Animal):
    def __init__(self,  name):
        #super(Dog, self).__init__(bark)
        ## has-a
        self.name = name
## is-a
class Cat(Animal):
    def __init__(self, name):
        ## has-a
        self.name = name

## Person is-a object.
class Person(object):
    def __init__(self, name):
        ## has-a
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## is-a
class Employee(Person):
    def __init__(self, name, salary):
        ## has-a
        super(Employee, self).__init__(name)
        ## has-a
        self.salary = salary

## is-a
class Fish(object):
    pass


## is-a
class Salmon(Fish):
    pass


## is-a
class Halibut(Fish):
    pass

## rover is-a dog
rover = Dog("rover")

print rover.name
rover.foo("p")
## Satan is a cat
Satan = Cat("Satan")

## Marry is person
Marry = Person("Marry")

## Marry's pet is Satan
Marry.pet = Satan

## Frank is an employee and his salary is 12000
Frank = Employee("Frank", 12000)

## Frank's pet is rover
Frank.pet = rover

##crouse is a Salmon
crouse = Salmon()

## harry is a Halibut
harry = Halibut()
