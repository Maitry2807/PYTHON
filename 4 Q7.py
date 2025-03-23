# Print nCr and nPr.
n=int(input("enter n= "))
r=int(input("enter r= "))

fact_n=1
for i in range(1,n+1):
    fact_n*=i

fact_r=1
for i in range(1,r+1):
    fact_r*=i

fact_r_n=1
for i in range(1,n-r+1):
    fact_r_n*=i

nCr=fact_n//fact_r*fact_r_n
nPr=fact_n//fact_r_n

print("nCr=",nCr)
print("nPr",nPr)