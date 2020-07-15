import csv

from matplotlib import pyplot as plt

from datetime import datetime

if __name__ == "__main__":
    filename = "death_valley_2014.csv"
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        # for index, value in enumerate(header_row):
        #     print(index, value)
        
        dates, highs, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print('data value error')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

        fig = plt.figure(dpi=128, figsize=(10, 6))
        plt.plot(dates, highs, c='red', alpha=0.5)
        plt.plot(dates, lows, c='blue', alpha=0.5)
        plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.2)
        plt.title('weather', fontsize=20)
        fig.autofmt_xdate()
        plt.ylabel('Temperature(F)', fontsize=18)
        plt.tick_params(axis='both', width=2, colors='green', which='both', labelsize=16)
        plt.savefig('Temperature-death')
        plt.show()

