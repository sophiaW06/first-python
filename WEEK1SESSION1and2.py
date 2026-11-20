# #idk what i'm doing in this class but YOLO
# """
# grgrgrggrgrr
# this is a multi line comment 
# it can be used to write multiple lines of comments
# heehee

# """
# print("hi")
# print("welcome","to","python")
# print("welcome \nto \npython!")
# print("\\insert a backslash character in a \\string")
# print("\t inserts a horizontal tab")
# print(" \" insert a double quote in a string e.g \"cat\" ")
# print(" \" insert a single quote in a string e.g \'dog\' ")
# print("HELLO WORLD CWC") #ignore this
# print("mama \nwants \ndrinks")
# print("don't \nmake \nme \ndrink \nalone")
# print("it's","5'O'Clock","somewhere")
# print('\tinserts a horizontal tab')
# print("I'm making a sentence and inserting a \nline break,","doesn't it look cool?") #yass it looks so cool
# print("\tno way, did you just see that?") #yass i did see that
# print('single quote because i am the goat')

# # name = input("Enter your name: ")
# #print("Hello", name, "Welcome to Python programming")

# x = 6 
# y = 7
# #variables up here 
# # statement: a line of code that does something 

# print("addition of two nos", x+y)
# print("substraction of two nos", x-y)
# print("multiplication of two nos", x*y)
# print("division of two nos", x/y)
# print("power of two nos", x**y)

# word = "My name is"
# name = "Mr. Computer Science"
# identity = word + " " + name
# print(identity)

# """
# PYTHON VOCAB
# string = any chracter or word
# float = decimals
# int = whole number
# dict = { BMW: 325, Engine: "V6", Year:2016} #key/value
# Tuple = ("Europe", "Africa", "Asia") any true cell value
# Boolean = True/False (Start/Stop)
# List = a list of random items
# Set = {1,1,2,2,3,3,5} anywhere you don't want anything to repeat, you use set 

# DATA TYPES IN PYTHON
# numeric = integer, float, complex number (a number with a real or imaginary component x+yj
# boolean = data with one of two built-in values TRUE or FALSE, 1 or 0 e.g. c = TRUE, b = FALSE
# """

# x = 32 
# y = 3.143
# print(x, "is an integer and the data type is: ", type(x)) #<class 'int'> should be displayed upon running
# print(y, "is a float and the data type is: ", type(y)) #<class 'float'> should be displayed upon running

# print(10>9) #displays TRUE
# print(3<1) #displays FALSE

# c = True
# d = False
# print("Start Engine", c) 

# """
# PYTHON MEMORY SLOT:

# - How Python saves variables in memory 
# Message --> "I am a string"
# N --> 17
# Pi --> 3.1459
# Syntax: id(variable

# Sequence Type

# String = ""/'' Single/Double Quotes
# List = [] Square Brackets
# Set = {} 
# Tuple = () Parentheses
# Dictionary = {key:value} 
# """

# print("The memory location of x in my processor is: ", id(x))

# e = "a"
# vowels = ("a","e","i","o","u")
# print(vowels, "what is the data type", type(vowels))

# mylist = ["book", "pen", True, False, 28, -34, 56] 
# print("This is my list", mylist, type(mylist))

# myset = {1,1,2,2,3,3,5}
# print(myset, "the data type is", type(myset)) #<class 'set'> displayed upon running



# car = {
#     "make" : "BW",
#     "model": 320,
#     "year": 2026,
#     "Trans": "Auto",
#     "4wd": True
# }

# print("my dictionary is", car, type(car))
# print(car.keys()) #dict_keys
# print(car.values()) #dict_values

# """
# Syntax = helps programmers to do coding in fewer steps 
# Java Hello World code

# class HelloWorld

# { 
#     public static void main(String args[])
#     {
#        System.out.println("Hello, World");
#        }
#     }

#     Python Syntax   Indetation not Braces
    
#     Python uses whitespace (tabs or spaces) to structure code instead of using braces 
#     for x in array: 
#     if x < pivot: 
#     less.append(x)
#     else: 
#     greater.append(x)

#     python statements also do not need to be terminated by semicolons
#     semicolons can be used, however, to separate multiple statements on a single line
#     e.g.
#     a= 5; b = 6; c = 7;
#     print("do not terminate python code with semicolons");
#     """

# a = 5; b=6; c=7
# print("hello python");
# print(b)

# a_list =[5,6,7, None]
# print("first item at index 0 is", a_list[0])
# print("first item at index 2 is", a_list[2])
# co_list = list(vowels) 
# print("The constructor list", co_list)

# """
# List is random
# - variable-length
# - mutable (can be modified)
# - can be defined using square brackets [] or using list type function list()
# - list() is a constructor (special methods to initialise objects when they are created from a class) 
# (helps asign inital values to object attributes and prepare objects for use)
# - takes an iterable (any object that is capable of returning its elements one at a time, allowing it to be looped over using a loop)
# as input

# Slicing a List

# You can extract a subset of a list by using a slice
# Example: 
# legends =['Groucho', 'Chico', 'Harpo', 'Carlin', 'Pryor']
# legends[0:2] ['Groucho', 'Chico']
# legends[1:3] ['Chico', 'Harpo']
# legends[:] ['Groucho', 'Chico', 'Harpo', 'Carlin', 'Pryor']

# Tuple is defined 

# """
# legends = ['Groucho', 'Chico', 'Harpo', 'Carlin', 'Pryor']
# print(legends[-2:4])

# L = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]
# print(L[1:3])

# """
# List Method append()

