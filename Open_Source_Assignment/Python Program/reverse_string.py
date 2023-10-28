def reverse_string(input_string):
    stack = list(input_string)
    reversed_str = []
    while stack:
        reversed_str.append(stack.pop())
    return ''.join(reversed_str)


text = input("Enter a string: ")
reversed_text = reverse_string(text)
print("Reversed string:", reversed_text)
