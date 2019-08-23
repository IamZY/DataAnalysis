# 数据分析

```python
import pandas as pd
import scipy.stats as ss
import matplotlib
%matplotlib inline

matplotlib.rcParams["font.sans-serif"] = ["SimHei"]
```

## 数值变量

+ 单个分类变量 呈现原始频数

  简单条图  点图

+ 单个分类变量 呈现数据构成比

  饼图 百分条图

+ 单个分类变量 呈现原始频数/构成比

  Pareto图  条图和线图的结合

+ 单个分类变量 各种特殊图形

  圆环图 气泡图

+ 单个数值变量 显示原始数据分布

  条带图 Strip Plot

  地毯图 Rug Plot

+ 单个数值变量显示汇总后的数据分布

  直方图

  茎叶图

+ 单个数值变量显示汇总后数据分布

  箱图

  增强箱图

+ 单个数值变量显示数据分布特征

  KDE 核密度估计

  提琴图 Violin Plot

+ 单个数值变量 和假设的分布特征相比较

  P-P图

  Q-Q图

## 分类变量

+ 分组条图 行面板图 列面板图
+ 分段条图 堆积条图
+ 百分条图 马赛克图
+ 树状图（单元格的大小 单元格的颜色深浅）
+ 复合饼图 圆环图

## 数值变量和分类变量

+ 条图
+ 面积图
+ 线图
+ 散点图
+ HexPlot/SunFlower
+ KDE 等高线图

## 双变量+更多的分类变量

组合统计图

双轴图

## 多个连续变量

图形矩阵

## 统计地图

Tableau

# 数据挖掘

+ 加载数据，观察问题
+ 针对问题给出解决方案
+ 数据集切分
+ 评估方法对比
+ 构建模型
+ 建模结果分析
+ 方案效果对比

## 加载数据

+ 数据标准化

  公式：$(x-u)/s$

  ```python
  # 数据标准化处理
  from sklearn.preprocessing import StandardScaler
  # reshape 一维数组化二维数组
  data["normAmount"] = StandardScaler().fit_transform(data["Amount"].values.reshape(-1,1))
  
  data = data.drop(["Time","Amount"],axis = 1)
  data.head()
  ```

## 数据集划分

+ 训练集 验证集 测试集

+ 随机分











