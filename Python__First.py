import math
# print("Salman Mazhar")

# if 5 < 2:
#     print("Five is graeter than two!")
# else:
#     print("Two is greater than five!")

# print("Add Number")
# print(3 + 5)

# age = 27

# name = "salman mazhar"

# print("My name is" , name , "and my age is", str(age)) ; print("I am new to the world of Python Programming")
# print ("*" * 10)


# Variable

# # Ex 01
# name = "John Smith"
# age = 20
# isPatientOld = True

# # Ex 02
# name = input("Waht is you name ")
# favouriteColor = input("what is your favourite color ")
# print("My name is " + name + " and my favourite color is " + favouriteColor)

# Ex 03
# weightInPound = input("What is your weight ")
# weightInKg  = int(weightInPound) * 0.45359237
# print("Your Weight in Kg is = " + str(weightInKg))

# Ex 04
# message = "Salman is a coder"
# print(message[1:-1])
# print(message[0:])
# print(message[:])
# print(message[3:6])

# Ex 05
# first = "salman"
# last = "mazhar"
# message = f'{first} [{last}] is a coder'
# print(message)

# Ex 06
# course = "Python beginner course"
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.find("P"))
# print(course.replace("beginner","Absolute Begnienners"))
# print("Python" in course)

# Ex 07
# x = (2+3) * 10 - 3
# print(x)

# Ex 08
# x = 2.9
# y = -2.9
# print(round(x))
# print(abs(y))
# print(math.ceil(x))
# print(math.floor(x))

# Ex 09
# buyerCredit = input("Enter your credit info = ")
# price = 1000000

# if int(buyerCredit) < 10000:
#     downpayment  =  0.1 * price
#     print("You need to put 10% " + str(downpayment))
# else:
#     downpayment  =  0.2 * price
#     print(f"You need to put 20% {str(downpayment)}")

# Ex 10
# name = input("PLease eter yourr name ")

# if len(name) < 3:
#     print("Namae must contain at least 3 characters")
# elif len(name) >= 20:
#     print("Name can be a maaximun of 20 characters")
# else:
#     print("Name looks good!")

# Ex 11
# weight = int(input("Please enter your weight = "))
# unit = input("(L)bs or (K)kg: ")

# if unit.upper() == "L":
#     converted = weight * 0.54
#     print(f"Your weight in lb is = {converted}")
# elif unit.upper() == "K":
#     converted = weight / 0.45
#     print(f"Your weight in kg is = {converted}")

# Ex 12
# i = 1
# while i<=5:
#     print(i)
#     i=i+1
# print ("done")

# i = 1
# while i<=5:
#     print("*" * i)
#     i=i+1
# print ("done")

# Guess the number game
# numberToGuess = 57
# number = int(input("Plese enter your number = "))
# while number != numberToGuess:
#     if number < numberToGuess:
#         print("Plaese ente greater number")
#     elif number > numberToGuess:
#         print("Plesae enter less number")
#     number = int(input("Plese enter your number again = "))
# print("Congratulation you guess the correct number")

# Ex 02
# Building the car game
# userEnter = input("Please enter help = ")
# while userEnter.upper() == "HELP":
#     if userEnter.upper() ==  "HELP":
#         print("""
#                 start - to start the car
#                 stop - to stop the car
#                 quit - to exit
#                 """)
#     else:
#          userEnter = input("Please enter help = ")
# while True:
#     userInput = input("Please enter option ")
#     if userInput.upper() == "START":
#         print("Car started... Ready to go!")
#     elif userInput.upper() == "STOP":
#             print("Car stopped.")
#     elif userInput.upper() == "QUIT":
#             print("Exiting game...")
#             break
#     else:
#         print("I don't understand that...")


# Guess the number game practice second time
# numberToGuess = 57
# number = int(input("Please enter your number to guess = "))
# while number != numberToGuess:
#     if numberToGuess > number:
#         print("Enter smaller number ")
#     elif numberToGuess < number:
#         print("Enter greter number ")
#     number = int(input("Please enter your number to guess = "))
# print("You guess the corrcet number")

# Building the car game
# counter = 0
# print ("Please enter help")

# while True:
#     userInput = input("> ").upper()

