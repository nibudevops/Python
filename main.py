import mymodule

#-----------------------------------------------
#Sample Print
#-----------------------------------------------
print("Hello World")
print ("This is Nibu learning Python")
if 5 > 2:
    print("Five is greater than 2")
    print("Five is greater than 2 - line 2")
x=5
y="Hello All"
#this is created by Nibu for learning purpose
#print("sample code commented")
print("Samle Code commented") # this code to be commented

#----------------------
#Multi Line Commenting
#----------------------

"""
Multi line commenting
"""

print(x)
print(y)

#----------------------
#DataTypes
#----------------------

a=int(3)
b=str(3)
c=float(3)
print (a)
print (b)
print (c)
print (type(a))
print (type(b))
print (type(c))

d='3'
D='Hello'
print(d)
print(D)

#------------------------------------
#Multipe declarations
#------------------------------------

x,y,z = "apple","orange",'banana'
print(x)
print(y)
print(z)

#------------------------------------
#Concatenation with Strings only
#------------------------------------

print ('---------------------------------')
a="Nibu"
b="Augustine"

print ("My First Name is " + a + " and my last name is " + b)

#-----------------------------------------------
#Function - Global variables , Local Variables
#-----------------------------------------------

print ('---------------------------------')

x="Nibu"
def funcdemo():
    x="is good"
    print(x)
funcdemo()
print(x)


#-----------------------------------------------
#Function - Define Global variables inside functions
#-----------------------------------------------
print ('---------------------------------')

def funcdemo():
    global x
    x="inside function"
    print(x)
funcdemo()
print("outside the function trying to print x " + x)

#-----------------------------------------------------------------------------------------------
#Function - Define Global variables inside functions overriding outside declarations assignment
#-----------------------------------------------------------------------------------------------
print ('---------------------------------')

x="awesome"
def funcdemo():
    global x
    x="Superb"
funcdemo()
print("Nibu is " + x)


################################################
#### datatype
#############################################


#------------------------------------
# Datatype - list , tuple , set , dict
#------------------------------------

##list
a= ["apple","orange",'banana']
#tuple
b= ("apple","orange",'banana')
#dict
c= {"Name " : "Nibu" , "Age " : 40 }
#set
d= {"Apple", "Banana" , "Orange"}
print(type(a))
print(type(b))
print(type(c))
print(type(d))


#------------------------------------
# Datatype - int , float , complex
#------------------------------------

##int
a= 5
#float
b= 5.5
#complex
c= 1j

print(type(a))
print(type(b))
print(type(c))


#------------------------------------
# Datatype Conversion -- int , float , complex
#------------------------------------


x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#----------------------------
# String Operations - Arrays
#----------------------------

a="hello world"
print (a[2])


#----------------------------
# String Operations
#----------------------------

print("---------------------------")
# loops
a="hello world"
for i in a:
    print(i)

print("---------------------------")
####################
# lenth
####################
a="hello world"
print("Length of Hello World is " , len(a))

####################
#Check in String
####################
a="God is Love"
if "love" in a:
    print("love is present in the word")
else:
    print ("love is not present in word")
####################
#Check not in String
####################
a="God is Great"
if "great" not in a:
    print("Great is not present in the word")
else:
    print ("Great is present in the word")


####################
#Check slicing
####################
#excluding last position
a= "God is Great"
print(a[2:5])
print(a[0:5])
print(a[:5])
print(a[5:])
print(a[-4:-2])


####################
#Modify String
####################

a= " God is Great "
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("Great","Love"))


#################################
#Format String by inserting number
#################################

print("---------------------------")
age = 40
children = 2
name = "Nibu"

details = "My name is {2} and my age is {0} . I have {1} children."
print(details.format(age, children, name))

#################################
#Escape char
#################################

print('My name is \'Nibu\' and i stay in \'charlotte\'')
print('My name is \'Nibu\' \n i stay in \'charlotte\'')

#################################
# Boolean Values return function
#################################
print("---------------------------")
print(10 > 9)
print(bool("abc"))
print(10*5)

def dummyfunc():
    return False
if dummyfunc():
    print("True is returned")
