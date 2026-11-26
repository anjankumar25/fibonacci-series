a=0
b=1
print(a)
print(b)



n=int(input("emter: "))
for i in range(2,n+1):
    c=a+b
    a=b
    b=c
    print(c)
if n == 1:
    print(a)