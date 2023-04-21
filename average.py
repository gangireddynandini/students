n=int(input('enter how many numbers u want:'))
lst=[]
for i in range(1,n+1):
    val=int(input('enter  {} value:'.format(i)))
    lst.append(val)
print(lst)
sum1=sum(lst)/n
print(sum1)