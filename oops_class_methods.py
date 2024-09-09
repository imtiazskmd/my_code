# OOP allows users to create their own objects.
# It allows to code that is repeatable and organized.
# Class name should have uppercase as the first letter.

class Dog():
    def __init__(self,breed):     # after passing self, you can give the attributes of the class in the def function.
        self.breed=breed
my_dog=Dog(breed='Lab')  # this is an instance of the Dog class
print("Type of the my_dog instance:",type(my_dog))
print("\nBreed of the Dog:",my_dog.breed)


