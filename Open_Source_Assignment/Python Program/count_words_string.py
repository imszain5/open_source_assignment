def count_words(input_string):
    words = input_string.split()
    return len(words)


text = input("Enter a string: ")
word_count = count_words(text)
print("Number of words in the string:", word_count)
