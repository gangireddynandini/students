#list of primes
n=int(input('enter a number up to which u want:'))
for i in range(2,n):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)
