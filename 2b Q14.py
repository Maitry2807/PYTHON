s1=int(input("the marks of the subject 1 is"))
s2=int(input("the marks of the subject 2 is"))
s3=int(input("the marks of the subject 3 is"))

total=s1+s2+s3
avg=(s1+s2+s3)%2

if marks>=80:
        print("O+")
        print("total is", total)
        print("average is",avg)
elif (marks>=70):
        print("A+")
        print("total is", total)
        print("average is",avg)
elif (marks>=60):
        print("A")
        print("total is", total)
        print("average is",avg)
elif (marks>=55):
        print("B+")
        print("total is", total)
        print("average is",avg)
elif (marks>=50):
        print("B")
        print("total is", total)
        print("average is",avg) 
elif (marks>=45):
        print("C")
        print("total is", total)
        print("average is",avg) 
elif (marks>=40):
        print("PASS")
        print("total is", total)
        print("average is",avg) 
elif (marks>0) & (marks<=39):
        print("FAIL")
else:
       PRINT("Enter valid marks")