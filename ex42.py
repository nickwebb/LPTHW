## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## class Dog is a Animal with __init__ with parameters self, and name
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## class Cat is a Animal with __init__ with parameters self, name
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has an attribute pet set equal to satan
mary.pet = satan

## frank is-a Employee withe parameters self, Frank, 120000
frank = Employee("Frank", 120000)

## frank has attribute pet set it equal to rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()