def get_average():
    with open('files/data', 'r') as file:
        data = file.readlines()
        values = data[1:]
    average = [float(number) for number in values]
    result = sum(average) / len(values)
    return result


average = get_average()

print(average)


