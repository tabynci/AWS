# 2-1. Simple Message: Store a message in a variable, and then print that 
# message.

# message= 'we are giving hope to others'
# print(message)


# 2-2. Simple Messages: Store a message in a variable, and print that message.
# Then change the value of your variable to a new message, and print the new 
# message.

# message= 'we are giving hope to others'
# print(message)
# msg=message
# print(msg)

# 2-3. Personal Message: Store a person’s name in a variable, and print a message to that person. Your message should be simple, such as, “Hello Eric, 
# would you like to learn some Python today?”


# message= 'Zaki'

# print(f"Hello {message}, would you like to learn python ")

# 2-4. Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase.


# message= 'zaki'

# print(f"Hello {message.title()}, would you like to learn python")

# Message= 'ZAKI'
# print(f"{Message.lower()}")
# print(f"{message.upper()}")

# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the 
# quote and the name of its author. Your output should look something like the 
# following, including the quotation marks:
# Albert Einstein once said, “A person who never made a 
# mistake never tried anything new.”

# msgs= 'Tabasum once said, “A person who never made a mistake never tried anything new.”'
# print(msgs)

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous person’s name in a variable called famous_person. Then compose your message 
# and store it in a new variable called message. Print your message.

# famous_person= 'Zaki'
# message=print(f'{famous_person} "once said A person who never made a mistake never tried anything new"')
# print(message)

# 2-7. Stripping Names: Store a person’s name, and include some whitespace 
# characters at the beginning and end of the name. Make sure you use each 
# character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(), 
# rstrip(), and strip().


# txt = '          taqi              ' 

# print(f'\n{txt.rstrip()}')
# print(f'{txt.lstrip()}')
# print(f'\t{txt.lstrip()}')

# test ='   zaki   '
# print(f'{test.strip()}')


# 2-8. Number Eight: Write addition, subtraction, multiplication, and division 
# operations that each result in the number 8. Be sure to enclose your operations 
# in print statements to see the results. You should create four lines that look 
# like this:
# print(5 + 3)


# print(2+3)
# print(5-2)
# print(4*2)
# print(8/2)


# 2-9. Favorite Number: Store your favorite number in a variable. Then, using 
# that variable, create a message that reveals your favorite number. Print that 
# message.


# number= 23
# message = "this is my favorite" + str(number)
# print(message)
# print(f"this is my {number}")

# 2-10. Adding Comments: Choose two of the programs you’ve written, and 
# add at least one comment to each. If you don’t have anything specific to write 
# because your programs are too simple at this point, just add your name and 
# the current date at the top of each program file. Then write one sentence 
# describing what the program does.

# Say hello to every one

# This is  2-10 lab we were doing



# import datetime
# today= datetime.date.today()
# print(today)

# number= 23
# message = "this is my favorite" + str(number)
# print(message)
# print(f"this is my {number}")

# 2-11. Zen of Python: Enter import this into a Python terminal session and skim 
# through the additional principles.

# import this

# 3-1. Names: Store the names of a few of your friends in a list called names. Print
# each person’s name by accessing each element in the list, one at a time.

# names= ['taby', 'deepi', 'manoj', 'radhika', 'kritika']


# print(names[1])
# print(names[2])
# print(names[3])

# extra
# for name in names:
#     print(f'{name}')


# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each mes-
# sage should be the same, but each message should be personalized with the
# person’s name.


# names= ['taby', 'deepi', 'manoj', 'radhika', 'kritika']


# print("hello",names[0])
# print("hello",names[1])
# print("hello"+names[2])
# print("hello"+names[3])

# alternate methjod
# message = "hello " + names[0].title()
# print(message)

# for name in names:
#     print(f'\t{name}')

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”

# list=['bmw', 'ferrari', 'honda']

# print("I would like to own a "+list[0])
# print("I would like to own a "+list[1])
# print("I would like to own a "+list[2])

# print(f'I would like to {list}')

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.

# Guest_list= ['dada', 'tata', 'rere', 'reer']

# print(f' you are invited to party {Guest_list[1]}')

# print(f' you are invited to party  {Guest_list[3]}')

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print statement at the
# end of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still
# in your list.

# Guest_list= ['dada', 'tata', 'rere', 'reer']

# print(f"{Guest_list[0]} cannot attend aprty")
# Guest_list[0]='janana'
# # Guest_list.remove('dada')


