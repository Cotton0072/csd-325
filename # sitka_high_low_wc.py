# sitka_high_low_wc.py
# Module 4 - Sitka Highs and Lows Interactive Program
# Author: Will Cotton
# Description:
# This program reads Sitka weather data and allows the user to view
# either high or low temperatures in a line graph, or exit the program.

import csv
from datetime import datetime
from matplotlib import pyplot as plt # pyright: ignore[reportMissingModuleSource]
import sys

# File with Sitka weather data
filename = 'sitka_weather_2018_simple.csv'

# Create empty lists for data
dates, highs, lows = [], [], []

# Read the CSV file
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high, and low temperatures from the file
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data for {row[2]}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Welcome message and menu instructions
print("\nWelcome to the Sitka Weather Viewer!")
print("You can view either High or Low temperatures for 2018.")
print("Type 'highs' for high temperatures, 'lows' for low temperatures, or 'exit' to quit.\n")

# Program loop
while True:
    choice = input("Enter your choice (highs/lows/exit): ").strip().lower()

    if choice == 'highs':
        plt.style.use('seaborn-v0_8')
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        plt.title("Daily High Temperatures - 2018, Sitka, AK", fontsize=20)
        plt.xlabel('', fontsize=14)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=14)
        plt.tick_params(axis='both', which='major', labelsize=12)
        plt.show()

    elif choice == 'lows':
        plt.style.use('seaborn-v0_8')
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        plt.title("Daily Low Temperatures - 2018, Sitka, AK", fontsize=20)
        plt.xlabel('', fontsize=14)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=14)
        plt.tick_params(axis='both', which='major', labelsize=12)
        plt.show()

    elif choice == 'exit':
        print("\nThank you for using the Sitka Weather Viewer. Goodbye!\n")
        sys.exit()

    else:
        print("Invalid option. Please type 'highs', 'lows', or 'exit'.")
