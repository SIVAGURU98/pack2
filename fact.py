#siva
n=int(input())
fact=1
if n<0:
    print('fact not exist')
elif n==0:
    print('fact of 0 is 1')
else:
    for i in range(1,n+1):
        fact=fact*i
    print('the fact of',n,'is',fact)
    
        