# Items can be appended to the end of the list with the append() method:
# Syntax:
# list.append(item)

# Add items to the i.e. big_birds and marxes list with the append() method
# big_birds = ['emu', 'flamingo', 'cassowary']
# big_birds.append('ostrich')
# print(big_birds)

# marxes = 'Groucho', 'Chico', 'Harpo']
# marxes.append('Zeppo')
# print(marxes)

# List Method remove()

# Elements can be removed by value with remove(), which locates the first such value and removes it 

# Syntax: 
# list.remove(item)

# List Method insert()

# Syntax:
# list.insert(index, item)

# i.e.
# games = ['Atari', 'Nintendo', 'Gameboy', 'Sega']
# games.insert(1, 'playstation')
# print(games)
# """

# legends.append("Diane Morgan")
# print("Our new refreshed list", legends)

# legends.remove("Diane Morgan")
# print("Our list after deletion", legends) #sorry girl

# games = ['Atari', 'Nintendo', 'Gameboy', 'Sega']
# games.insert(1, 'playstation')
# print(games)

# games.insert(1, 'XBOX')
# print(games)

# print(games[1])
# print(games[0])

# print(f"I love watching shows that feature {legends[1]}") 

# OrderItem = [1, "Jeff", "Computer", 75.50, True] # 1 = 0, Computer = 2, True = 4
# print(OrderItem[0])
# print(OrderItem[2])
# print(OrderItem[4])

# """
# sort() = sorts item in a list into order
# pop() = removes an item from a list, without an index it removes the last given item from the list
# reverse() = reverses the order of items in a list 

# """
# #SORT()
# numbers = [6, 2, 9, 1, 7] 
# numbers.sort()
# print(numbers)

# #POP()
# numbers.pop()
# print(numbers)

# #REVERSE()
# numbers.reverse()
# print(numbers)

# """
# DICTIONARY

# - flexibly sized collection of key-value pairs, where key and value are Python data types like boolean, integer, tuple, string
# and others 
# - mutable
# - you can add, delete and change their key-value elements
# - can be created with {} and dict()
# """

# eng2deu= {'one':'eins', 'two':'zwei', 'three':'drei'}
# countries = {}
# countries["UK"] = "EUROPE"
# countries["CHINA"] = "ASIA"
# countries["NIGERIA"] = "AFRICA"
# print(eng2deu.keys(),eng2deu.values(),"\n", countries)

# print(eng2deu, "\n", countries)

# apps = dict(twitter="USA", tiktok="CHINA", faceapp="RUSSIA")
# print(apps)

# list_items = [ ['Weather', 'Sunny'], ['Volume', 'Loud'], ['Hell', 'HOT'] ]
# print("Dictionary created from list", dict(list_items))

# Zelda_Characters = {'Sheik' : 'Zelda',
#                     'Majora' : 'Skull Kid',
#                     'Linkl' : 'Fem! Link'
# }

# others = {"Koopa King" : "Bowser"}
# print("Mario" in Zelda_Characters)
# print("Sheik" in Zelda_Characters)

# Zelda_Characters.update(others)
# print("The new updated Zelda_Characters dictionary: ", Zelda_Characters)

# # Syntax: dict.update(dict)

# print(Zelda_Characters ["Sheik"])

# """
# Syntax: dict['key']
# Syntax: dict.get('key') RETRIEVES VALUE OF A SPECIFIED KEY FROM A DICTIONARY 
# - returns NONE by default if the specified key is not present 
# Syntax: del dict['key']  DELETES VALUE OF A SPECIFIED KEY FROM A DICTIONARY

# i.e. 
# Zelda_Characters=['Sheik':'Zelda']
# del Zelda_Characters['Sheik']

# TO DELETE EVERYTHING
# Syntax: dict.clear()
# Zelda_Characters.clear()

# """

# Mario_Characters = {'M': 'Mario', 'Princess Toadstool':'Peach', 'Dead Koopa':'DryBones'}
# others2 = {'Star' : 'Lumilee', 'Princess of the Galaxy':'Rosalina'}
# Mario_Characters.update(others2)
# print(Mario_Characters)

# """
# To copy a dictionary copy()

# Syntax:
# dict.copy()

# e.g.

# signals = {'green': 'go', 'yellow' : 'go faster', 'red': 'smile for the camera'}
# signals.copy()
# Traffic_light = signals.copy()

# TUPLE
# - fixed-length, immutable sequence of items
# - the sequence of objects contained within the tuple is fixed at the time of construction
# - elements cannot be added, removed, reordered or replaced 

# e.g. 
# tuple1 = ('a','b','c','d','e')
# tuple[0] = 'f'

# TypeError: object doesn't support item assignment 

# To create a tuple with a single element, we have to include a final comma. 
# tuple1 = ('a',)

# tuple()

# syntax: 
# tuple(iterable)

# """
# newtuple = tuple(legends)
# print("This is my new tuple", newtuple)

# """
# Tuple Slicing

# You can extract a subset using a slice

# Count items in Tuple

# count()

# Syntax:
# tuple.count(item)

# Tuples addition: 
# tuple1 = (1,2,3)
# tuple2= (4,5,6)
# tuple3= tuple1 + tuple2

# print("This is my new tuple: ", tuple3)

# """
# print(newtuple[1:4])
# print(newtuple[-2])

# """
# SET {}

# set()

# An unordered collection of unique elements
# - like dicts, but ONLY keys, no values
# - DOESN'T REPEAT

# e.g.
# Set1 = {1,2,3}
# Set2 = {"red","green","blue"}

