password_user = input("Enter new password: ")


def check_password(password):

    result = {}

    lenght_symbols = False

    if len(password) >= 8:
        result['Lenght symbols'] = True
    else:
        result['Lenght symbols'] = False

    digit_in_password = False
    number_is_password = False


    for item in password:
        if item.isdigit():
            digit_in_password = True
        if item.isupper():
            number_is_password = True

    result['Digit in password:'] = digit_in_password
    result['Number in password'] = number_is_password

    if all(result.values()):
        return 'You have strong password'
    else:
        return 'You have a weak password'

print(check_password(password_user))








