#write a python program to print the multiplication tables from 1 to n
'''  n=int(input())
for i in range(1,n+1):
    print(f"Multiplication table of {i}")
    print("-----------------------------")
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")'''
#Write a python program to print the reversed multiplication tables from 1 to n
n=int(input())
for i in range(1,n+1):
    print(f"Multiplication table of {i}")
    print("-----------------------------")
    for j in range(10,0,-1):
        print(f"{i} * {j} = {i*j}")