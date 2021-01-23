import csv
from datetime import datetime

import matplotlib.pyplot as plt 

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #从文件中获取日期和降水量。
    dates, precips = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            precip = float(row[3])
        except ValueError:
            print("Missing data for " + str(current_date))
        else:
            dates.append(current_date)
            precips.append(precip)

#根据最高温度和最低温度绘制图形。
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precips, c='red', alpha=0.5)

#设置图形的格式。
ax.set_title("Daily Rainfall Amounts - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rainfall (in)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.show()