#     if userInput.upper() == "START":
#         if counter == 0:
#              print("Car started... Ready to go!")
#              counter = 1

#         else:
#              print("Car is already started")

#     elif userInput.upper() == "STOP": 
#             if counter > 0:
#                  print("Car is stopped")
#                  counter = 0
#             else:
#                  print("Car is already stopped")
#     elif userInput.upper() == "HELP":
#          print("""
# start - to start the car
# stop - to stop the car
# quit - to exit
# """)
#     elif userInput.upper() == "QUIT":
#             print("Exiting game...")
#             break
#     else:
#         print("I don't understand that...")

# For loop
# for item in range(10):
#     print(item)

# for item in range(5,10):
#     print(item)

# (5 ,10) means ir range between 5 to 10 and means it jumps 2 numbers
# for item in range(5,10,2):
#     print(item)

#For Ex Total number of list amount
# for itemsAmount in (10,20,30):
#     total = itemsAmount + total

# print(total)

# Nested Loop 
# for x in range(4):
#     for y in range(3):
#         print(f'({x},{y})')

# Nested Loop Ex
# My solution
# numbers = [5,2,5,2,2]
# for y in numbers:
#         print(y * "x")

# Mosh Solution without python built in function
# numbers=[5,2,5,2,2]
# for x in numbers:
#     output = ""
#     for y in range(x):
#         output += "x"
#     print(output)

# Largest Number in list find Ex
# numbers = [1,2,3,4,5,3,213,43,2,4,666]
# biggetNumber = numbers[0]
# for x in numbers:
#     if x > biggetNumber:
#         biggetNumber = x
# print("Largest number in array is " , biggetNumber)

# 2D list
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(matrix[0][2])
# for row in matrix:
#     for item in row:
#         print(item)

#list methods
# Add new number in the list
# numbers = [5,3,4,6,7,8,1,4]
# numbers.append(20)
# print(numbers)

# # Add number between the list
# numbers.insert(3,18)
# print(numbers)

# #To item from the list
# numbers.remove(18)
# print(numbers)

# # To remove item from the end of the list
# numbers.pop()
# print(numbers)

# #To clearr the data frorm he list
# # numbers.clear()
# # print(numbers)

# #To find tthe index number of the list item
# print(numbers.index(3))

# # To find if number is present in the string or not
# print(100 in numbers)

# #To find the repeated value in the list
# print(numbers.count(4))

# #To sort he list
# numbers.sort()
# print(numbers)

# #To Sort list in reverse
# numbers.reverse()
# print(numbers)

#List Methods Ex
# numbers = [2,2,4,5,6,6,7,8,9,9]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

# Tuples are like a list we can store items init but we cannot change its value like list
# numbers = (1,2,3)
# # numbers[0] = 10 -- We cannot change its value if we define a tuple
# print(numbers)


#unpacking is a powerfull tool in python EX we have a list and we want to use each item in the individually so we can use unpacking at that tttime
# items = (1,2,3)
# x, y, z = items
# print(x)
# it auttomatically see the item in tuples and set them to the values we define

#Dictionaries
#One of the most important part is the dictionaries in the python
#We store information tthat comes in key value pair

# customer = {
#     "name" : "Salman",
#     "lastName" : "Mazhar",
#     "age" : 30,
#     "isVrified" : False
# }

# # print(customer["name"], customer["lastName"])
# # print(customer.get("birthday", "Jan 1 1990")) ineted of none we get defaul value

# # We can also update value in the dict
# customer["name"] = "Salman Mazhar"
# print(customer["name"])

# customer["birthdate"] = "Jan 01 2000"
# print(customer["birthdate"])

# Dict Ex
# userInput = input("Phone No : ")

# phoneDicty = {
#     "1" : "One",
#     "2" : "Two",
#     "3" : "Three",
#     "4" : "Four"
# }
# output = ""
# for x in userInput:
#     output += phoneDicty.get(x , "!") + " "
# print(output)

# function
# Simple Addtion function
# def greet_user():
#     print("""
#         how are yoiu
#           i am fine 
#           and you
#         """)
# greet_user()

# Prameters in fucntion
# def additionOfNumbers(x,y):
#     print(x+y)
# additionOfNumbers(4,5)

