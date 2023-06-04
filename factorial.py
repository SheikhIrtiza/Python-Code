def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial cannot be calculated for negative numbers.")
else:
    result = factorial(num)
    print("The factorial of", num, "is", result)
