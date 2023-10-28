def number_to_words(number):

    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion", "trillion"]


    def chunk_to_words(chunk):
        chunk = int(chunk)
        if chunk == 0:
            return ""
        elif chunk < 10:
            return ones[chunk]
        elif chunk < 20:
            return teens[chunk - 10]
        else:
            return tens[chunk // 10] + " " + ones[chunk % 10]

    if number == 0:
        return "zero"

    number_str = str(number)
    num_chunks = (len(number_str) + 2) // 3
    num_chunks = max(num_chunks, 1)
    words = []

    for i in range(num_chunks):
        chunk = number_str[-(i * 3):][:3]
        chunk_words = chunk_to_words(chunk)
        if chunk_words:
            words.append(chunk_words + " " + thousands[i])

    return " ".join(reversed(words))

num = int(input("Enter a number: "))
words = number_to_words(num)
print("Number in words:", words)
