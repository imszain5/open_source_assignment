import math

def find_lcm(num1, num2):
 
    gcd = math.gcd(num1, num2)
    lcm = (num1 * num2) // gcd
    return lcm


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

lcm = find_lcm(num1, num2)

print("LCM of", num1, "and", num2, "is", lcm)
