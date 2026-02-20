num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("\n--- Arithmetic Operations ---")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
if num2 != 0:
    print("Division:", num1 / num2)
    print("Modulus:", num1 % num2)
else:
    print("Division, Modulus and Floor Division not possible (division by zero)")
