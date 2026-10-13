a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition =", a + b)

print("Difference =", a - b)

print("Multiplication =", a * b)

if b != 0:
    print("Division =", a / b)
else:
    print("Division is not possible")

print("Modulus =", a % b if b != 0 else "Not possible")