def is_armstrong_number(number):
  
    num_str = str(number)
    num_digits = len(num_str)
    
  
    digit_sum = sum(int(digit) ** num_digits for digit in num_str)
 
    return number == digit_sum


num = int(input("Enter a number: "))

if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
