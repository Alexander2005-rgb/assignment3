#calculate factorial using a function
def factorial(n):
     if n == 0:
          return 1
     else:
          return n * factorial(n-1)
n=int(input("Enter a number : "))

print("Factorial of", n, "is", factorial(n))

#using the math module for calculation  
import math
n=int(input("Enter a number : "))
print("Square root:",math.sqrt(n))
print("Logarithm:",math.log(n))
print("Sine:",math.sin(n))
