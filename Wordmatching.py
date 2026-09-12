def match_words(words):
    ctr=0
    lst=[]
    for i in words:
       if  i[0]==i[-1]:
           ctr+=1
           lst.append(i)
    print(lst)
    return ctr
x=match_words(["hello", "world","zinz","googlg"])
print(x)



    
