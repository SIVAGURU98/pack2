#siva
n=int(input())
a=[int(n) for n in input().split()]
w=a.sort()
k=n//2
median=a[k]
print(median)
