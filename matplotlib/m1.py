from matplotlib import pyplot as plt


# 长短为20，8  dpi每英寸上像素点的个数
fig = plt.figure(figsize=(20,8),dpi=80)


x = range(2,26,2)
y = [15,13,14.5,17,20,26,27,22,18,15,11,32]

# 绘图
plt.plot(x,y)

# 绘制x轴的刻度
_xtick_labels = [i/2 for i in range(4,48)]

plt.xticks(_xtick_labels[::3])
plt.yticks(range(min(y),max(y)+1))

plt.savefig("./t1.png")

plt.show()