import csv

with open('weather.csv', 'r') as file:
    data = list(csv.reader(file))

print(data)

user_city = input('Write a city to check ---> ')

for row in data[1:]:
    if row[0] == user_city:
        print(row[1])




