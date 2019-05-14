#siva
a,b=map(int,input().split())
for n in range(a,b+1):
    summ=0
    k=n
    while n>0:
        r=n%10
        summ=summ+r**3
        n=n//10
        if k==summ:
            print(summ)