# Using set() to create set
# Letters = set ( 'letters' )
# numbers = set([2,2,2,1,3,3]) #list
# set( ('Beta', 'Gamma', 'Alpha') ) #tuple

# SET operations

# a = {1,2,3,4,5}
# b = {3,4,5,6,7,8}

# Merge two sets use the union() method or | binary operator
# a. union(set)
# a | b

# To get elements in common use intersection(set) or & binary operator 
# a. intersection(set)
# a & b 

# """

# set2 = ("red", "green", "blue") 
# set3 = set("letters")
# print(myset, set2, set3)

# k = (1,2,3,4,5)
# 1 = (3,4,5,6,7,8)

# m = k.union(1)

# print("the union of k and 1 sets", m)
# print("Items in common", k&1)


# """
# To bring code back to life, CTRL + forward slash
# Type CLEAR to clear terminal

# SESSION 1 WEEK 2 

# """

# a, b, c = 5,3.2, "Hello"
# print(a)
# print(b)
# print(c)

# current_salary = 1000
# PI = 3.142
# SPEED_OF_LIGHT = 3600000
# FirstName = "Sophia"
# lastName = "Wells"
# print(current_salary,  PI, SPEED_OF_LIGHT,
#       FirstName, lastName)

# print("show me the type of my data:",
#       type(current_salary), "PI", type(PI),"FirstName",
#       type(FirstName))

# """
# You cannot use a reserved Python keyword as a variable name  (i.e. def)

# def function_name (List of parameters):    # Paramaters is variables
# STATEMENTS                                           # STATEMENT IS A SINGLE LINE VARIABLE ASSIGNMENT

# CALL

# Any created function must be called in order to perform its operation
# You call the function to run it 

# def Function_name():
# """
# #Function without Parameter
# def myFunction():
#     print("Sweet angel babies mamas got you")  #*no. multiplies the amount of time this is printed

# myFunction() 

# #Function with two Paramaters

# def add_numbers(a,b):
#     c = a + b
#     print("The result of adding two numbers is", c)

# add_numbers(5, 5000)

# # Function with one Parameter

# def my_email(student_id):
#     print(student_id + "@leedstrinity.ac.uk")

# my_email("2608364")

# # with optional parameter 

# def greet(name, msg= "good morning mama."):
#     print("Hello", name + ', ' + msg)

# greet("Sophia") 

# """
# Function Rules (Indentation)

# Statements inside function must be indented from the left margin 

# """
# # 1) Write a function that divides two numbers

# def divide_numbers(a,b):
#     c = a / b
#     print("The result of dividing two numbers is", c)

# divide_numbers(429, 247)

# """
# 2 ) Define a function that takes in two inputs first name and last name. Print the following statement "My name is first name last name."

# """

# def print_name(FirstName, lastName):
#     print("My name is", FirstName, lastName)

# print_name("Sophia","Wells")

# """
# 3) Write a function that takes one input and output the squared of that input. For example, if the input is 5,
# the function should output 25

# """

# def square(number):
#     print(number ** 2)

# square(5)

# """
# FLOW OF EXECUTION

# In order to ensure that a function is defined before its first use, you must have to know 
# the order in which statements are executed

# e.g.

# def newline():
#               print("Execute First")  #1
#               print("second statement") #2
#               print("Third statement") #3

# Execution always begins at the first statement of the program
# - executed one at a time, in order from top to bottom

# PARAMETERS AND ARGUMENTS

# - Some of the built-in functions require arguments:
# - inputs that control how the function does its job
# e.g.
# type(input), str(24)

# - Some functions take more than one argument:
# e.g. 
# pow(base,exponent) 3^3

# PARAMETER

# - Python handles function arguments in a very flexible manner
# - Supports multiple types of arguments in the function definition:
#      - Positional arguments PA # The first value goes to the first parameter, second to the second, and so on
#                                # Changing the order can lead to unexpected results.
#      - Keyword arguments  KA # Order does not matter as long as the names are correct,
#                           #Defaults are used if some arguments are not provided
#                           #Makes code more readable and less error-prone
#      - Default arguments
#      - Variable Length Positional Arguments (*args) VLPA # For multiple variables use (*) before the input
#                                                         # for when you aren't completely aware of the argument, circumstantial 
#                                                         # e.g. def my_function(*inputs)
#                                                         print ("The youngest student is" + inputs[2])
#                                                         my_function("Liam","Thomas", "Peter")
#      - Variable Length Keyword Arguments (**kwargs) 

# Double Parameters 

# e.g. 
# def printTwice(prm1, prm2):
#      print("I am the first parameter :", prm1)
#      print("I am the second parameter :", prm2)

# def printName(fname, lname):
#     print("Name of the applicant", fname, lname)

# Variables / Parameters in Functions are local 
# - bound to function's local scope
# - only exist while the function is being executed 
# - cannot be assessed outside the function
     
# LAMBDA FUNCTIONS
# - can have any number of arguments but only one expression
# - expression is evaluated and returned 

# SYNTAX:
# lambda arguments: expression

# """

# squaredFunction = lambda x: x**2
# print("My first lambda square function: ", squaredFunction)
# def squared(x):
#     c = x ** 2
#     print("My output", c)

# print("========= SESSION 2 WEEK 2 =========")
# """
# SESSION 2 WEEK 2 

# CONTROL FLOW: DECISION MAKING AND LOOPS 

# - Decision making: (Yes, No, Break, Continue)
# - Decision making is required when we want to execute a code only if a certain condition is satisfied
# - The if..elif..else statement is used in Python for decision taking

