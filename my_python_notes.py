

# # print("Hello World")

# # #String concatenation
# # 'print("Angela" + " "+ "Yu")

# # #Fix the code bugs
# # print("Day 1 - String Manipulation")
# # print("String Concatenation is done with the" +  " +"   + " sign")
# # print('e.g. print("Hello" + "World"")')
# # print("New lines can be created with a backslash and n")

# # #Working with the input function 
# # #input will get user input in the console
# # #Then print() will print the word "Hello" and the user input
# # print("Hello " + input("What is your name?"))

# # #Printing the length of a string using the len() function
# # print("My name is", len(input("What is your name  ")), "characters long")

# # #Python Variables
# # #A variable is a container for storing data

# # name = input("what is your name?")
# # print(name)

# # name = "Angela"
# # length = len(name)
# # print(length)

# # #This code interchanges the values of a and b
# # a = input("a:  ")
# # b = input("b:  ")

# # c = a

# # a = b

# # b = c

# # #This code is achieves the came result but what if they are immiscible?
# # c = a + b
# # a =str(c-a)
# # b =str( c-b)

# # print("a =  " + a)
# # print("b =  " +  b)

# # #--------------------------------------------------------------------------------------------------------------------------
# # #--------------------------------------------------------------------------------------------------------------------------
# # #Rules for naming variables
# # #Make your code readabler
# # #Underscores sepearate multiple words in a variable name
# # #No numbers or special characters at the beginning of a variable name
# # #No special charaters in a variable name with the exception of an underscore
# # #Do not use built in functions as variable names
 
 


# # #Day 2 Notes

# # #--------------------------------------------------------------------------------------------------------------------------
# # #    Data Types, Numbers, Operations, Type conversion, f-strings
# # #--------------------------------------------------------------------------------------------------------------------------
 
# # #Data Types
 
# #  #Strings
# # print( "Hello"[4])  #This is called Subscripting
# # print("123" + "345")
 
# #  #Integers---all whole numbers, +ve or -ve
 
# # print(123 + 345)
 
# #  #Large numbers that require commas as in finance are written with underscore(s), _ between them

# #  #Float---numbers with decimal points-decimal points flow around a number
 
# # print(3.14159)

# # #Boolean--true and false valus

# # True
# # False


# # #Type Error, Type check, Type conversion or Type casting

# # #You can't concatenate dissimilar data type'
# # num_char = len(input("What is your name?"))
# # print(type(num_char))
# # #print("Your name has " + num_char + "characters")

# # a = float(123)

# # print(type(a))

# # print(float(40) + int(100))


# # #Mathematical Operators in Python

# # 3 + 5

# # 7 - 4

# # 3 * 2

# # 6 / 3  #returns a float by default

# # 2 ** 3

# # #Priority of operations

# # #PEMDAS L-R
# # #  ()
# # #  **
# # #  * /
# # #  + -


# # print(3*(3+3)/3-3)




 
# # #Rounding numbers

# # print(round(9/2.9, 3))
 
# # print(round(2.666666666, 2))

# # print(8 // 3) #returns an integer

# # print(8 / 3) #returns floating point number
 
# # result = 4 / 2
 
# # result /=2
 
# # print(result)
 
 
# #  #Updating the value of a variable---manipulating a value based on the previous value

# # score = 0

# # # User scores a point
 
# # score +=1
# # score -=1
# # score  /=1
# # score *=1
# # score +=1
# # #instead of 
# # #score = score + 1
# # print(score)

# # #Working with f-Strings---makes it easy to mix strings and different data types

# # score = 0
# # height = 1.8
# # isWinning = True

# # print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")






# # #Day 3
# # #-----------------------------------------------------
# # #if-else statements
# # #Nested if statements and elif statements

# # #Modulo 

# # number = int(input("Enter a number:  "))

# # if number % 2 == 0:
# # 	print("This is an even number")
# # else:
# # 	print("This is an old number")





# # #Multiple if-else statements




# # #Logical Operators
# # # and --both conditions have to be true
# # # or -- only one of the conditions have to true
# # # not --reverses a condition


	

# # #Randomization
# # #Using the random module

# # #Python uses the -----Mersenne-Twister------- to generate random numbers.
 
# # #AskPython.com conains the explanation to all python modules modules

# # import random
# # import my_module
# # random_integer = random.randint(1, 10)
# # print(random_integer)
# # print(my_module.pi)

# # random_float = random.random()
# # rounded_value = round

# # #31-12-2025

# # #Lists---Used to store related piece of data in an orderly manner

# # fruits = ["Apple", "Perl", "Cherry"]

