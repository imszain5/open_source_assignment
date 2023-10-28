import math

def find_common_divisors(num1, num2):
   
    gcd = math.gcd(num1, num2)
    
   
    common_divisors = []
    for i in range(1, gcd + 1):
        if num1 % i == 0 and num2 % i == 0:
            common_divisors.append(i)
    
    return gcd, common_divisors


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number:"))

gcd, divisors = find_common_divisors(num1, num2)

print("GCD of", num1, "and", num2, "is", gcd)
print("Common Divisors:", divisors)
