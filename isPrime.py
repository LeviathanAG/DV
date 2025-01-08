def isPrime(a):
    num = 2
    while(num<a):
        if(a==2):
            return 1
        if(a==3):
            return 1
        if(a<0):
            return 0
        if(a%num==0):
            return 0
        num=num+1
    return 1
# body
a=int(input("a="))
c=isPrime(a)
if(c):
    print("Prime")
else: print("Not prime")