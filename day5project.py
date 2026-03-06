import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','\*','+']

letters_count = int(input("How many letters do you want? "))
numbers_count = int(input("How many numbers do you want? "))
symbols_count = int(input("How many symbols do you want? "))

password_list = []

for char in range(letters_count):        # Fixed: range(count), not range(1, count)
    password_list.append(random.choice(letters))

for char in range(numbers_count):        # Fixed
    password_list.append(random.choice(numbers))

for char in range(symbols_count):        # Fixed
    password_list.append(random.choice(symbols))

random.shuffle(password_list)            # Added: shuffle so pattern isn't predictable

password = "".join(password_list)
print(f"Your password: {password}")