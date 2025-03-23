# Print a multiplication table of a given number.
num = int(input("Enter a number: "))
i = 0

while i <= 10:
    print(num ,"x", i, "=", num * i)
    i += 1