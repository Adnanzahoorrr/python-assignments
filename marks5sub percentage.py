maths=int(input("enter marks in maths"))
english=int(input("enter marks in english"))
sst=int(input("enter marks in sst"))
urdu=int(input("enter marks in urdu"))
science=int(input("enter marks in science"))
totalmarks=maths+english+sst+urdu+science
percentage=totalmarks/500*100
if percentage<33:
          print("fail")
else:
       print("pass")
if(percentage>=90):
    grade="a"
elif(percentage>=80):
    grade ="b"
elif(percentage>=70):
           grade ="c"
elif (percentage>=60):
           grade ="d"
elif (percentage>=40):
           grade ="e"
else:
 grade="fail "
print("grade obtained by student:", grade)