print("Dear sender, Please send the message")

strings = []
number_of_strings = int(input("Enter the number of strings: "))

for i in range(number_of_strings):
    string = input("Enter a string: ")
    strings.append(string)

modified_strings = [string[1:] + string[0] for string in strings]

target_string2 = " ".join(modified_strings)

print("Modified target string:", target_string2)

import random
import string

S = 3
ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
ran2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))

secret = ran + target_string2 + ran2

print(secret)
print()

print("Dear Receiver, Decode the Message")

original_string = secret
prefix_length = 3
suffix_length = 3

prefix = original_string[:prefix_length]
suffix = original_string[-suffix_length:]

modified_string_here = original_string[prefix_length:-suffix_length]

print(modified_string_here)

name = modified_string_here
res = [s[-1] + s[:-1] for s in name]  # Use 's' instead of 'string'

target_string3 = "".join(res)
print("Decoded Message: " + target_string3)