# # print(Guest_list[1]+"you are in party list")
# # print(Guest_list[2]+"you are in party list")
# # print(Guest_list[3]+"you are in party list")

# for guest in Guest_list:
#     print(guest+"you are invited for party")


# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.


# Guest_list= ['dada', 'tata', 'rere', 'reer']
# print(Guest_list)

# Guest_list.insert(0, 'mena')
# Guest_list.insert(1, 'lena')
# Guest_list.insert(2, 'hena')
# Guest_list.insert(8, 'shena')
# Guest_list.append('jena')
# print(Guest_list)


# print(f'{Guest_list[0]} You are all invited for the aprty') 
# print(f'{Guest_list[1]} You are all invited for the aprty') 
# print(f'{Guest_list[2]} You are all invited for the aprty') 
# print(f'{Guest_list[3]} You are all invited for the aprty') 
# print(f'{Guest_list[4]} You are all invited for the aprty') 
# print(f'{Guest_list[5]} You are all invited for the aprty') 

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.


# Guest_list= ['dada', 'tata', 'rere', 'reer', 'tere', 'uni']
# print(Guest_list)

# print("Only two people can be invited for dinner.")
# Guest_list.pop(0)
# print(f'{Guest_list[0] } sorry you cannot invited')
# print(f'{Guest_list[2] } sorry you cannot invited')

# del Guest_list[0]
# del Guest_list[1]

# print(Guest_list)

# print(f"{Guest_list} peeple left")
# Guest_list.remove('uni')
# print(f'{Guest_list}, only two people left')


# del Guest_list[0]
# print(Guest_list)
# del Guest_list[0]
# print(Guest_list)


# Extra
# Guest_list.append('ayu')
# print(Guest_list)


# 3-8. Seeing the World: Think of at least five places in the world you’d like to
# visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.
# • Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.
# • Use sorted() to print your list in alphabetical order without modifying the
# actual list.
# • Show that your list is still in its original order by printing it.

# • Use sorted() to print your list in reverse alphabetical order without chang-
# ing the order of the original list.

# • Show that your list is still in its original order by printing it again.
# • Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
# • Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.
# • Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.
# • Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.


# List =['india', 'china', 'mumbai', 'donlaighure', 'antartica']
# print(List)

# print(sorted(List))
# # It reverse the original list 
# List.reverse()
# print(List)
# List.reverse()
# print(List)

#  Use sort() to change your list so it’s stored in alphabetical order. Print the
# # list to show that its order has been changed.

# List.sort()
# print(List)
# • Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.

# List.sort(reverse=True)
# print(List)

# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (page 46), use len() to print a message indicating the number
# of people you are inviting to dinner.



# List =['india', 'china', 'mumbai', 'donlaighure', 'antartica']
# print(len(List))


# 3-10. Every Function: Think of something you could store in a list. For example,

# you could make a list of mountains, rivers, countries, cities, languages, or any-
# thing else you’d like. Write a program that creates a list containing these items

# and then uses each function introduced in this chapter at least once.

# List_mountains = ['himalyan', 'mount_evert', 'mount abu', 'abbu']

# print(len(List_mountains))
# List_mountains.append('Taby')
# print(List_mountains)
# List_mountains.remove('Taby')

# print(List_mountains)

# print(sorted(List_mountains))

# print(List_mountains)

# print(List_mountains.sort())

# print(List_mountains)

# List_mountains.insert(0, 'Tabys')
# print(List_mountains)

# List_mountains.pop(0)
# print(List_mountains)

# print(List_mountains[-1])


# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.
# • Modify your for loop to print a sentence using the name of the pizza
# instead of printing just the name of the pizza. For each pizza you should
# have one line of output containing a simple statement like I like pepperoni
# pizza.
# • Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!

# pizza_list= ['tomato_pizza', 'spinach_pizza', 'margarita_pizza']
# for pizza in pizza_list:
#     print(f'\n i love {pizza}')

# print('How much you lik3e pizza ')


# 4-2. Animals: Think of at least three different animals that have a common char-
# acteristic. Store the names of these animals in a list, and then use a for loop to

# print out the name of each animal.
# • Modify your program to print a statement about each animal, such as
# A dog would make a great pet.
# • Add a line at the end of your program stating what these animals have in
# common. You could print a sentence such as Any of these animals would
# make a great pet!


# Animals= ['Dog', 'Cat', 'Lion', 'Tiger']

# for animal in Animals:
#     print(f'A {animal} would make a great pet')
# print('I love dog and cats')

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive.



