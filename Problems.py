x=956000000
count=0
rem=0
while(x!=0):
    rem=x%10
    count=count+1
    x=x//10
print(count)