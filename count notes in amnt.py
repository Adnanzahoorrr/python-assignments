a=int(input("enter cash:"))
f=0
t=0
h=0
c=0
b=0
q=0
if a >=500:
    f+=a//500
    a=a%500
    if a >= 200:
        t += a //200
        a = a % 200
        if a >= 100:
            h += a //100
            a = a % 100
            if a >= 50:
                c += a // 50
                a = a % 50
                if a >=20:
                    b += a //20
                    a = a %20
                    if a >= 10:
                        q += a//10
                        a = a%10


print("No. of five hundred notes: ", f)
print("No. of two hundred notes: ", t)
print("No. of one hundred notes: ", h)
print("No. of fifty notes: ", c)
print("No. of twenty notes: ", b)
print("No. of ten notes: ", q)