# for value  in range(1, 21):
#     print(f'{value}')


# Extra
# number= []
# for value  in range(1, 21):
#     print(f'{value}')
#     number.append(value)
# print(number)

# squares =[]

# for value in range(1, 11):
#     square = value**2
#     squares.append(square)
#     print(square)


# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.)

# for value in range(1, 1000):
#     print(value)

# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.

# numbers = list(range(1,10000001))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# 4-6. Odd Numbers: Use the third argument of the range() function to make a list
# of the odd numbers from 1 to 20. Use a for loop to print each number.

# odd_numbers= list(range(1, 21, 3))
# print(odd_numbers)

# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.
# number =3
# for i in range(1, 11):
#     print(f'{number} * {i}={number}')


# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.

# for value in range(1, 10):
#     cube= value**3
#     print(cube)


# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes.


# cube = [value**3 for value in range(1, 10)]
# print(cube) 


# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# • Print the message, The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
# • Print the message, Three items from the middle of the list are:. Use a slice
# to print three items from the middle of the list.
# • Print the message, The last three items in the list are:. Use a slice to print
# the last three items in the list.



#  • Print the message, The first three items in the list are:. Then use a slice to
# # print the first three items from that program’s list.

# List_mountains = ['himalyan', 'mount_evert', 'mount abu', 'abbu', 'himu', 'timu', 'hiids']

# print(List_mountains[:])

# print(List_mountains[:3])


# • Print the message, Three items from the middle of the list are:. Use a slice
# # to print three items from the middle of the list.

# print(List_mountains[2: 4:])

# • Print the message, The last three items in the list are:. Use a slice to print
# # the last three items in the list.


# print(List_mountains[4:])


# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 
# (page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
# •	 Add a new pizza to the original list.
# •	 Add a different pizza to the list friend_pizzas.
# •	 Prove that you have two separate lists. Print the message, My favorite 
# pizzas are:, and then use a for loop to print the first list. Print the message, 
# My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.



# pizza_lists= ['tomato_pizza', 'spinach_pizza', 'margarita_pizza']

# friend_pizzas =pizza_lists[:]

# pizza_lists.append('potato')
# print(pizza_lists)

# friend_pizzas.append('chiili_pizza')
# print(friend_pizzas)

# for pizza_List in pizza_lists:
#     print(pizza_List)

# for freind_pizza in friend_pizzas:
#     print(freind_pizza)

# 4-12. More Loops: All versions of foods.py in this section have avoided using 
# for loops when printing to save space. Choose a version of foods.py, and 
# write two for loops to print each list of foods.


# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]
# # print("My favorite foods are:")
# # print(my_foods)
# # print("\nMy friend's favorite foods are:")
# # print(friend_foods)


# for food in my_foods:
#    print(food)
#    break

# for food in friend_foods:
#     print(food)

# extra

# for food in my_foods:
       
#    food='res'
#    my_foods.append(food)
#    print(food)
#    break





# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five 
# simple foods, and store them in a tuple.
# •	 Use a for loop to print each food the restaurant offers.
# •	 Try to modify one of the items, and make sure that Python rejects the 
# change.
# •	 The restaurant changes its menu, replacing two of the items with different 
# foods. Add a block of code that rewrites the tuple, and then use a for
# loop to print each of the items on the revised menu.



# Instead of list saqure  bracket we are using parenthesis

# Buffet=('chicken fry', 'dum allo', 'gobi', 'biryani', 'chicken gravy')

# for food in Buffet:
#    print(food)


# •	 Try to modify one of the items, and make sure that Python rejects the 
# change.
# Buffet[0]='fish'

# Buffet.append('fish')

# Buffet=('Mutton fry', 'dum allo', 'gobi', 'biryani', 'chicken fry')


# for food in Buffet:
#    print(food)


# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement 
# describing each test and your prediction for the results of each test. Your code 
# should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')

# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')

# car = 'Mw'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'aud'? I predict False")


# Car_list=['BMW', 'Subaru', 'audi', 'ferrari', 'toyota']

# for car in Car_list:
#     if car =='BMW':
#         print(car == 'BMW')

# for car in Car_list:
#     if car !='BMW':
#         print(car == 'BMW')


