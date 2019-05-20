#%%
import matplotlib.pyplot as plt
import numpy as np

flg = plt.figure(figsize=(10, 6))
# 两行两列
ax1 = flg.add_subplot(2, 2, 1)
ax1 = flg.add_subplot(2, 2, 2)
ax1 = flg.add_subplot(2, 2, 4)

ax1.plot(np.random.randint(1,5,5),np.arange(5))

plt.show()

