
# Global variables
num1 = 0
num2 = 0

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

def calculate_sum():
    #Local variable
    global num1, num2
    sum = num1 + num2
    print(f"Sum: {sum}")
    return sum


def calculate_difference():
    #Local variable
    global sum
    difference = num1 - num2
    print(f"Difference: {difference}")
    return sum

calculate_sum()
calculate_difference()