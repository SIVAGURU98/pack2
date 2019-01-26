#siva
num=int(input())
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            print('not a prime')
            print(i,'times',num//i,'is',num)
            break
    else:
        print('is a prime')
else:
    print('not a prime')
    

