num = int(input("Enter a number: "))
temp = num
sumdigits = 0
while temp > 0:
    digit = temp % 10
    sumdigits += digit
    temp //= 10
print("Sum of digits =", sumdigits)