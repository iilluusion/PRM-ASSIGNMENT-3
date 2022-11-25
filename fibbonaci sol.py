def fibbonaci(n):
    if n<=0:
        return "incorrect input"
    else:
        l=[]
        a=0
        l.append(a)
        b=1
        l.append(b)
        for i in range(n-1):
            c=a+b
            l.append(c)
            a=b
            b=c
        return l[n-1]
n=int(input("ENTER THE NUMBER "))
c=fibbonaci(n)
print("result :", c)