# 10-6. Addition: One common problem when prompting for numerical input 
# occurs when people provide text instead of numbers. When you try to convert 
# the input to an int, you’ll get a TypeError. Write a program that prompts for 
# two numbers. Add them together and print the result. Catch the TypeError if 
# either input value is not a number, and print a friendly error message. Test your 
# program by entering two numbers and then by entering some text instead of a 
# number



# while True:
#     try:
#         number1 =int(input("please enter number1"))
#         number2=int(input("please enter number2"))
#         result=number1+number2
#         print(result)

#     except ValueError:
#         msg="sorry invalid characters please add as valid number"
#         print(msg)


# Alternate method
# try:
#     number1 =int(input("please enter number1"))
#     number2=int(input("please enter number2"))
#     result=number1+number2
#     print(result)

# except ValueError:
#     msg="sorry invalid characters please add as valid number"
#     print(msg)


# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop 
# so the user can continue entering numbers even if they make a mistake and 
# enter text instead of a number.


# while True:
#     try:
#         number1 =int(input("please enter number1"))
#         number2=int(input("please enter number2"))
#         result=number1+number2
#         print(result)

#     except ValueError:
#         msg="sorry invalid characters please add as valid number"
#         print(msg)


# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three 
# names of cats in the first file and three names of dogs in the second file. Write 
# a program that tries to read these files and print the contents of the file to the 
# screen. Wrap your code in a try-except block to catch the FileNotFound error, 
# and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the except block 
# executes properly

# File_name='D:\lab-AWS\cat.txt'
# File_name1='D:\lab-AWS\Dog.txt'
# def Many_file(file):
#     try:
#        with open(file) as Object:
#            contents=Object.read()
#            print(contents)
#     except FileNotFoundError:
#         msg = "Sorry, the file " + file + " does not exist."
#         print(msg)

# Files=['D:\lab-AWS\cat.txt','D:\lab-AWS\Dog.txt']
# for file in Files:
#     print(Many_file(file))




# Ertra ChatGPT



# def readFile(filename):
#     try:
#         with open(filename, 'r') as file:
#             contents = file.read()
#             print(contents)
#     except FileNotFoundError:
#         print(f"Error: file '{filename}' not found")

# # read contacts of cats.text

# readFile('D:\lab-aws\cat.txt')
# readFile('D:\lab-AWS\Dog.txt')

# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail 
# silently if either file is missing.

# File_name='D:\lab-AWS\cat.txt'
# File_name1='D:\lab-AWS\Dog.txt'
# def Many_file(file):
#     try:
#        with open(file) as Object:
#            contents=Object.read()
#            print(contents)
#     except FileNotFoundError:
#         print("Sorry, the file " + file + " does not exist.")
     

# Files=['D:\lab-AWS\Python\cat.txt','D:\lab-AWS\Dog.txt']
# for file in Files:
#     print(Many_file(file))





# 10-10. Common Words: Visit Project Gutenberg (http://gutenberg.org/ ) 
# and find a few texts you’d like to analyze. Download the text files for these 
# works, or copy the raw text from your browser into a text file on your 
# computer.
# You can use the count() method to find out how many times a word or 
# phrase appears in a string. For example, the following code counts the number 
# of times 'row' appears in a string:
# >>> line = "Row, row, row your boat" 
# >>> line.count('row') 
# 2 
# >>> line.lower().count('row')




# def ReafFiles(File):
#     try:
#         with open(File) as File_Object:
#             content= File_Object.read()
#     except FileNotFoundError:
#         print("Sorry, the file " + File +"doesnot exists")
#     else:
#         words=content.count('row')
#         print(" The"+ File + "has about" +" "+ str(words) + "times repeated")

# File= r'D:/lab-AWS/File-Samuel.txt'
# ReafFiles(File)


# Extra


# def Read_File(Filename, word):
#     try:
#         with open(Filename) as f_obj :
#             content= f_obj.read()
#             word_count=content.lower().count(word.lower())
#             return word_count
#     except FileNotFoundError:
#         print("{filename} doesnot exist ")
    
# Filename= 'D:/lab-AWS/File-Samuel.txt'
# word= "row"


# occurrences = Read_File(Filename, word)
# if occurrences is not None:
#     print(f" the word '{word}' appears {occurrences} times in the file.")



