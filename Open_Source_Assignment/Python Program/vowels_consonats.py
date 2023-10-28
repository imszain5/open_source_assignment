def count_vowels(input_string):
    
    input_string = input_string.lower()
    
    vowel_count = 0

    vowels = set("aeiou")

    for char in input_string:
        if char in vowels:
            vowel_count += 1
    
    return vowel_count

text = input("Enter a string: ")
vowel_count = count_vowels(text)
print("Number of vowels in the string:", vowel_count)
