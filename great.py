
password = input('Enter a password here. I will check ---> ')

# 8 symbols
# 1 big letter
# At least 1 number
def check_password():
    len_password = len(password)

    list_with_result = {}

    strong_password = False
    if len_password >= 8:
        strong_password = True
    list_with_result['8 symbols'] = strong_password

    big_letter = False
    one_number = False

    for letter in password:
        if letter.isupper():
            big_letter = True
        if letter.isdigit():
            one_number = True

    list_with_result['Big letter'] = big_letter
    list_with_result['One number'] = one_number
    print(all(list_with_result))
    print(list_with_result)
    if all(list_with_result.values()):
        return 'You have a strong password.'
    return 'You have a weak password'

print(check_password())










