import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

#设置图表标题并给坐标轴加上标签
ax.set_title("Square numbers", fontsize=18)
ax.set_xlabel("values", fontsize=14)
ax.set_ylabel("Squares", fontsize=14)

#设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)

#设置每个坐标轴的取值范围
ax.axis([0, 1100, 0, 1100000])
plt.savefig('squares_plot.png', bbox_inches='tight')