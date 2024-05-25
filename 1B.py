def factorial(n):
    result = 1
    for x in range(1, n + 1):
        result *= x
    return result
number = int(input("Enter a number: "))
print(f"The factorial of {number} is {factorial(number)}")
