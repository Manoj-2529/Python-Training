def add(a,b):
    print("The sum is:",a+b)
def sub(a,b):
    print("The difference is:",a-b)
def mul(a,b):
    print("The product is:",a*b)
def div(a,b):
    print("The quotient is:",a/b)
def rem(a,b):
    print("The remainder is:",a%b)
while True:
    print("Enter the operation you want to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Remainder")
    print("6. Exit")
    choice = int(input("Enter your choice:"))
    if  choice == 6:
        break
    print("Enter the first number:")
    num1 = int(input())
    print("Enter the second number:")
    num2 = int(input())
    if choice == 1:
        add(num1,num2)
    elif choice == 2:
        sub(num1,num2)
    elif choice == 3:
        mul(num1,num2)
    elif choice == 4:
        div(num1,num2)
    elif choice == 5:
        rem(num1,num2)
    else:
        print("Invalid choice! Please try again.")