# # print(fruits)
# # print(fruits[0])
# # print(fruits[-1])
# # fruits.append("Mango")
# # print(fruits)

# # 02/01/2026

# # Nested lists are common in python.
# # One common error you might come across when dealing with lists is "list index out of range."

# # fruits = ["mango", "Orange", "Banana"]
# # vegetables = ["Spinach", "Tomatoes", "Potatoes"]

# # dirty_dozen = [fruits, vegetables]
# # print(dirty_dozen)

# #08/01/2026

# #Functions--python has a wide range of built-in funactions--check the python documentation

# # A function can be identified by the its name and parenthesis e.g print(), len(), int(), str(), input(), count(), sample(), choices(), sum().

# #This how you write a function: we define the function using the def keyword, followed by a name
# # What differentiates a function from a variable is the parenthesis
# # A function will remain dormant when executed unless it is triggered or call later on in the code. You can define a function and call it any time you have need of it in the code.
# # To call the function, type the name of the function followed by parenthesis and add the input if need be.
# # After a function is called, the computer knows how to go and carry out all the instructions encompassed within the fuction.
# #

# # # Defining Fuctions
# # def my_function():
# #     #Do this
# #     print("Hello")
# #     #Then do this
# #     print("Bye")
# # #Calling Functions
# # my_function()

# # # 10/01/2026
# # # Indentation--It is very important in python. It defines the scope of a particular program.

# # # Indentatation in practice
# # def my_function():
# #     a = 5
# #     b = 6
# #     print(a)
# #     print(b)
# # my_function()

# # # a and b are on the same level of indentation
# # # my_function() and a/b are not on the same level of indentation
# # # some people prefer spaces over files. in python3, you can't even mix spaces and tabs in your code.
# # # Spaces are preferable. 
# # # The default number of spaces for indentation in python is 4 spaces or 4 dots.

# # while-loops - It continues as long as a condition is true

# # Use cases of for-loop
# # Looping through a list of items
# # Creating a range of  values and working on them

# # while something_is_true:
# #     Do this
# #     Then do this
# #     Then do this

# # When do we use for-loop or while-loop?

# # for-loop is great when you are iterating over something and you want to perform an action on every element in that thing. You also use a for-loop when you are iterating over a range of values

# # You use a while-loop when you don't care what number in a sequence you are in, which item you are iterating through in a list and you just simply want to carry out some functionality many times until some sort of condition set.

# # while-loops are a little more dangerous than for-loops in that in for-loops, you actually set the number of times you want your code to run in advance, while-loops run as long as a condition is true. If you have a condition that doesn't actually evaluates to false, it'll continue to run without breaking potentially crashing your device. It becomes an infinite loop.

# # 12/01/2026

# # Hangman program

# # "python for education" by google is a great resources

# #13/01/2026
# # It is important to note that while loops require a change in the loop to tell it that the condition has reached.

# # #For example: The code below is an infinite loop
# # end_of_game = False
# # for i in range(0, 200):
# #     print(i)
# #     while not end_of_game:
# #         if i == 100:
# #             end_of_game = True
# #         print(i)

# #20/01/2026

# # fUNCTIONS WITH INPUT
# # ARGUMENTS AND PARAMETERS

# # -- FUNCTIONS are a handy way of taking a complex set of instructions and packaging them together inside a block of code that has a name given to it.

# # --we call the function when we have need of it.

# # Review:
# # Create a function called greet()
# # def greet():
# #     #Write 3 print statements inside the function
# #     print("Good morning")
# #     print("Good afternoon")
# #     print("Good evening")
# # #Call the greet() function and run your code
# # greet()

# # We can add the name of a variable inside the parenthesis of the function name.

# # We can also create a function that allows for input
# # 
# # def my_function(something):
# #     #Do this with something
# #     #Then do this
# #     # And finally do this

# # differences between round() and math.ceil()
# # --Use round() when you want to perform proper approximations--it will round it up or down based on the approximation rules. You can also specify the number of decimal places but the same rule applies

# # e.g. 5.4 will appr. to 5, 5.5 -- 6

# # --Use math.ceil when you want to force a decimal value to approximate to the immediate higher number.

# #e.g. 5.1, 5.2 5.4 ... will all appr. to 6

# # 21/01/2026
# # Functions continued

# # CAESAR CIPHER

# # To get the index of a paricular letter in a list of alphabets, use the list_name.index(letter)

# # 27/01/2027

# # Dictionaries and Nested Lists

# # Every dictionary has two parts to it: key and values

# # dictionary:

# # {key:value} -- the key goes first followed by the value

