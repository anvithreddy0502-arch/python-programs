num = int(input("Enter a number: "))
temp = num
numdigits = len(str(num))
sumofpowers = 0
while temp > 0:
    digit = temp % 10
    sumofpowers += digit ** numdigits
    temp //= 10
if sumofpowers == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")