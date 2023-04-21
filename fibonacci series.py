n=int(input('enter a number:'))
first=0
second=1
for i in range(0,n):
    if(i<=1):
        result=i
    else:
        result=first+second
        first=second
        second=result
    print(result)

