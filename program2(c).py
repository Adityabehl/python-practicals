# 2.l. Generate first n prime numbers
def genrateprime(n):
    flag=False
    count=0
    i=2
    while(count<n):
        flag=True
        for j in range(2,i):
            if i%j==0:
                flag=False
                break
        if flag :
            print(i)
            count+=1
        i+=1
n=int(input("enter the amount of primes you want"))
genrateprime(n)
