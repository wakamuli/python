L=[1,2,3,4,5]
print(L)
count=0
for i in L:
    count+=i
avg=count/(len(L))
print(count, avg)

L.sort()
print("Smallest interger", L[0])
print("Largest Integer", L[-1])