else:
    print("False is returned")



#################################
# List Operations
#################################
print("---------------------------")

fruits = ["apple", "banana" , "cherry"]
print (fruits)
print (fruits[1])

#append an item to the list
fruits.append("orange")
print (fruits)
#insert an item to a particular position of  list
fruits.insert(2,"Lemon")
print (fruits)
#remove an item from the list
fruits.remove("banana")
print (fruits)
#print using negtive indexing
print (fruits[-1])

#print a range of items in the list
print (fruits[0:2])
#print the no of items in the list
print (len(fruits))


#Join 2 lists using +
fruits = ["apple", "banana" ]
count = [1,2]
print (fruits+count)


#Join 2 lists using extend
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#################################
# Tuple Operations
#################################


print("---------------------------")


#tuple append via list conversion
fruits = ("apple", "banana" , "cherry")
y=list(fruits)
y.append("Orange")
x=tuple(y)
print(y)


#################################
# Set Operations
#################################

print("---------------------------")

fruits = {"apple", "banana" , "cherry"}
if "apple" in fruits:
    print("apple is present")
else:
    print("apple is not present")

for i in fruits:
    print(i)


fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
print(fruits.update(more_fruits))


#################################
# Dictionaries Operations
#################################

print("---------------------------")

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#dictionaries - modify a value for a key
car.update({"year":2000 })
print(car.get("year"))

#dictionaries - added a new key & value
car.update({"color" : "red"})
print(car.get("color"))


#dictionaries - pop / remove a key value from dictionary
car.pop("color")
print(car)


#################################
# For Loops
##################################

print("---------------------------")

#break the loop , check the else part
fruits = ("apple","orange","lemon")
for x in fruits:
    if x == "orange":
        break
    else:
        print(x)


print("---------------------------")
#nested for loops
fruits = ("apple","orange","lemon")
cars = ("maruti","honda","toyota")
for x in fruits:
    for y in cars:
        print(x,y)


#################################
# Functions
##################################

print("---------------------------")

def myfunc(fname):
    print(fname)

myfunc("Nibu")
myfunc("Sample")
myfunc("Function")

print("---------------------------")
#more than one param
def myfunc(fname , lname):
    print(fname  + " " + lname)

myfunc("Nibu" , "Augustine")

print("---------------------------")
#Arbitrary Arguments, *args
def myfunc(*name):
    print("First Name = " + name[0])
    print("Last Name = " + name[1])

myfunc("Nibu" , "Augustine")


print("---------------------------")
#Default param variable in function

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


print("---------------------------")
#passing a list to a function
def my_function(country):
    for x in country:
       print("I am from " + x)

country = ["Sweden" , "India" , "Brazil"]
my_function(country)


#################################
# Lambda Functions
##################################

print("---------------------------")

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))


#################################
# Class using Pythons
##################################

print("---------------------------")
class myclass:
 x=5

ob = myclass()
print(ob.x)


#passing a list to a function
print("---------------------------")

class mydemoclass:
   def __init__(object, name , age):
        object.name = name
        object.age = age

   def myfunc(object):
       print("my name is " + object.name + " and my age is " + object.age )


ob = mydemoclass("Nibu" , "40")
ob.myfunc()

#################################
# Inheritence
##################################

print("---------------------------")


