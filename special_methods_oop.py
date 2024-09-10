# Python has special methods in OOP that allow us to use some built-in operations such length and print function with our own user-created objects.

class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def __str__(self):      # This is a special method str which will return whatever we return in this method by just calling a class instance in print method
        return f"{self.title} by {self.author}"
    def __len__(self):      # This is a len method which will return whatever we return in this method by just calling a class instance in len method
        return self.pages
    def __del__(self):      # This method helps in performing an action when you delete a variable
        print("A book object has been deleted")

b=Book('Python','Jose',200)

print(b)
print(len(b))

# We can delete a variable from a memory using del keyword as below and write a del function above to person an action
del b


# Homework solution using classes

class Line:
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
    def distance(self):
        x1,y1=self.coor1        # We are unpacking the tuples, either you can do this or we can use indexing in the above method by calling self.x1=coor1[0]
        x2,y2=self.coor2
        return ((x2-x1)**2 + (y2-y1)**2) ** 0.5
    def slope(self):
        x1,y1=self.coor1
        x2,y2=self.coor2
        return (y2-y1) / (x2-x1)

c1=(3,2)
c2=(8,10)
myline=Line(c1,c2)
print("\nDistance of my line:", myline.distance())
print("Slope of my line:", myline.slope())


class Cylinder():
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
    def volume(self):
        return self.height * 3.14 * self.radius**2

    def surface_area(self):
        top=3.14 * (self.radius**2)
        return (2*top) + (2*3.14*self.radius*self.height)

mycyl=Cylinder(2,3)
print ("\nVolume of my Cylinder:",mycyl.volume())
print ("Surface area of my Cylinder:", mycyl.surface_area())


# OOP challenge question to create bank class and attributes

print("\nExample of banking transaction:")
class Account():
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,dep_amt):
        self.balance=self.balance+dep_amt
        print(f"Added {dep_amt} to the balance")
    def withdraw(self,wd_amt):
        if self.balance>=wd_amt:
            self.balance=self.balance-wd_amt
            print(f"{wd_amt} is withdrawn")    # You can print withdrawn amount and current balance in print function by writing print(f"Amount withdrawn: {wd_amt} and Current Balance: {self.balance}")
        else:
            print("No sufficient funds")
    def __str__(self):
        return f'Owner:{self.owner} \nBalance:{self.balance}'

a= Account("Sam",500)
print(a)
a.deposit(100)
print(a)
a.withdraw(600)
print(a)
a.withdraw(1)




