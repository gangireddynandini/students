n=int(input('enter a number'))
b=str(n)
p=len(b)
sum=0
for i in b:
    j=int(i)**p
    # print(j)
    sum=sum+j
if(n==sum):
    print('the given number is armstrong')
else:
    print('not armstrong')