# CONDITIONALS: IF 

# - We need the ability to check conditions and change the behaviour of programmes accordingly 
# - e.g. 
# if x > 0:
#    print("x is positive")

# - The Boolean expression after the IF statement is called the condition. 
# - if it is true, then theindented statement gets executed or otherwise
# - no limit on the number of statements that can appear in the body of an if statement
# - BUT there has to be at least one

# Decision Making: 
# if (expression is True):
#     execute statement(s)

# Decision making is required when we want to execute a code only if a certain condition is satisfied.
# """
# x = -25
# if (x > 0):
#     print("X is a positive integer")
# else:
#     print("X is 0 or less than 0, a negative no.")

# passing_score = 40
# my_score = 38

# if (my_score >= passing_score):
#     print("I have passed the module!", my_score)
# else:
#     print("Your score is too low to pass.", my_score)

# if "Python" in ["Java", "C#0", "C", "Python"]:
#     print("Python is in the list")


# """
# CONDITIONAL IF & PASS

# - Occasionally, it is useful to have a body with no statements (place keeper for code you haven't written yet)
# - you can use a PASS statement, which does nothing 

# if 2 > 0: 
# pass 

# ALTERNATE EXECUTION: 
# - a second form of the if statement is alternative execution, in which there are two possibilities

# if (condition):
# #block of code to be executed if the condition is true 
# else:
# #block of code to be executed if the condition is false


# """
# print("Even", 2%2, "Odd with remainer", 3%2)

# x = 18
# def checkEvenOdd(x):
#     if (x % 2 == 0):
#         print(x, "is even")
#     else:
#         print(x, "is odd")

# checkEvenOdd(18)


# """


# """
# def checkSize(x):
#     if (x > 3):
#         print(x, " is bigger")
#     else:
#         print(x, "is smaller")

# checkSize(55)

# """
# 1) Write a conditional for this scenario. If the temperature is above 30 degrees print "stay at home", and if the temperature
# is below 30 degrees, print "I am out and about".

# """

# def checkTemp(x):
#     if (x > 30):
#         print(x, ",", "I'm staying at home, it's way too hot!")
#     else:
#         print(x, "," , "I'm out and about!")

# checkTemp(50)

# """
# 2) CHECK FLOW CHART PPT FOR MY RESPONSE

# 3) The variables a = 14 and b = 14, write a conditional logic that satisfies the following: 
# i. if a is greater than b, print "a is the bigger number"
# ii. else if a = b, print "a and b are equal"
# iii. else, if b is greater than a print "b is bigger than a"

# """
# """
# CHAINED CONDITIONS

# - Sometimes there are more than two possibilities, and we need more than two branches
# if condition:
# # block of code to be executed if condition is true 
# elif condition:
# #block of code to be executed if first condition is false
# else:
# # code to be executed if all conditions above are FALSE

# e.g. 

# if x < y:
#      print(x, " is less than", y)
# elif x < y:
#     print(x, " is greater than", y)
# else:
#     print(x, " and ", y, "are equal")

# - elif is an abbreviation of "else if."
# - there is no limit to the number of elif statements
# - BUT the last branch has to be an else statement

# """

# """
# NESTED CONDITIONAL 

# - a conditional expressed under another condition is referred to as a Nested Conditional
# e.g.

# if 0 < x:
#     if x < 10:
#        print(x, " is a positive single digit")

# - the print statement is executed ONLY if we make it past both the conditionals 

# Nested Conditionals using AND

# - we can use the AND operator to express the previous nested expressions

# if 0 < x and x < 10:
#     print(x, " is a positive single digit")

# The mathematical expression is as follows:

# if 0 < x < 10:
#      print(x, " is a positive single digit")


# """

# """
# RETURN STATEMENT

# - Allows you to terminate the execution of a function before you reach the end
# - the return keyword is to exit a function and return a value...

# def fun():
#    statements
#    .....
#    .....
#    return [expression]

# def cube(x):
#     r = x**3
#     return [r]

# - One reason to use return is if you detect an error condition

# def printResult(x):
#     if x <= 0:
#        print ("Positive numbers only, please.")
#        return
#        result = x + 2  #ignored
#     print("This is the result ", result)
# """
# x = -40 
# def printResult(x):
#     if x <= 0:
#         print ("Positive numbers only, please.")
#         return
# result = x + 2

# print("This is the result,", result)

# printResult(x)


# """
# RECURSION

# - The ability for one function to call another is called recursion


# """

# def countdown(n):
#     if n == 0:
#       print ("HAPPY NEW YEAR!!!")
#     else:
#         print(n)
#         countdown(n-1)

# countdown(10)

# """
# FOR LOOP

# - used to iterate over a sequence (list, tuple, string) or other iterable objects 
# # any object in programming that can be looped over or traversed item-by-item, usually using a for loop
# # capable of returning its elements one at a time
# - iterating over a sequence is called traversal

# - FOR statement allows you to repeat an action or several actions for each item in a sequence of items
# - Loop continues until we reach the last item in the sequence

# for VARIABLE in LIST: LOOP BODY
# for VARIABLE in range(): LOOP BODY

# - You can iterate over a sequence of elements using the different variations of for loop

# for letter in 'Programming':
#     print(letter)

# for x in range(0,3)
#     print(x)

# e.g.

# genre = ["pop", "rock", "jazz"]

# # iterate over the list using index
# for i in range(len(genre)):
#     print("I like", genre[i])

# digits = 

# """

# genre = ["pop", "rock", "jazz"]