# 5-2. More Conditional Tests: You don’t have to limit the number of tests you 
# create to 10. If you want to try more comparisons, write more tests and add 
# them to conditional_tests.py. Have at least one True and one False result for 
# each of the following:
# •	 Tests for equality and inequality with strings
# •	 Tests using the lower() function
# •	 Numerical tests involving equality and inequality, greater than and 
# less than, greater than or equal to, and less than or equal to
# •	 Tests using the and keyword and the or keyword
# •	 Test whether an item is in a list
# •	 Test whether an item is not in a lis

# bike = 'bmx'
# if bike=='bmx':
#     print("\nbike=='bmx'? I predict True")

# car ='BMW'
# print(car.lower() == 'bmw')

# car ='Tesla'
# print(car!='Tesla')

# age=23
# print(age>34)

# print(age==23)
# print(age!=23)

# print(age<=23)
# print(age>4)
# print(age<2)

# age=23
# name='taby'
# print(age== 23 and name=='taby')

# my_foods = ['pizza', 'falafel', 'carrot cake']


# # print('pizza' in my_foods)

# print('choloate' not in  my_foods)

# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a 
# variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# •	 Write an if statement to test whether the alien’s color is green. If it is, print 
# a message that the player just earned 5 points.
# •	 Write one version of this program that passes the if test and another that 
# fails. (The version that fails will have no output.)


alin_color=['green', 'yellow', 'red']

# if 'green' in alin_color:
#     print('player earned 50 pints')



# if 'blue ' in alin_color:
#     print('player is not there')

# Extra
# alin_color=['green', 'yellow', 'red']

# if 'green' in alin_color:
#     print('player earned 50 pints')
# elif 'yellow' in alin_color:
#     print('player earned 500 pints')
# elif 'blue'  not in alin_color:
#     print('player is not there')
# else:
#     print("player is not there")


# extra
# for alien in alin_color:
#     if alien == 'green':
#         print('f {alien} just earned 5 points')


# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.
# •	 If the alien is green, print a message that the player earned 5 points.
# •	 If the alien is yellow, print a message that the player earned 10 points.
# •	 If the alien is red, print a message that the player earned 15 points.
# •	 Write three versions of this program, making sure each message is printed 
# for the appropriate color alien

# if 'green' in alin_color:
#     print('player earned 50 pints')
# elif 'yellow' in alin_color:
#     print('player earned 500 pints')
# elif 'blue'  not in alin_color:
#     print('player is not there')
# else:
#     print("player is not there")


# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s 
# stage of life. Set a value for the variable age, and then:
# •	 If the person is less than 2 years old, print a message that the person is 
# a baby.
# •	 If the person is at least 2 years old but less than 4, print a message that 
# the person is a toddler.
# •	 If the person is at least 4 years old but less than 13, print a message that 
# the person is a kid.
# •	 If the person is at least 13 years old but less than 20, print a message that 
# the person is a teenager.
# •	 If the person is at least 20 years old but less than 65, print a message that 
# the person is an adult.
# •	 If the person is age 65 or older, print a message that the person is an 
# elder.


# age= 23

# if age<2:
#     print('person is a baby')
# elif age>=2 and age<4:
#     print('the person is toddler')
# elif age>=4 and age < 13:
#     print('Kid')
# elif age>=13  and age<20:
#     print('teenager')
# elif age>20 and age<65:
#     print('adult')
# elif age>65:
#     print('elder')
# else:
#     print('invalid entry')

# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of 
# independent if statements that check for certain fruits in your list.
# •	 Make a list of your three favorite fruits and call it favorite_fruits.
# •	 Write five if statements. Each should check whether a certain kind of fruit 
# is in your list. If the fruit is in your list, the if block should print a statement, 
# such as You really like bananas!

# favorite_fruits= ['apple', 'Banana', 'orange', 'grapes', 'mango']

# if 'apple'  not in favorite_fruits:
#     print('apple is in list')
# elif 'banana'.title() in favorite_fruits:
#     print('banana in a list')

# 5-8. Hello Admin: Make a list of five or more usernames, including the name 
# 'admin'. Imagine you are writing code that will print a greeting to each user 
# after they log in to a website. Loop through the list, and print a greeting to 
# each user:
# •	 If the username is 'admin', print a special greeting, such as Hello admin, 
# would you like to see a status report?
# •	 Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.

# Person_list=['admin', 'taby', 'zaki', 'taqi', 'deepi']

