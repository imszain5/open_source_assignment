def sum_of_digits(number):
   
    digit_sum = 0
    

    number = abs(number)
    
    
    while number > 0:
       
        digit_sum += number % 10
        
       
        number //= 10
    
    return digit_sum


num = int(input("Enter a number: "))
result = sum_of_digits(num)
print("Sum of digits in", num, "is", result)
