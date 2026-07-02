import math

print("SIMPLE CALCULATOR")

print("Please choose a operator")

print("1.Addition") #Choose it for adding your numbers

print("2.Subtraction")#Choose it for subtracting your numbers

print("3.Multiply")#Choose it for multiplying your numbers

print("4.Division")#Choose it for dividing your numbers

print("5.HCF")

a=int(input("Choose a operator 1, 2, 3 or 4 :")) #Choose the operation you want to perform

b=int(input("Enter greater number:"))

c=int(input("Enter smaller number:"))

if a==1:

print(b,"+",c,"=",b+c)

elif a==2:

print(b,"-",c,"=" ,b-c)

elif a==3:

print(b,"*",c,"=",b*c)

elif a==4:

print(b,"/",c,"=" ,b/c)

else:

print("Invalid input")

#CREATED BY MANJAS ANAND

print(“Thank You For Using!”)