# for music in range(len(genre)):
#     print("I like", genre[music])  #

# digits = [0, 1, 5]

# for i in digits:
#     print(i)
# else:
#     print("No items left.")


# # Program to find the sum of all numbers stored in a list

# #List of numbers
# numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# #Variable to store the sum
# sum = 0 

# # iterate over the list
# for val in numbers:
#     sum = sum+val

# print("The sum is", sum)

# for number in range(20):
#     if number % 2 == 0:
#         print(number)

# """
# WHILE CONDITIONAL (LOOPING)

# - while statement allows you to repeat one or more actions while a condition remains TRUE

# Syntax:
# while test_expression:
#       block of code

# """

# #e.g.

# count = 1 
# while count <= 5:
#     print(count)
#     count +=1      #count = count + 1 

# """
# USING ELSE IN WHILE LOOPING

# e.g. 

# counter = 0

# while counter < 3:
#      print("Inside the loop")
#      print("The current counter is:", counter)
#      counter = counter + 1 
# else:
#     print("Inside else")


# """

# counter = 0

# while counter < 3:
#      print("Inside the loop")
#      print("The current counter is:", counter)
#      counter = counter + 1 
# else:
#     print("Inside else")

# """
# ---------- WEEK 3 SESSION 1 -----------
# ---------- OBJECT ORIENTATED PROGRAMMING -----------

# OBJECT = anything that you want to model inside of a computer environment 
# - created using CLASS
# - multiple objects at the same time referred to as instances

# * CRAFTING CLASSES

# CLASS = BLUEPRINT OF OBJECTS
# - custom data structure containing attributes and functions called methods (i.e. car, bird, etc.)
# - user-defined prototype for an object that defines a set of attributes that characterise any object of the class

# ATTRIBUTE = a variable inside a class that is part of the characteristics of the class or the object
# - can assign attributes when creating a class or after

# METHOD = actions portrayed by the object
# - defined inside a class definition
# - makes the r'ship between class and method explicit
# - syntax for invoking a method different from syntax for calling a function 

# # SYNTAX

# def nameOfMethod(self ): 
#     pass 
    


# """

# #CLASS INITIATION

# print("GOOD MORNING BALTIMORE")

# class CAR:
#     #attributes
#     make = "mercedes"
#     model = "C-Class"
#     year = 2019
#     manual = False
#     color = "Blue" #BOOLEAN

# # Instance a reference of the class object
# # Create instance
# mycar = CAR()
# print(mycar.model, mycar.year)

# print("Is the car manual?", mycar.manual)
# """
# Access / GET method 

# - to access attributes of the created class 

# *SYNTAX
# Instance.attribute

# SET method

# - to modify intitialised or created values of the attribute 

# *SYNTAX
# Instance.attribute = new_value

# """

# #mycar.manual = True

# #print("Is the car manual?", mycar.manual)

# """
# ATTRIBUTE ASSIGNMENTS IN CLASS IS STATIC

# - any created object has default values of the class attribute

# AUTOMATE ATTRIBUTE ASSIGNMENT  __init__

# - to assign object attributes at creation time
# - intitialization method:

# def __init__(self):
#         pass 
        
# _init_() is a method that initialises an individual object from its class definition

# - first parameter should be named self if it is an object
# - self is NOT a reserved word

# i.e. 

# class Car():
#     def __init__(self, make):
#             self.make = make

# - can create an object from the Car class by passing a string for the name parameter 
# """

# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
#     def display(self):
#         print("Make:", self.make, "Model:", self.model)

# CAR = Vehicle("Audi", "A3")
# CAR.display()

# """
# Class Attribute __class__

# - Class attributes are the same for all instances of a class

# """

# class Vehicle(object):
#     Transmission = "Automatic"
#     def __init__(self, make, model, speed):
#         self.make = make
#         self.model = model
#         self.speed = speed
    
#     def accelerate(self):
#         print("The car is accelerating at", self.speed, "mph")
#         self.speed = self.speed + 30
#         print("The car is moving at", self.speed, "mph")

#     def stop(self):
#         print("Applying Breaks")
#         self.speed = self.speed - 10
#         print("The car is moving at", self.speed, "mph")

#     def turnRight(self):
#         print("The car is turning right")


# CAR = Vehicle("Audi", "A3", 30)

# CAR.accelerate()
# CAR.stop()
# CAR.turnRight()
# CAR.accelerate()

# """
# GETTER AND SETTER INTRODUCTION

# - Add validation logic around getting and setting a value

# GETTER METHOD: retrieving data 



# """

# def getSpeed(self):
#     print("The current speed is:", self.speed, "mph")

#     def __init__(self, make, model, speed):
#         self.make = make
#         self.model = model
#         self.speed = speed

# CAR = Vehicle("Audi", "A3", 30) 

# """
# PYTHON FORMAT OUTPUT

# - format() method output specifies values
# - inserts them inside a string's placeholder
# - placeholder defined using curly brackets {}
#        - name
#        - number
#        - empty 


# e.g. 

# NAME:

# txt1 = "My name is {fname}, I'm {age}". format(fname = "John", age = 36)

# NUMBER:

# txt2 = "My name is {0}, I'm {1}". format("John", 36)

# EMPTY: 

# txt3 = "My name is {}, I'm {}". format("John",36)



# """
# # METHODS WITH ARGUMENTS

# class Parrot(object):

#     #instance atttributes
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     #instance method
#     def sing(self, song):
#         return "{} sings {}".format(self.name, song)

