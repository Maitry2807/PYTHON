x1=int(input("x1"))
x2=int(input("x2"))
x3=int(input("x3"))
y1=int(input("y1"))
y2=int(input("y2"))
y3=int(input("y3"))

A=x1*(y2-y3)+x2*(y3-y1)+x3*(y2-y1)

if (A==0):
    print("the points lie in the straight line")
else:
    print("the points doesnot lie in the straight line")



