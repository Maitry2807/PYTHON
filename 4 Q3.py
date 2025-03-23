# Count no. of alphabets and no. of digits in any given string.
string=input("enter a string")
alphabets=0
digits=0

for char in string:
    if char.isalpha():
        alphabets+=1
    else:
        digits+=1

print("the number of alphabets is",alphabets)
print("the number of digits",digits)