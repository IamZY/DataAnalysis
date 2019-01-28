from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager


# font = {
#     "family":"MicroSoft YaHei",
#     "weight":"bold",
#     "size":"larger"
# }
#
# matplotlib.rc("font",**font)

my_font = font_manager.FontProperties(fname=r"c:\windows\fonts\simsun.ttc")



# 长短为20，8  dpi每英寸上像素点的个数
fig = plt.figure(figsize=(20,8),dpi=80)


x = range(0,120)
y = [random.randint(20,35) for i in range(0,120)]

# 调整x轴的刻度
_x = list(x)
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i-60) for i in range(60,120)]
plt.xticks(_x[::3],_xtick_labels[::3],rotation=45,fontproperties=my_font)
# plt.xlabel()

# 绘图
plt.plot(x,y)

plt.show()