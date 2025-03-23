words = [
    "zero", "one", "two", "three", "four", 
    "five", "six", "seven", "eight", "nine", 
    "ten", "eleven", "twelve", "thirteen", "fourteen", 
    "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
]
number = int(input("Enter a number (0 to 19): "))

if 0 <= number <= 19:
    print("The word for number is:",words)
else:
    print("Number out of range! Please enter a number between 0 and 19.")