# for name in Person_list:
#     if name == 'admin':
#         print(f"'Hello' {name}")
#     elif name == 'taby':
#         print(f"Hello {name}, thank you for logging in again")
#     elif name == 'zaki':
#         print(f"Hello {name}, thank you for logging in again")
#     elif name == 'taqi':
#         print(f"Hello {name}, thank you for logging in again")
#     elif name == 'deepi':
#         print(f"Hello {name}, thank you for logging in again")

# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is 
# not empty.
# •	 If the list is empty, print the message We need to find some users!
# •	 Remove all of the usernames from your list, and make sure the correct 
# message is printed.


# Person_list=['admin', 'taby', 'zaki', 'taqi', 'deepi']
# Person_list=[]

# if Person_list:
#     for persson in Person_list:
#         if persson not in Person_list:
#             print("Added "  + {persson})
# else:
#     print("list is empty")
# for name in Person_list:
#     if name != '' :
#         print(f"'add user ' {name}")
#         Person_list.remove('admin')




# 5-10. Checking Usernames: Do the following to create a program that simulates 
# how websites ensure that everyone has a unique username.
# •	 Make a list of five or more usernames called current_users.
# •	 Make another list of five usernames called new_users. Make sure one or 
# two of the new usernames are also in the current_users list.
# •	 Loop through the new_users list to see if each new username has already 
# been used. If it has, print a message that the person will need to enter a 
# new username. If a username has not been used, print a message saying 
# that the username is available.
# •	 Make sure your comparison is case insensitive. If 'John' has been used, 
# 'JOHN' should not be accepted.


# current_users=['taqi', 'taby', 'deep', 'farid', 'dari', 'tren']
# new_users=['deep', 'xan', 'van', 'taby', 'zak']

# for user in new_users:
#     if user.lower() in current_users:
#         print(f'{user}+" will need to enter"')
#     else:
#         print('user is not available')

# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such 
# as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
# •	 Store the numbers 1 through 9 in a list.
# •	 Loop through the list.
# •	 Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 
# 7th 8th 9th", and each result should be on a separate line.


# Ordinal_Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for number in Ordinal_Numbers:
#     if number == 1:
#         print("\n", str(number)+"st")
    
#     elif number == 2:
#         print("\n", str(number)+"nd")
#     elif number == 3:
#         print("\n", str(number)+"rd")
#     else:
#         print( str(number)+"th")    

# 5-12. Styling if statements: Review the programs you wrote in this chapter, and 
# make sure you styled your conditional tests appropriately

# N/A

# 5-13. Your Ideas: At this point, you’re a more capable programmer than you 
# were when you started this book. Now that you have a better sense of how 
# real-world situations are modeled in programs, you might be thinking of some 
# problems you could solve with your own programs. Record any new ideas you 
# have about problems you might want to solve as your programming skills continue to improve. Consider games you might want to write, data sets you might 
# want to explore, and web applications you’d like to create.


# N/A


                                # Dictionary

# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You 
# should have keys such as first_name, last_name, age, and city. Print each 
# piece of information stored in your dictionary.

# Person ={'first_name':'taby', 'last_name':'kouser', 'age':34, 'city':'London'}
# print("first name:"+Person['first_name'])
# print("second name:"+Person['last_name'])
# print("age:"+str(Person['age']))
# print("city: "+Person['city'])

# print(Person)

# print(Person.keys())

# print(Person.values())
# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite 
# number for each person, and store each as a value in your dictionary. Print 
# each person’s name and their favorite number. For even more fun, poll a few 
# friends and get some actual data for your program.


# favorite_number= {'taby':1, 'zaki':2, 'tamanna':3, 'tr':5, 'ren':3}



# for key, value in favorite_number.items():
#     print(f"\nkey: " +key)
#     print(f"\nvalue:" + str(value))

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# •	 Think of five programming words you’ve learned about in the previous 
# chapters. Use these words as the keys in your glossary, and store their 
# meanings as values.
# •	 Print each word and its meaning as neatly formatted output. You might 
# print the word followed by a colon and then its meaning, or print the word 
# on one line and then print its meaning indented on a second line. Use the 
# newline character (\n) to insert a blank line between each word-meaning 
# pair in your output.
# Looping Through a Dictiona

# glossary = {'Object':'Instance of a class', 
#             'class' : 'collection of objects',
#               'string' :'collection of characters',
#               'tuple':'immutable collection of constants',
#               'list':'mutable collection of constants'}
# #print(glossary.keys())
# #print(glossary.values())
# print("Object : \n")
# print("\t" + glossary['Object'])
# print("class : \n")
# print("\t" + glossary['class'])
# print("string : \n")
# print("\t" + glossary['string'])
# print("tuple : \n")
# print("\t"+ glossary['list'])


# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean 
# up the code from Exercise 6-3 (page 102) by replacing your series of print
# statements with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your 
# glossary. When you run your program again, these new words and meanings 
# should automatically be included in the output.

# glossary = {'Object':'Instance of a class', 
#             'class' : 'collection of objects',
#               'string' :'collection of characters',
#               'tuple':'immutable collection of constants',
#               'list':'mutable collection of constants'}
# for key,value in glossary.items():
#     print(f"{key}:\n \t{value}\n")

# 6-5. Rivers: Make a dictionary containing three major rivers and the country 
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# •	 Use a loop to print a sentence about each river, such as The Nile runs 
# through Egypt.
# •	 Use a loop to print the name of each river included in the dictionary.
# •	 Use a loop to print the name of each country included in the dictionary


# Rivers={'Ganga':'India', 'Jamuna':'Indai', 'Nile':'Egypt'}


# for key, value in Rivers.items():
#     print(f'{key} runs through in {value}')

# for key in Rivers:
#     print(f'River : {key}')
# for value in Rivers:
#     print(f'River : {value}')

# 6-6. Polling: Use the code in favorite_languages.py (page 104).
# •	 Make a list of people who should take the favorite languages poll. Include 
# some names that are already in the dictionary and some that are not.
# •	 Loop through the list of people who should take the poll. If they have 
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take 
# the poll



# favorite_languages = {
#  'jen': 'python',
#  'sarah': 'c',
#  'edward': 'ruby',
#  'phil': 'python',
#  }

# friend_List=['taby', 'sarah']

# for name in friend_List:
#     if name in favorite_languages.keys():
#         print(name.title() +"Thank you for responding")
#     else:
#         print(name.title()+"Please the take poll")



# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three 
# dictionaries in a list called people. Loop through your list of people. As you 
# loop through the list, print everything you know about each person.

# AsianPeople={'name':'Zaki', 'age':3, 'mobile':9023321231}
# Egyptpeople={'name':'Taki', 'age':3, 'mobile':9023321231}
# USApeople={'name':'Naki', 'age':3, 'mobile':9023321231}
# PeoplesList= [AsianPeople, Egyptpeople, USApeople]

# for people in PeoplesList:
#     print(people)



# 6-8. Pets: Make several dictionaries, where the name of each dictionary is the 
# name of a pet. In each dictionary, include the kind of animal and the owner’s 
# name. Store these dictionaries in a list called pets. Next, loop through your list 
# and as you do print everything you know about each pet.

# Same as it as in top

# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three 
# names to use as keys in the dictionary, and store one to three favorite places 
# for each person. To make this exercise a bit more interesting, ask some friends 
# to name a few of their favorite places. Loop through the dictionary, and print 
# each person’s name and their favorite places.


# Favorite_place={
#     'taby':['kerry', 'galway', 'cork'],
#     'Deepika':['Howth', 'powerscot'],
#     'Richard':['UK'],
#     'Manoj':['india', 'Dublin']
# }

# for name, places in Favorite_place.items():
#     print(f"\n{name} favorite plcaces are" )
#     for place in places:
#         print("\t"+ place )

# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so 
# each person can have more than one favorite number. Then print each person’s 
# name along with their favorite numbers.

# Smae as it is


# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as 
# keys in your dictionary. Create a dictionary of information about each city and 
# include the country that the city is in, its approximate population, and one fact 
# about that city. The keys for each city’s dictionary should be something like 
# country, population, and fact. Print the name of each city and all of the information you have stored about it.

#Same as it as 

# 6-12. Extensions: We’re now working with examples that are complex enough 
# that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program or improving the formatting of the output.


# Same as it 




                            # User Input and while loop

# 7-1. Rental Car: Write a program that asks the user what kind of rental car they 
# would like. Print a message about that car, such as “Let me see if I can find you 
# a Subaru.”

# Car =input("what kind ogf car would you like to?")
# print(f"Let me see if I can {Car}")

# 7-2. Restaurant Seating: Write a program that asks the user how many people 
# are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is read



# people = int(input("How many people are in their dinner group "))
# if (people) > 8:
#     print("You have to wait for the table")
# else:
#     print("table is ready")


# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the 
# number is a multiple of 10 or not.


# Number = int(input('Please give a number'))
# if Number%10==0:
#     print(f"{Number} is Multiple of 10")
# else:
#     print("Number is not multiple of 10")


# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of 
# pizza toppings until they enter a 'quit' value. As they enter each topping, 
# print a message saying you’ll add that topping to their pizza.

# Pizza =("Please enter your pizza topping")

# while  True:
#     Message = input(Pizza)
#     if Message=='q':
#        break
#     else:
#         print("\n{Message} your topping will be added")


# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on 
# a person’s age. If a person is under the age of 3, the ticket is free; if they are 
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is 
# $15. Write a loop in which you ask users their age, and then tell them the cost 
# of their movie ticket.

# Age =int(input("Please enter your age"))

# if Age < 3:
#     print("ticke is free") 
    
# elif Age >=3 and Age<=12:
#     print("ticket is $10")
    
# elif Age >12:
#     print("ticket is $15") 
  
# while True:
    
#     if Age < 3:
#         print("ticke is free") 
#         break
#     elif Age >=3 and Age<=12:
#         print("ticket is $10")
#         break
#     elif Age >12:
#         print("ticket is $15") 
#         break     

# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 
# that do each of the following at least once:
# •	 Use a conditional test in the while statement to stop the loop.
# •	 Use an active variable to control how long the loop runs.
# •	 Use a break statement to exit the loop when the user enters a 'quit' value.

# Message =("\n enter your  age")

# active = True
# while active:
#     Age = input(Message)
#     if Age =='q':
#       active =False  
#     elif int(Age) < 3:
#         print("ticke is free") 
#         break
#     elif int(Age) >=3 and int(Age)<=12:
#         print("ticket is $10")
#         break
#     elif int(Age) >12:
#         print("ticket is $15") 
#         break 
     



# 7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press 
# ctrl-C or close the window displaying the output.)

# while True:
    
#     if Age < 3:
#         print("ticke is free") 
#        
#     elif Age >=3 and Age<=12:
#         print("ticket is $10")
#       
#     elif Age >12:
#         print("ticket is $15") 


# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop 
# through the list of sandwich orders and print a message for each order, such 
# as I made your tuna sandwich. As each sandwich is made, move it to the list 
# of finished sandwiches. After all the sandwiches have been made, print a 
# message listing each sandwich that was made.


# Sandwich_orders= ['spinach_sandwich', 'chicken_sandwich', 'Mutton_sandwich']
# finished_sandwich=[]

# for sandwich in Sandwich_orders:

#     print(f"As i made {sandwich} ")
    
#     finished_sandwich.append(sandwich)
#     print(f"\t{sandwich} are ready to coolect")

# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure 
# the sandwich 'pastrami' appears in the list at least three times. Add code 
# near the beginning of your program to print a message saying the deli has 
# run out of pastrami, and then use a while loop to remove all occurrences of 
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up 
# in finished_sandwiches.


# Sandwich_orders= ['spinach_sandwich', 'chicken_sandwich', 'Mutton_sandwich', 'pastrami', 'pastrami', 'pastrami']
# finished_sandwich=[]

# Message= "Deli is out of order"
# print(Message)

# while 'pastrami' in Sandwich_orders:
#     Sandwich_orders.remove('pastrami')
#     print(Sandwich_orders)

# 7-10. Dream Vacation: Write a program that polls users about their dream 
# vacation. Write a prompt similar to If you could visit one place in the world, 
# where would you go? Include a block of code that prints the results of the poll.



# responses={}

# polling_active = True
# while polling_active:

#     Name =input("What is your name?")
#     response =input("which place would you like to go?")

#     responses[Name]= response

#     repeat = input("Would you like to let another person respond? (yes/ no) ")
#     if repeat == 'no':
#         polling_active= False
# print("\n --- Poll Result ---")
# for name, response in responses.items():
#         print(name + "would like visit " + response +".")

                                    # Function


# 8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the 
# function, and make sure the message displays correctly.





# def display_message():
#     print("what are you learning about this chappter")
# display_message()

# 8-2. Favorite Book: Write a function called favorite_book() that accepts one 
# parameter, title. The function should print a message, such as One of my 
# favorite books is Alice in Wonderland. Call the function, making sure to 
# include a book title as an argument in the function call.


