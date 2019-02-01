#siva
n=int(input())
summ=0
k=n
while n>0:
    
    r=n%10
    
    summ=summ*10+r
    
    n=n//10
print(summ)
if summ==k:
    print('yes')
else:
    print('no')

