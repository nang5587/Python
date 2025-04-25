

# with open('data/weather_data/death_valley_2021_full.csv', 'r') as f:
#     for line in f:
#         print(line)

import csv
import matplotlib.pyplot as plt
from datetime import datetime

with open('data/weather_data/sitka_weather_2021_simple.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    print(f"highs = {highs}")

    for i, column_header in enumerate(header_row):
        print(i, column_header)

    print(f"header_row = {header_row}")

    plt.style.use('seaborn')
    fig, ax = plt.subplots()

    ax.plot(dates, highs, color='red', alpha=0.5)
    ax.plot(dates, lows, color='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    ax.set_title("daily high temperatures", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature(F)", fontsize=16)
    ax.tick_params(labelsize=16)

    plt.show()