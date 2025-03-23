l=int(input("enter the length"))
b=int(input("enter the breath"))

A=l*b
P=2*(l+b)

if (A>P):
    print("the area is greater than the perimeter")
else:
    print("the perimeter is greater than the area")