#Write a python program and input from user and check whether the age is valid to vote or not
'''age=int(input("Enter your age: "))
if(age>=18):
    print("eligible to vote")
else:
    print("Not eligiblle to vote")
res="eligible" if age>=18 else "not eligible"
print("You are",res,"to vote")'''
#write a python program to read an integer as a input from user and check wheather it is +ve or -ve or 0
'''num=int(input("Enter Your number: "))
if(num>0):
    print(f"{num} is Positive")
elif(num<0):
    print(f"{num} is Negative")
else:
    print(f"{num} is zero")'''
#write a python program to read 2 integer values as an input and find the largest number
'''a,b=map(int,input("Enter your numbers: ").split())
if(a>b):
    print("A")
else:
    print("B")'''
'''month=int(input("Enter Month number"))
if(month>=1 and month<=12):
    print("Month number",month,"is valid")
else:
    print("Month number",month,"is invalid")'''
#write a python program to read a input as integer and check 
'''month=int(input("Enter Month number"))
if(month in [1,3,5,7,8,10,12]):
    print("Month number",month,"has 31 days")
elif(month in [4,6,9,11]):
    print("Month number",month,"has 30 days")
elif(month==2):
    print("Month number",month,"has 28 or 29 days")
else:
    print("Month number",month,"is invalid")'''
#write a python program and take input from user to check it is even or odd
'''n=int(input("Enter your number"))
if(n%2!=0):
    print("Your number",n,"is odd")
else:
    print("Your number",n,"is even")'''
#write a python program to check wheteher the year is leap year or not#
'''year=int(input("Enter Year: "))
if(year%4==0 and year%100!=0) or (year%400==0):
    print(f"{year} is a leap year")'''
#write a python program to read three integers values and find the largest number
#write a python program to read three integers values and find the smallest number
#write a python program to read 2 integers values and find the smallest number
#write a python program to read 3 integers values and find the middle number
'''a=int(input())
b=int(input())
c=int(input())
if(a>b and a>c):
    print("A is",a,"Largest")
elif(b>a and b>c):
    print("B is",b,"Largest number")
elif(c>a and c>b):
    print("C is ",c,"Largest number")
a,b,c=map(int,input("Enter a,b,c numbers : ").split())
if(a<b and a<c):
    print("A is smallest number")'''




'''n=int(input("Enter bill amount"))
if(n>500):
    print("Disocunt applied",n/10)
else:
    print("Discount not applied",n,"remains same amount")'''
n=int(input("Enter marks of a student:"))
if(n>=35):
    print("Pass")
else:
    print("Fail")