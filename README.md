# assignment3
# Calculate factorial using a function
def factorial(n):
This line defines a function named factorial that takes one parameter n. This function will be used to calculate the factorial of the number n.
    if n == 0:
This line checks if the value of n is equal to 0. The factorial of 0 is defined to be 1.
        return 1
If the condition in the previous line is true (i.e., n is 0), this line returns 1, which is the factorial of 0.
    else:
This line introduces an alternative condition that will execute if the previous if condition is false (i.e., if n is not 0).
        return n * factorial(n - 1)
If n is not 0, this line calculates the factorial recursively. It returns the product of n and the factorial of n - 1. This continues until n reaches 0, at which point the recursion stops.
n = int(input("Enter a number: "))
This line prompts the user to enter a number. The input() function captures the user's input as a string, and int() converts it to an integer, which is then stored in the variable n.
print("Factorial of", n, "is", factorial(n))
This line calls the factorial function with the user-provided number n and prints the result. It displays the message "Factorial of" followed by the value of n and the calculated factorial.
# Using the math module for calculation
import math
This line imports the math module, which provides access to mathematical functions and constants.
n = int(input("Enter a number: "))
Similar to the previous input, this line prompts the user to enter another number and stores it in the variable n.
print("Square root:", math.sqrt(n))
This line calculates the square root of the number n using the sqrt function from the math module and prints the result, displaying the message "Square root:" followed by the calculated value.
print("Logarithm:", math.log(n))
This line calculates the natural logarithm of the number n using the log function from the math module and prints the result, displaying the message "Logarithm:" followed by the calculated value.
print("Sine:", math.sin(n))
This line calculates the sine of the number n (in radians) using the sin function from the math module and prints the result, displaying the message "Sine:" followed by the calculated value.
