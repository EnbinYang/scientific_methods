import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

#设置图表标题并给坐标轴加上标签
ax.set_title("Square numbers", fontsize=18)
ax.set_xlabel("values", fontsize=14)
ax.set_ylabel("Squares", fontsize=14)

#设置刻度标记的大小
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()