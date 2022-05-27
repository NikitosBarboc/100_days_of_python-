import string
import random
symbols = list(string.ascii_letters)
numbers = list(string.digits)
punctuation = list(string.punctuation)
print('Welcome to the PyPassword Generator!')
length = int(input('How many letters would you like?'))
symbols_len = int(input('How many symbols would you like?'))
num_len = int(input('How many numbers would you like?'))
password = []

for symb in range(symbols_len):
    password.append(random.choice(symbols))
for num in range(num_len):
    password.append(random.choice(numbers))
for char in range(length - num_len - symbols_len):
    password.append(random.choice(punctuation))

random.shuffle(password)
res = ''
for i in password:
    res += str(i)
print(res)