#     def dancing(self,dance):
#         return "{} is now dancing {}".format(self.name, dance)


# """
# ----------- WEEK 3 SESSION 2 -------------

# ENCAPSULATION

# - method of wrapping data and functions into a single entity 
# - a class encapsulates all the data 

# """

# class Employee(object):
#     def __init__(self, name, id, salary):
#         #public member
#         self.name = name 
#         self.id = id
#         self.salary = salary

#     def show(self):
#         print("My name is ", self.name, "with ID", self.id, "and my salary is", self.salary)

# emp = Employee("Dianne", "A123", 40000)
# emp.show()

# # access salary from outside of a class 
# print(emp.salary)

# """
# ENCAPSULATION

# - acts as a protective layer
# - can restrict access to methods and variables from outside
# - can prevent data from being modified by accidental/unauthorised modification 
# - hides data
# - PYTHON can achieve encapsulation by using prefix single / double underscore 
#           - controls access of variable and method 

# """

# # Encapsulation (restrict salary)

# class Employee(object):
#     def __init__(self, name, id, salary):
#         #public member
#         self.name = name
#         self.id = id 
#         #private member
#         #not accessible outside of a class
#         self._salary = salary

#     def show(self):
#         print("Name is", self.name, self.id, "and salary is", self._salary)

# emp = Employee("Yasseer", "C334", 40000)
# emp.show()

# """
# STATIC METHOD

# - general utility method that performs a task in isolation 
# - no self reference
# - consumes less memory 

# CLASS METHOD

# - called on the class itself, NOT on a specific object instance
# - class level, all class instances share a class method
# - bound to the class
# - can only access class variables
# - can modify class state by changing the value of a class variable
# - cls as the first parameter 



# """

# class Student(object):
#     schoolName = "Microsoft Academy" #global attribute
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def admission(cls, name):
#         print("This is the first school name: ", Student.schoolName)
#         Student.schoolName = name
#         print("The new attribute name", Student.schoolName)

# student1 = Student('Akram', 20)
# student1.admission('Akram')


# """
# METHOD WITH NO ARGUMENTS 

# *SYNTAX

# def functionName(s):
#     #user code

# i.e.

# def carInfo(self):
#     print("This is the model of the car", self.model)


# METHOD WITH ONE ARGUMENT

# *SYNTAX

# def functionName(self, arg1):
#     #user code


# i.e.

# def setBrand(self, psg):
#    self.passengers = psg
#    print("Number of passengers", self.passengers)


# METHOD WITH TWO ARGUMENTS

# *SYNTAX:

# def functionName(self, arg1, arg2):
#     #user code

# i.e.

# def setBrand(self, carmake, carmodel):
#     self.make = carmake
#     self.model = carmodel
#     print("This is the model of the car", self.make, self.model)


# CONCATENATION IN METHODS

# Three methods:
# - Direct concatenation 
# - Add during initialisation
# - Add in the __init__ argument



# """

# class Employee(object):
#     def __init__(self, fname, lname, number, salary):
#         self.fname = fname
#         self.lname = lname
#         self.number = number 
#         self.salary = salary 

#     def printEmail(self):
#         print("This is my email address", self.fname + self.lname+ "@leedstrinity.ac.uk")

# Empy1 = Employee("Jon", "Doe", 1234, 2500)
# Empy1.printEmail()

# """


# """
# # Using the TV class, create a static method that prints the model of the TV

# class TV:
#     @staticmethod
#     def show_model():
#         print("Samsung Smart TV")

# TV.show_model()

# # Using the Employee class, introduce a global attitude, then use class method to change the attribute 

# class Employee:
#     company = "Trinity LTD."

#     @classmethod
#     def change_company(cls, new_company):
#         cls.company = new_company

#     print(Employee.company)
#     Employee.change_company("Leeds LTD.")

#     print(Employee.company)


# """
# ----- ARITHMETIC OVERLOADING -----

# OPERATOR OVERLOADING

# - Operator + used to add two integers 
# - joins two strings
# - merges two lists 

# i.e. 

# print(1+2) --> 3 
# print("Hello"+"World") --> HelloWorld

# DEFINE OPERATORS:
# - define a method for every operator  --> operator overloading
# - can overload all existing operators
# - can't create a new operator 


# -------- MAGIC METHODS / FUNCTIONS ---------

# 1) __add__ +
# 2) __sub__ - 
# 3) __mul__ *
# 4) __truediv__ /
# 5) __pow__ **

# (+) OPERATOR


# class Circle(object):
#    def __init__(self, area):
#       self.area = area
#    def __add__(self, other):
#       return(self.area + other.area)

# C1 = Circle(4)
# C2 = Circle(10)
# print("addition of 2 areas", C1 + C2)


# (-) OPERATOR

# class Circle(object):
#    def __init__(self, area):
#       self.area = area
#    def __sub__(self, other):
#       return(self.area - other.area)

# C1 = Circle(4)
# C2 = Circle(10)


# (/) OPERATOR

# class Circle(object):
#    def __init__(self, area):
#       self.area = area
#    def __truediv__(self, other):
#       return(self.area / other.area)

# C1 = Circle(4)
# C2 = Circle(10)


# (<) OPERATOR

# class Circle(object):
#    def __init__(self, area):
#       self.area = area
#    def __lt__(self, other):
#       return(self.area < other.area)

# C1 = Circle(4)
# C2 = Circle(10)

# """

# """

# --------- POLYMORPHISM IN OOP ----------

# - allows functions to use objects of any of these polymorphic classes
# - doesn't need to be aware of distinctions across the classes
# - 