#                       Storing data

# import json
# numbers=[1,2,3,4,5,6,7,8,9]

# filename='D:\lab-AWS\numbers.json'
# with open(filename, 'w') as f_obj:
#     json.dump(numbers, f_obj)
    

# import json
# filename ='numbers.json'
# with open(filename) as f_obj:
#     numbers= json.load(f_obj)
# print(numbers)


# import json

# username =input("What is your name?")
# filename=r'D:\lab-AWS\username.json'

# with open(filename, 'w') as obj:
#     json.dump(username, obj)
#     print("We'll remember you when you come back, " + username + "!")

# Now let’s write a new program that greets a user whose name has 
# already been stored


# import json
# filename =r'D:\lab-AWS\username.json'

# with open(filename) as obj:
#     username= json.load(obj)
#     print("Welcome back," + username + "!")

# import json
# def get_stored_username():
#     filename = r'D:\lab-AWS\username.json'
#     try:
#         with open(filename) as Obj:
#             username= json.load(Obj)
#     except FileNotFoundError:
#         return None
#     else:
#         return username
    
# def greet_user():
#     username = get_stored_username()
#     if username:
#         print("welcome back," + username +"!" )
#     else:
#         username = input("What is your your name? ")
#         filename =r'D:\lab-AWS\username.json'
#         with open(filename, 'w') as obj:
#             json.dump(username, obj)
#             print("well remembre you when you come back, " + username + "!")

# greet_user()



# 10-11. Favorite Number: Write a program that prompts for the user’s favorite 
# number. Use json.dump() to store this number in a file. Write a separate program that reads in this value and prints the message, “I know your favorite 
# number! It’s _____.”

    
# import json
# number = input("Please enter your favorite number")
# filename=r'D:\lab-AWS\favourite_number.json'
# with open(filename, 'w') as obj:
#     json.dump(number, obj)
#     print("Your favourite number" +  "is "+number )

# with open(filename) as obj_file:
#     user_nmuber=json.load(obj_file)
#     print("I know your favorite number is " +user_nmuber)


# 10-12. Favorite Number Remembered: Combine the two programs from 
# Exercise 10-11 into one file. If the number is already stored, report the favorite 
# number to the user. If not, prompt for the user’s favorite number and store it in a 
# file. Run the program twice to see that it works.



import json
# filename='favourite_number.json'
# favorite_number= input("what is your favorite number?")
# with open(filename, 'w')as obj:
            
#     json.dump(favorite_number, obj)
#     print("Your favourite number" +  "is "+favorite_number )


# import json
# def get_stored_number():
#     filename='favourite_number.json'
#     try:
#         with open(filename) as f_obj:
#             favorite_number =json.load(f_obj)
#     except FileNotFoundError:
#         return None
#     else:
#             return favorite_number
# get_stored_number() 

# def remember_fav_number():
#     number= get_stored_number()
#     if number:
#         print("Your remembered number," +number+ "!") 
#     else:
#         number =input("what is your favourite number")
#         filename='favourite_number.json'
#         with open(filename, 'w') as f_obj:
#              json.dump(number, f_obj)
#              print("we'll remember your number " + number + "!")

# remember_fav_number()


# 10-13. Verify User: The final listing for remember_me.py assumes either that the 
# user has already entered their username or that the program is running for the 
# first time. We should modify it in case the current user is not the person who 
# last used the program.
# Before printing a welcome back message in greet_user(), ask the user if 
# this is the correct username. If it’s not, call get_new_username() to get the correct 
# username.


# import json
def create_user():
    username= input("What is your name?")
    filename='NewFile.json'

    try:
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("we'll remember you when you come back, " + username + "!" )
    except FileNotFoundError:
        print("File not found")
    else:
        return username
create_user()


def greet_user():
    filename='NewFile.json'

    try:
        with open(filename) as f_obj:
            username= json.load(f_obj)
    except FileNotFoundError:
        username = create_user()
        print("we'll remember you come back," + username+"!")
    else:
        response= input("Is '" +username + " the correct username?(yes/no)")
        if response.lower() == 'no':
            username = create_user()
            print(f"welcome back,  {username}'!")
        else:
            print(f"welcome back, {username}  !")

greet_user()


        






