# Prameters in fucntion
# def additionOfNumbers(x,y):
#     return (x+y)
# v = additionOfNumbers(4,5)

# Mosh EX
# def greet_user(first_name, last_name):
#     print(f"Hello {first_name} {last_name}")
#     print("Welcomwe abord!")

# greet_user("Salman", "Mazhar")
# greet_user("hamza", "Mazhar")
# greet_user("usman", "Mazhar")
# greet_user("afaq", "javed")

# Exceptoin
# try:
#     age = int(input("Age : "))
#     income = 20000
#     risk = income/age
#     print(age)

# # Only excepts error that you define in except
# except ZeroDivisionError:
#     print('Age cannot be divided by 0')
# except ValueError:
#     print("invalud value")



# Classes

# class Point:
#     def __init__(self,x,y): # Connstructor
#         self.x = x
#         self.y = y
#     def move(self):
#         print("Moev")
#     def draw(self):
#         print("Draw")

# point = Point(10 ,320)
# point.x = 11
# print(point.x)
# print(point.y)

# Classes example
# class Person:
#     def __init__(self,name):
#         self.name = name

#     def talk(self):
#         print(f"Hi, I am {self.name}")

# salman = Person("Salman Mazhar")
# salman.talk()

# usman = Person("Usman Mazhar")
# usman.talk()


# Classes inheritance
# class Mammal:
#     def walk(self):
#         # print("Walking")
#         return "walking"
#     def flying(self):
#         return "flying"

# class Dog(Mammal):
#     def animalDog (self,animalName):
#         print(f"{animalName} is " + self.walk()) 
#         # self.walk()

# class Cat(Mammal):
#     def animalCat (self , animalName):
#         print(f"{animalName} is walking")
#         self.walk()

# class Parrot(Mammal):
#     def birdParrot (self, birdName):
#         print(f"{birdName} is "+self.flying())

# dog1 = Dog()
# dog1.animalDog("dog ")

# cat1 = Cat()
# cat1.animalCat("Cat ")

# bird1 = Parrot()
# bird1.birdParrot("Macaw")

#Modules practice and Ex
# import converters
# print(f"Your weight in kg is {converters.kg_to_lbs((74))}")

# from converters import lbs_to_kg
# print(f"Your weight in kg is {lbs_to_kg((164.4444))}")

# from utils import find_max #This will only import function from the other file
# import utils #This will import all the function from the module file

# #Both are correct
# numbers = [10,8,7,4]
# print(find_max(numbers))
# print(utils.find_max(numbers))

#Package for modules
#This is good to work but we use other approach to make our life easier
# import ecommerce.shipping
# ecommerce.shipping.calculate_shipping()

# #Second approach
# from ecommerce.shipping import calculate_shipping
# calculate_shipping()

# #Third and ery useable approach
# #Using this approach we can import all he modules with one line and use them as many as we want
# from ecommerce import shipping
# shipping.calculate_shipping()

#Generathing random values
import random
# for i in range(3):
#     print(random.random())


# This will generate only random values that we provide
# for i in range(3):
#     print(random.randint(10,20))



# WE can also choose the values randomly from the list
# members = ["salman", "usman", "hamza", "ahsan", "afaq"]
# leader = random.choice(members)
# print(leader)

# Dice game
# Solution 1
# class Dice:
#     def roll(self):
#         first = random.randint(1,6)
#         second = random.randint(1,6)
#         print(first, second)

# dice1 = Dice()
# dice1.roll()

# Solution 2
# class Dice:
#     def roll(self):
#         first = random.randint(1,6)
#         second = random.randint(1,6)
#         return [first, second]

# dice1 = Dice()
# print(dice1.roll())

#My approach but not very good
# for i in range(3):
#     print(f"({random.randint(1,6)} , {random.randint(1,6)})")


# Working with directory
from pathlib import Path

# To find the directory exists or not
# path = Path ("ecoomerce")
# print(path.exists())

# To create a directory
# path = Path("emails")
# print(path.mkdir())

#To remoe the directory
# print(path.rmdir())


#To find the files and directry in system in the current path
path = Path()
# print(path.glob('*.py'))
for file in path.glob("*.py"):
    print(file)