# """
# class Shark(object):
#     def swim(self):
#         print("The shark is swimming.")

#     def swim_backwards(self):
#         print("The shark cannot swim backwards but can sink backwards.")

#     def skeleton(self):
#         print("The shark's skeleton is made of cartilage.")

# class Eelfish(object):
#     def swim(self):
#             print("The eelfish is swimming.")
            
#     def swim_backwards(self):
#         print("The eelfish can swim backwards.")

#     def skeleton(self):
#         print("The eelfish's skeleton is made of bones.")

# s1 = Shark()
# e1 = Eelfish()

# for fish in (s1, e1):
#     fish.swim()
#     fish.swim_backwards()
#     fish.skeleton()

# """
# ACTIVITY

# 1) data1 == data3  
#  data2 != data3    

# """

# # 2)

# k = 5 
# m = 2

# print(k & m)  #OUTPUT 0
# print(k | m)  #OUTPUT 7
# print(k ^ m)  #OUTPUT 7

# # 3


# y = 10
# z = 20

# mylist = [10, 2, 3, 4, 5]

# if y in mylist and z in mylist:
#     print("Both are in my list")
# else: 
#     print("Both are not in my list")

# print("happy new year")


# """
# --------------- WEEK 6 SESSION 1 -----------------

# --------------- EXTERNAL LIBRARIES ------------------

# - Regex / Regular Expression: 
#     - defines a pattern for searching / manipulating strings 
#     - can use a regex to match, search, replace and manipulate inside textual data 

# e.g.
# import re 
# word = 'possibility' 
# m = re.findall('s', word)
# print("Number of pattern in the word: ", len(m))
# print("The result of the regex matching",m)
# #findall returns a list of all s in the word


# =========== RE SPECIAL CHARACTERS AND SEQUENCE ============

# - \A matches pattern only at the start of the string 
# - \Z matches pattern only at the end of the string
# - \d matches to any digit- short for character classes [0-9]
# - \D matches to any non-digit - short for [^0-0]
# - \s matches any whitespace character - short for character class [\t\n\x0b\r\f]
# - \S matches any non-whitespace character - short for [^\t\n\x0b\r\f]
# - \w matches any alphanumeric character - short for character class [a-zA-Z_0-9]
# - \W matches any non-alphanumeric character - short for [^a-zA-Z_0-9]
# - \b matches the empty string BUT only at the beginning or end of a word. 
#    - matches a word boundary where a word character is [a-zA-Z0-9_]
# - \B opposite of a \b, matches empty string, but only when it is not at the beginning / end of a word 

# ============ REGEX METHODS ==============

# - re.compile('pattern')     = compiles regex pattern provided as a string into a re.pattern object
# - re.search(pattern,str)    = searches for occurrences of regex pattern inside target string, returns only the first match
# - re.match(pattern, str)       = matches regex pattern at start of string, returns a match only if pattern is located at beginning of string 
# - re.fullmatch(pattern, str)    = matches regex pattern to entire string
# - re.findall(pattern, str)     = scans regex pattern through entire string, returns all matches
# - re.finditer(pattern, str)   = scans regex pattern through entire string, returns an iterator yielding match objects   # watdatmean

# ==== RE: FULL MATCH ===

# - match regular expression pattern to the entire string from first-last char

# === RE: MATCH ANY CHARACTER ===

# - match any regex pattern at the start of the string

# === RE: SEARCH() ===

# - search for occurences of the regex pattern inside the target string and return only the first match

# === RE: SPLIT() ===

# - regex to split string on whitespaces

# === RE: SUB ===

# - regex for replacement, it replaces space with hyphen(-)


# """

"""

============== GRAPHICAL USER INTERFACE (GUI) =================

"""

import tkinter 

# window = tkinter.Tk()
# window.title("My first GUI programming")
# window.minsize(500,300)

# label = tkinter.Label(window, text="Scientists reveal the HI", font = ("Calibri 30 bold"))
# label.pack()

# button = tkinter.Button(window, text="Hi")
# button.pack()

# TextEntry = tkinter.Entry(window, width = 30).pack()
# checkButton = tkinter.Checkbutton(window, text ="Hi", bg = "pink", bd = 1)
# checkButton.pack()


# optionList = ["Scientists", "Reveal", "The", "Hi"]
# tkvar = tkinter.StringVar(window)
# tkvar.set("Select a country")
# tkinter.OptionMenu(window, tkvar, *optionList).pack()
            
# tkinter.Radiobutton(window,
#                     text= "Scientists",
#                     variable="house", 
#                     value= 1).pack()

# tkinter.Radiobutton(window,
#                     text= "Hi",
#                     variable="house", 
#                     value= 2).pack()

# scrollBar = tkinter.Scrollbar(orient=tkinter.VERTICAL,
#                               command=tkinter.Scrollbar.set).pack()

# frame = tkinter.Frame(window)
# frame.pack()

# bottomframe = tkinter.Frame(window)
# bottomframe.pack( side=tkinter.BOTTOM)

# pinkbutton = tkinter.Button(frame, text="HI", foreground= "pink")
# pinkbutton.pack( side = tkinter.LEFT)


# window.mainloop()



# CREATE A GUI SHOWING YOUR NAME AND YOUR NUMBER

# window = tkinter.Tk()
# window.title("DOXXING MYSELF")
# window.minsize(500,300)
# window.configure(bg= "blue")


# nameLabel = tkinter.Label(window, text= "Name",
#                           bg = "orange",
#                           foreground= "white")
# nameLabel.grid(row=0, column=1)
# nameEntry = tkinter.Entry(window)
# nameEntry.grid(row=0, column=2)


