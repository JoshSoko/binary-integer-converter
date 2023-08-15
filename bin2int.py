# Python program that converts base-2 numbers into positive base-10 integers
# Takes an input, removes spaces, checks if each character is a 0 or a 1, then returns the new integer

binary = input('Please enter a binary number: ')
total = 0

binary = binary.replace(' ', '')
for i in range(len(binary)):
    if binary[i] == '0':
        continue
    elif binary[i] == '1':
        total += (2 ** (len(binary) - i - 1))
    else:
        print("Please enter a binary number.")
        exit()

print(total)