
#! String

# \n escap sequence charactor
#\t tab space sequence charactor

# str = "\nMy name is Praveen Kumar\n\nI'm flutter developer\n" 
# print(str)

#! concatenate of string

# len(str) to calaculate length of str
# str[2] to find 
# print("hello"+"world")

# ! slicing of a string

# str =  "Hello World"

# sliceStr = str[0:5]
# sliceStr2 = str[:5] #![0:5]
# sliceStr4 = str[2:] #! [2:len(str)]
# print(sliceStr)

# ! negative indexing

# str = "apple"

# print(str[-5:-1  ])


#! String Function

str = "Hello Praveen"

# print(str.endswith("een"))
# print(str.capitalize())
# print(str.lower())
# print(str.upper())
# print(str.replace("e","a"))
# print(str.find("ell"))
# print(str.count("e"))

#! 1. write a program in which take str from input and prin their length


# str = input("enter str: ")

# print(len(str))

#! 2. WAP to find $ occurrence in a string

# str = "helle $ dosto $ my name is $aman"

# print(str.count("$"))

#! Conditional statements
 
# mark = 94

# if(mark >=90):
#     print("Grad A")
# elif(mark >= 80 and mark < 90):
#     print("Grad B")
# elif(mark >= 70 and mark < 80):
#     print("Grad C")
# elif(mark >= 60 and mark < 70):
#     print("Grad D")
# else:
#     print("fail")

# ! 1. take input form the user and check number is even or odd


# number = int(input("enter number: "))

# if((number % 2) == 0):
#     print("number is even")
# else:
#     print("number is odd")


#! 2. WAP to find the greatest of 3 numbers entered by the user.

num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
num3 = int(input("enter num3: "))

if(num1 >= num2 and num1>= num3):
    print("num1 is greater")
elif(num2 >= num3):
    print("num2 is greater")
else:
    print("num3 is greater")

#! 3. WAP to find if a number is multiple of 7 or not

# number = int(input("enter number: "))

# if(number % 7 == 0):
#     print("number is multiple of 7")
# else:
#     print("number is not multiple of 7")

