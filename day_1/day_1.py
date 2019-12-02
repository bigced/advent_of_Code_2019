import csv
from math import floor


def calculate_fuel(mass):
    return floor(mass / 3) - 2


def fuel_of_fuel(mass):
    fuel = calculate_fuel(mass)
    if fuel > 0:
        return fuel + fuel_of_fuel(fuel)
    return 0


def load_data(data):
    return [int(_[0].strip()) for _ in data if _[0].strip()]


def main():
    return None


if __name__ == '__main__':
    input_data_file = csv.reader(open('data.csv'))
    input_data = load_data(input_data_file)
    result = 0
    for mass in input_data:
        result = result + fuel_of_fuel(mass)
    print(result)
