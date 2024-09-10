# OOP allows users to create their own objects.
# It allows to code that is repeatable and organized.
# Class name should have uppercase as the first letter.

class Dog():
    species='Mammal'    #it is class object attribute and it is same for any instance of a class. We need not use self keyword here because it is a reference to this particular instance.
    def __init__(self,breed,name,spots):     # after passing self, you can give the attributes of the class in the def function.
        self.breed=breed
        self.name=name
        self.spots=spots    #We can expect boolean result for spots

    #The below is a method which performs Operations/Actions
    def bark(self,number):
        print("Woof! My name is {} and number is {}".format(self.name,number))  # no need to call number as self.number becoz it is not connected to a particular instance of the class.
my_dog=Dog(breed='Lab',name='Jimmy',spots=False)  # this is an instance of the Dog class
print("Type of the my_dog instance:",type(my_dog))
print("\nBreed of the Dog:",my_dog.breed)   # Attributes can be called without paranthesis (), but when we call methods we need to use ()
print("Name of the Dog:",my_dog.name)
print("Dog has spots:",my_dog.spots)
print("What type of species:",my_dog.species)
print("I am calling a method bark:")
my_dog.bark(10)

#Creating another class to get radius, circumference of a circle

print("\nAnother example of class to get parameters of Circle:\n")
class Circle():
    #class object attribute
    pi=3.14
    def __init__(self,radius=1):    # I am passing a default value to radius and we can always pass a radius while calling a class
        self.radius=radius
        self.area= radius * radius * Circle.pi   # In OOP, if you have an attribute, it doesn't necessarily have to be defined from a parameter call. Hence we have directly created self.area attribute. We can call a variable pi, using name of the class, i.e., Class.pi
    #Method
    def get_circum(self):
        return self.radius * self.pi * 2        # You can even call pi, as Class.pi
my_circle=Circle(30)
print("Value of Pi: ",my_circle.pi)
print("Value of Radius:", my_circle.radius)
print("Circumference: ",my_circle.get_circum())
print("Area of circle:",my_circle.area)

# Inheritance & Polymorphism

print("\nExample of Inheritance:")

class Animal():
    def __init__(self):
        print("Animal Created")
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print("I am eating")
class NewDog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    def who_am_i(self):
        print("I am a dog!")

myanimal=Animal()
myanimal.who_am_i()
myanimal.eat()
mydog=NewDog()
print("Calling eat function of Animal class from a Dog class:")
mydog.eat()
print("Overriding Animal class from a Dog class:")
mydog.who_am_i()

#Polymorphism

print("\nExample of Polymorphism:")
class PolyDog():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name + " Says Woof!"

class PolyCat():
    def __init__(self,name):
        self.name=name
    def speak(self):        # We are using the same name of the method in PolyDog class in this class to show polymorphism
        return self.name + " Says Meow!"

tony=PolyDog("Tony")
kitty=PolyCat("Kitty")
print(tony.speak())
print(kitty.speak())

print("\nChecking the type of pet by iterating in both the instances of diff class:\n")
for pet in [tony,kitty]:
    print(type(pet))    # Both tony & kitty share the same method name called as speak
    print(pet.speak())

print("\nAnother way of checking Polymorphism by using method:\n")
def pet_speak(pet):
    print(pet.speak())
pet_speak(tony)
pet_speak(kitty)

# Abstract class is one that never expects to be instantiated.
# You never expect to create instance of this class.
# It is commonly used with Inheritance.
# It is defined to serve only as a base class.
# One of the realtime use of Polymorphism & having these Abstract methods is to open different file types (word, excel, ppt). So you can have a method name open and create a base class for opening files and other classes can inherit it.

print("\nExample of Abstract class:")
class AbsAnimal():
    def __init__(self,name):
        self.name=name
    def speak(self):
        raise NotImplementedError("Sub class must implement this abstract method")
class AbsDog(AbsAnimal):
    def speak(self):
        return self.name+ " Says Woof!"

class AbsCat(AbsAnimal):
    def speak(self):
        return self.name+ " Says Meow!"

fido=AbsDog("Fido")
lida=AbsCat("Lida")
print(fido.speak())
print(lida.speak())







