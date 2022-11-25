l=[int(x) for x  in input("enter numbers").split()]
l=sorted(l)
print("List before arrangement",l)
z=[]
if len(l)==0 or len(l)==1:
    print("REARRANGEMENT NOT POSSIBLE")
elif len(l)%2==0:
    for i in range(len(l)):
        z.append(max(l))
        z.append(min(l))
        l.remove(max(l))
        l.remove(min(l))
        if len(l)==0:
            break
    print("Result after arrangement",z)
elif len(l)%2!=0:
    for i in range(len(l)):
        z.append(max(l))
        z.append(min(l))
        l.remove(max(l))
        l.remove(min(l))
        if len(l)==1:
            z.append(l[0])
            l.remove(l[0])
            break
        else:
            continue
    print("Result after arrangement",z)