#parent and child inheritence
class parent:
    def __init__(self, fname , lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print("student's first name is " + self.fname + " and last name is " + self.lname)


class student(parent):
    def __init__(self, fname , lname):
      self.fname = fname
      self.lname = lname
    def printaddress(self):
        print("student's address is " + self.fname + " and zip code is " + self.lname)


s1 = student("2210 Baggins Ln", '28269')
s1.printname()
s1.printaddress()

print("------------#parent and child seperate---------------")


#parent and child seperate
class parent:
    def __init__(self, fname , lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print("student's first name is " + self.fname + " and last name is " + self.lname)


class student(parent):
    def __init__(self, address , zip):
      self.address = address
      self.zip = zip
    def printaddress(self):
        print("student's address is " + self.address + " and zip code is " + self.zip)


p1 = parent("Nibu" , "Augustine")
s1 = student("2210 Baggins Ln", '28269')
p1.printname()
s1.printaddress()



print("----------#additional properties adding in child which interited the parent-----------------")


#additional properties adding in child which interited the parent

class parent:
    def __init__(self, fname , lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print("student's first name is " + self.fname + " and last name is " + self.lname)


class student(parent):
    def __init__(self, fname , lname , address , zip):
      super().__init__(fname , lname)
      self.address = address
      self.zip = zip
    def printaddress(self):
        print("student's address is " + self.address + " and zip code is " + self.zip)


s1 = student("Nibu","Augustine","2210 Baggins Ln", '28269')
s1.printname()
s1.printaddress()


#################################
# Iterator
##################################

print("-------------Iterator--------------")


mytuple = ("apple" , "orange" , "lemon")
myit = iter(mytuple)

print (next(myit))
print (next(myit))
print (next(myit))


print("-------------Iterator--String Breakdown------------")


mytuple = ("apple")
myit = iter(mytuple)

print (next(myit))
print (next(myit))
print (next(myit))
print (next(myit))
print (next(myit))


print("-------------Iterator using loops - stop iteration------")

class Myclass:
    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        if self.a < 20:
            self.a += 1
            return self.a
        else:
            raise StopIteration

m = Myclass()
i = iter(m)

for x in i:
    print(x)


#################################
# Scope
##################################

print("--------global scope--------")

x = 300

def myfunc():
    x = 200
    print(x)

myfunc()
print(x)

#################################
# Module Import
##################################

print("--------global scope--------")

mymodule.namedisp("Nibu")

print("--------Platform module dir--------")
import platform

x = dir(platform)
print(x)

print("--------datetime current date--------")

import datetime as date

print(date.datetime.now())
y = date.datetime.now()
print(y.year)


print("--------datetime strftime--------")

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))


######################
# Math Modules Import
######################

print("--------Math Module--------")

import math
x= math.pow(2,3)
print (x)
x= math.ceil (5/4)
print (x)


######################
# Json Modules Import
######################
print("--------Convert JSON to Python--------")
import json

x ='{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y)
print(y["age"])


print("--------Convert Python to JSON--------")
x= {
    'name': 'John',
    'age': 30,
    'city': 'New York'
   }
y= json.dumps(x)
print(y)


#########################
# Try , except , finally
#########################

print("--------try except finally--------")

try:
 print(abc)
except:
  print("exception is raised")

print("--------try except finally revised--------")
try:
  abcd = "hello"
  print(abcd)
except:
  print("Something went wrong")
else:
  print("All Good")
finally:
  print("The 'try except' is finished")


"""print("--------raise an exception--------")
x= -1
if (x<0):
    raise Exception ("something went wrong")"""

"""x= "hello"

if type(x) is not int:
    raise TypeError("not an interger , only integer is allowed ")"""

##############
# User Input
##############

#a= input("enter the username")
#print ("User name is " + a)


#########################
# String formatting Input
#########################

print("--------String Foramtting--------")

x = "My name is {0} . {0} is {1} years old . {0} is living in {2}"
print(x.format("Nibu" , "40" , "Charlotte"))


################
# File Handling
################
"""
print("--------File Read--------")

f= open("D://Documents/Nibu/DevOps/Python/Demofile.txt")
print(f.read())

print("--------Append to the file--------")
f= open("D://Documents/Nibu/DevOps/Python/Demofile.txt" , "a")
f.write("Writing additional lines")
f.close()
f= open("D://Documents/Nibu/DevOps/Python/Demofile.txt" )
print(f.read())
f.close()
"""



print("--------Remove a file--------")
import os
"""
os.remove("D://Documents/Nibu/DevOps/Python/Demofile.txt")
f= open("D://Documents/Nibu/DevOps/Python/Demofile.txt" , "w")
f.write("hello welcome to Python")
f.close()
f= open("D://Documents/Nibu/DevOps/Python/Demofile.txt" , "a")
f.write(" Adding more comments")
f.close()
f= open("D://Documents/Nibu/DevOps/Python/Demofile.txt")
print(f.read())
f.close()"""



