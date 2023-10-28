def is_palindrome(input_string):
    
    cleaned_string = input_string.replace(" ", "").lower()

  
    return cleaned_string == cleaned_string[::-1]


text = input("Enter a string: ")

if is_palindrome(text):
    print(f"{text} is a palindrome.")
else:
    print(f"{text} is not a palindrome.")
