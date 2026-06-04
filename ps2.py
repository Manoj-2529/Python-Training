list=[1,2,3,4,5,6,7,89,2,13,2224343,43,5,34,235,25,235,45,2,423,432,234]
even = 0
odd = 0

for i in range(list):

    if list % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers =", even)
print("Odd numbers =", odd)