# # A good practice in python when working with a dictionary is to add the key-values on new lines.
# # Remember to add a comma at the end of the keyt-values

# # programming_dictionary = {
# #     "Bug": "An error in a program that prevents the program from running as expected",
# #     "Function": "A piece of code that you can easily calol over and over again",
# # }

# # Retrieving an element of a dictionary
# # You use a key to indicate the item you wanted to retrieve
# # # The keys are mostly strings
# # print(programming_dictioonary["Bug"])

# # Adding new items to dictionary

# # programming_dictioonary["Loop"] = "The action of doing something over and over again"

# # print(programming_dictioonary)
# # print(programming_dictioonary["Bug"])

# # As good practice, it is always better to start with an empty dictionary
# # empty_dictionary = {}

# # # Wipe an existing dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)

# # You can add items to the empty dictionary by using the method of adding elements into a dictionary

# # programming_dictionary["Loop"] = "The action of doing something over and over again"

# # print(programming_dictionary)

# # # Edit an item in a dictionary
# # # If it finds a key of that name, it will modify it's value; if not, it will be appended at the end of the dictionary
# # programming_dictionary["Bug"] = "A moth in your computer."
# # print(programming_dictionary)

# # Looping through a dictionary
# # for key in programming_dictionary:
# #     print(f"{key}: {programming_dictionary[key]}")

# # NESTING LISTS AND DICTIONARIES
# # Sometimes we may decided given the data to be worked on to use dictionaries or lists as the values of keys in dictionaries -- nesting of lists or dictionaries into a dictionary.

# # capitals = {
# #     "France": "Paris",
# #     "Germany": "Berlin"
# # }

# # # Nesting a List in a Dictionary

# # travel_log = {
# #     "France": ["Paris", "Lille", "Dijon"],
# #     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# # }

# # print(travel_log["France"])
# # # Nesting Dictionary in a Dictionary 

# # travel_log = {
# #     "France": {"cites_visited": ["Paris", "Lille", "Dijon"], "total_visits": 14},
# #     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
# # }

# # # Nesting a dictionary in a List

# # travel_log = [
# #     {
# #         "country": "France", 
# #         "cites_visited": ["Paris", "Lille", "Dijon"], 
# #         "total_visits": 14
# #     },
# #     {
# #         "country": "Germany", 
# #         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
# #         "total_visits": 5
# #     },
# # ]

# # print(travel_log[0])

# # 02/02/2026

# # FUNCTIONS WITH OUTPUTS

# # def my_function():
# #     result = 3 * 2
# #     return result
# # Here the return keyword is the output keyword
# # When something is returned in a function, it replaces the function call and becomes the output that can either be printed directly or saved to a variable for later use. 
# # Any code written in a function after the return function never executes.
# # The return keyword is also very helpful in flow control to catch errors and avoid repetions of code where necessary 

# # 04/02/2026

# # DOCSTRINGS
# # They are ways of creating a little bit of documentations as we code along
# # We use three quotations marks
# # Note that the three quotation marks can also be used to write a multi-line comment.
# # The official python guidance is to avoid multi-line comments using 3 quotes. It is safer and less confusing to write multi-line comments on different lines and then comment the lines individually

# #05/06/2026

# # Difference between print() and return

# # A print() function when used in a function does not allow for use of that function as the input of another function.

# # On the other hand, the return keyword enables us to use the output of one function as the input of another function.

# # It can be compared to the pipe | symbol in Linux

# #07/02/2026

# # RECURSION
# # Recursion is the idea that you can have a function call itself

# # USE CASE
# # It takes no input and output
# # def recursive_function():
# #     #Do something
# # #We call the recursive function so that it could find the place where it was defined and carry out all of the instructions therein.
# # recursive_function()

# # Notes:
# # When using a recursive function with a while loop, care should be taken to avoid infinite loops. It's always a good practice to use recursive functions with a condition.

# #08/02/2026

# # Black Jack game


# import random
# def deal_card():
#     """Returns a random card from the deck"""
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     #Pick a random card
#     card = random.choice(cards)
#     return card


# # Deal the user and computer 2 cards each using deal_card()

# user_cards = []
# computer_cards = []

# for _ in range(2):
#     # new_card = deal_card()
#     # user_cards.append(deal_card)
#     user_cards.append(deal_card)

#     # A wrong way of getiing the cards

#     new_card = deal_card # What is returned here is an integer
#     user_cards += new_card #This line of code is shorthand for:
#     user_cards.extend(new_card) # Whatever you put in the parenthesis of the extend function has to be a list.

#     # It show the erroe message: TypeError: 'function' object is not iterable