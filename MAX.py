#siva
n=int(input())
a=[int(n) for n in input().split()]
w=a.sort()
maxx=0
for i in range(len(a)):
    if maxx<a[i]:
        maxx=a[i]
print(maxx)

