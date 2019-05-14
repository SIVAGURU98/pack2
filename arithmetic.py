# Python Program to find Sum of Arithmetic Progression Series
n,a,d = map(int,input().split())

summ=0
i=0
while i<n:
    summ=summ+a
    a=a+1
    i=i+1
print(summ)

