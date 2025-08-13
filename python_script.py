import os
import sys
import time

#/@ cette fonction to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

#/@ cette fonction to generate Fibonacci sequence up to a certain limit
def fibonacci(limit):
    fib_seq = [0, 1]
    while fib_seq[-1] + fib_seq[-2] < limit:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

#/@ cette fonction Main function
def main():
    #// Displaying welcome message
    print("Welcome to the Python Script!")

    #// Prompting user to enter a number
    num = int(input("Enter a number: "))

    #// Checking if the number is prime
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

    #// Generating Fibonacci sequence up to the entered number
    fib_limit = int(input("Enter a limit for the Fibonacci sequence: "))
    fib_seq = fibonacci(fib_limit)
    print(f"Fibonacci sequence up to {fib_limit}: {fib_seq}")

    #// Displaying current date and time
    print(f"Current date and time: {time.strftime('%Y-%m-%d %H:%M:%S')}")

    #// Displaying system information
    print(f"System platform: {sys.platform}")
    print(f"Python version: {sys.version}")

    #// Creating a new directory
    new_dir = input("Enter the name of the directory to create: ")
    os.makedirs(new_dir)
    print(f"Directory '{new_dir}' created successfully.")

#// cette condion
if __name__ == "_main_":
    #// Calling the main function
    main()

#/@ cette class est appeler Class1
class Class1:
    def __init__(self) -> None:
        print("C'est une class")