# numberLabel = tkinter.Label(window, text= "Number",
#                             bg= "orange",
#                             foreground= "white")
# numberLabel.grid(row=1, column=1)
# numberEntry = tkinter.Entry(window)
# numberEntry.grid(row=1, column=2)

# window.mainloop()
"""
=========== WEEK 7 SESSION 2 ============



"""

# import tkinter as tk
# window= tk.Tk()
# frame = tk.Frame(window)
# tk.Label(frame, text="Pack Demo of side and fill").pack()
# tk.Button(frame, text="A").pack(side=tk.LEFT, fill=tk.Y)

# tk.Button(frame, text="B").pack(side=tk.TOP, fill=tk.X)

# tk.Button(frame, text="C").pack(side=tk.RIGHT,fill=tk.NONE)

# tk.Button(frame, text="D").pack(side=tk.TOP, fill=tk.BOTH)

# tk.Label (window, text="Pack Demo of expand").pack()
# tk.Button(window, text="I do not expand").pack()
# tk.Button(window, text="I do not fill x but I expand").pack(expand = 1)

# tk.Button(window, text="I fill x and expand").pack(fill=tk.X, expand=1)


# frame.pack()

# window.mainloop()

# ======================================

# import tkinter as tk
# parent = tk.Tk()
# parent.title('Find & Replace')
# tk.Label(parent, text="Find:").grid(row=0, column=0, sticky='e')
# tk.Entry(parent, width=60).grid(row=0, column=1, padx=2, pady=2, sticky='we', columnspan=9)

# tk.Label(parent, text = "Replace:").grid(row=1, column=0, sticky= tk.W)
# tk.Entry(parent, width=60).grid(row=1, column =1, padx=2, pady=2, sticky= tk.W , columnspan =9)

# tk.Button(parent, text="Find").grid( row=0,
#                                      column=10, sticky='e' + 'w', padx=2, pady=2)
# tk.Button(parent, text="Find All").grid(row=1,
#                                          column=10, sticky='e' + 'w', padx=2
#                                          )

# tk.Button(parent, text="Replace").grid(row=2, column=10, sticky='e' + 'w', padx=2)
# tk.Button(parent, text="Replace All").grid(row=3, column=10, sticky='e' + 'w', padx=2)

# tk.Checkbutton(parent, text='Match whole word only').grid(row=2, column=1, columnspan=4, sticky='w')
# tk.Checkbutton(parent, text='Match Case').grid(row=3, column=1, columnspan=4, sticky='w')

# tk.Checkbutton(parent, text='Wrap around').grid(row=4,
#                                                  column=1, columnspan=4, sticky='w'
#                                                  )
# tk.Label(parent, text="Direction:").grid(row=2, column=6, sticky='w')
# tk.Radiobutton(parent, text='Up', value=1).grid(row=3,
#                                                  column=6, columnspan=6, sticky='w'
#                                                  )

# tk.Radiobutton(parent, text='Down', value=2).grid(row=3,
#                                                    column=7, columnspan=2, sticky='e'
#                                                    )

# root = tk.Tk()
# tk.Button(root, text="Absolute Placement").place(x=20, y=10)
# tk.Button(root, text="Relative").place(relx=0.8, rely=0.2, relwidth=0.5, width=10, anchor=tk.NE)
# root.mainloop()
                                          

# parent.mainloop()


"""
=============== WEEK 8 SESSION 1 ================
========= GRAPHICAL USER INTERFACE =========

---- ENTRY WIDGET ----

- basic Tkinter widgets used to get input from the user of an application 
- allows users to enter a single line of text

widget = Entry(master,opinion,...)



"""

# import tkinter as tk

# window = tk.Tk()
# tk.Label(window, text="First Name").grid(row=0)
# tk.Label(window, text="Last Name").grid(row=1)

# e1 = tk.Entry(window)
# e2 = tk.Entry(window)

# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)

# e1.insert(10, "John")
# e2.insert(10, "Doe")    # AUTOMATICALLY INSERTS NAME INTO LINES

# window.mainloop()

"""
---- EXAMPLE 2: GET METHOD ----

- Creates an application that will display the input text through a label widget 


"""

import tkinter as tk
# window = tk.Tk()

# def get_value():
#     e_text=entry.get()
#     #Label(window, text=e_text, font= ('Century 15 bold')).pack(pady=20)
#    #tk.Label(window, text=e1.get() + "\n"+ e2.get(), font= ('Century 15 bold')).grid(row=3,column=3)

# #Create an Entry Widget
# entry= tk.Entry(window,font=('Century 12'),width=40)
# entry.pack(pady= 30)

# #Create a button to display the text of entry widget

# button= tk.Button(window, text="Enter",command=get_value)
# button.pack()
# window.mainloop()

entry = tk.Entry(window, font=('Century 12'), width=40)
e2 = tk.Entry(window, font=('Century 12'), width=40)
entry.pack(pady=10)
e2.pack(pady=10)

def showDetails():
    fName = "First Name " + entry.get()
    Lname = "Last Name " + e2.get()
    fullName = fName + " " + Lname
    tk.Label(window, text=fullName).grid(row=4)

SButton = tk.Button(window, text='Show', command=showDetails)
SButton.grid(row=3, column=0, sticky=tk.W, pady=4)

QButton = tk.Button(window, text='Quit', command=window.quit)
QButton.grid(row=3, column=1, sticky=tk.W, pady=4)

window.mainloop()
