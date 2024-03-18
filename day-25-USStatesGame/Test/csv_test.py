# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
#     print(temperature)
import pandas


def fahrenheit_convert(x):
    return 9 / 5 * x + 32


data = pandas.read_csv("weather_data.csv")

print(fahrenheit_convert(data[data.day == "Monday"].temp[0]))
