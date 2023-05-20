# We need to check if we have 8 symbols(less or more), 1 big letter and minimum 1 number.

password = input('Type here a password to check: ')
password_lenght = len(password)

print(password_lenght)

result = []

strong_password = False

if password_lenght >= 8:
    result.append(True)
else:
    result.append((False))

big_letter = False
for i in password:
    if i.isupper():
        big_letter = True

result.append(big_letter)

digit = False
for i in password:
    if i.isdigit():
        digit = True

result.append(digit)

print(result)

if all(result):
    print('You have a good and strong password.')
else:
    print('You have a bad password.')



