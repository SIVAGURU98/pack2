#siva
n=int(input())
a=[int(n) for n in input().split()]
w=a.sort()
maxx=0
for i in range(len(a)):
    if maxx<a[i]:
        maxx=a[i]
print(maxx)
k=maxx
mini=k
for b in range(len(a)):
    if mini>a[b]:
        mini=a[b]
print(mini)