# def favorite_book(title):
#     print(f"favorite book is  {title} in WOnderland ")
#     print("favorite book is" +title+ "!")
# favorite_book('Alice')

# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the 
# text of a message that should be printed on the shirt. The function should print 
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the 
# function a second time using keyword arguments.


# def make_shirt(text, Size):
#     print(f"  {Size} {text} ")

# make_shirt('my shirt is', 5 )



# If we change postion then it will change it will print what is in that position
# def make_shirt(text, Size):
#     print(f"  {Size} {text} ")

# make_shirt(5, 'my shirt is')

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large 
# by default with a message that reads I love Python. Make a large shirt and a 
# medium shirt with the default message, and a shirt of any size with a different 
# message.

# def make_shirt(size="large",text='I love Python'):
#     print(f"Size of the shirt is' {size}\t {text}")
# make_shirt()

# make_shirt("medium")

# make_shirt("small", 'I hate java')


# 8-5. Cities: Write a function called describe_city() that accepts the name of 
# a city and its country. The function should print a simple sentence, such as 
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the 
# default country.


# def describe_city(city, country="Iceland"):
#     print(f"{city} is in {country}")
# describe_city('Rekjavi')
# describe_city('sekjavi')
# describe_city('gahvika')
# describe_city('Mumabai', 'India')


# 8-6. City Names: Write a function called city_country() that takes in the name 
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the value 
# that’s returned.

# def city_country(city, country):

#     city_country= city +','+ country
#     return city_country
# cititis=city_country('Santiage','Chile')
# cititis=city_country('Mumbai','Indai')

# We need to give argument

# cititis=city_country()
# print(cititis)



    # print(f"{city}+ {country}")

# city_country('Rekjavi')
# city_country('sekjavi')
# city_country('gahvika')
# city_country('Mumabai', 'India')


# 8-7. Album: Write a function called make_album() that builds a dictionary 
# describing a music album. The function should take in an artist name and an 
# album title, and it should return a dictionary containing these two pieces of 
# information. Use the function to make three dictionaries representing different 
# albums. Print each return value to show that the dictionaries are storing the 
# album information correctly.
# Add an optional parameter to make_album() that allows you to store the 
# number of tracks on an album. If the calling line includes a value for the number of tracks, add that value to the album’s dictionary. Make at least one new 
# function call that includes the number of tracks on an album.


# def make_album(artist_name, album_title, No_Track=''):
#     Persons= {'name':artist_name, 'title':album_title}
#     if No_Track:
#          Persons['No_Track'] =No_Track   
#     return Persons
# Artist=make_album('Taby', 'dg')
# print(Artist)

# Artist1=make_album('Taqi', 'mix-song')
# print(Artist)
# Artist2=make_album('zaki', 'kes')
# print(Artist2)

# Artist2=make_album('zaki', 'kes', 5)
# print(Artist2)


# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that 
# information, call make_album() with the user’s input and print the dictionary 
# that’s created. Be sure to include a quit value in the while loop.

# def make_album(artist, artist_title):
#     Person={ 'artist_name': artist, 'title': artist_title}
#     return Person
# while True:
#     artist=input("\n Please enter artist name")
#     if artist == 'q':
#         break
#     artist_title=input("\n enter title name")
#     if artist_title == 'q':
#         break
    
#     Artist=make_album(artist, artist_title)
#     print(Artist)

# 8-9. Magicians: Make a list of magician’s names. Pass the list to a function 
# called show_magicians(), which prints the name of each magician in the list.

# def show_magicians(names):

#     for name in names:
#         print("hello"+ name)
# magicians= ['terre', 'rere', 'resd', 'asdsad']
# show_magicians(magicians)



# extra

# def show_Actor(ActorNmaes):

#     for actor in ActorNmaes:
#         print(actor+ "hi")

# Actors=['neevah', 'forela', 'mele']
# show_Actor(Actors)


# 8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list of magicians by adding the phrase the Great to each magician’s name. Call show_magicians() to 
# see that the list has actually been modified.


# def make_great(magicians):
#     for macian in magicians:
#         print("Great"+macian)

# Magicians=['tre', 'ewwe', 'reedd', 'ererrw']

# make_great(Magicians)


# 8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the 
# function make_great() with a copy of the list of magicians’ names. Because the 
# original list will be unchanged, return the new list and store it in a separate list.
# Call show_magicians() with each list to show that you have one list of the original names and one list with the Great added to each magician’s name.


# def make_great():

# def show_magicians():





