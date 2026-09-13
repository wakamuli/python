
def palind(r):
    e=len(r)-1
    s=0
    while s<e:
        if r[s]==r[e]:
            s+=1
            e-=1
        else: return "false"
    return "True"

r=(1,7,3,3,9,1)
x=palind(r)
print(x)

