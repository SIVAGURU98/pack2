#siva
a=0
b=1
summ=0
n=int(input())
for i in range(n):
    summ=a+b
    a=b
    b=summ
    print(summ,end=' ')

