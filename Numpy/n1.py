#%%
# print("x")
import numpy as np

world_alcohol = np.genfromtxt(r"D:\src\数据分析\DataAnalysis\Numpy\world_alcohol.txt",delimiter=",", dtype=str,skip_header=1)
print(world_alcohol)
# arr = np.array([1, 2, 3, 4])
# print(arr.shape)

# 第二行第四列
uruguay_other_1986 = world_alcohol[1, 4]
print(uruguay_other_1986)

matrix = np.array([
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
])

# 取第三列
print(matrix[:, 2])
# 第一列和第三列
print(matrix[:,0:2])

veter = np.array([5, 10, 15, 20])
print(veter == 10)
print(matrix == 10)

equal_to_10 = (veter == 10)
print(veter[equal_to_10])
# 判断第0列有没有等于20的
second_column_20 = (matrix[:,0] == 20)
print(matrix[second_column_20, :])
# axis=1按行 =0按列
print(matrix.sum(axis=1))

print(np.arange(15))

a = np.arange(15).reshape(3, 5)
print(a)

print(np.arange(10, 30, 5))
print(np.random.random((2, 3)))

print(np.floor(10 * np.random.random((3, 5))))
print(np.floor(10 * np.random.random((3, 5))).ravel())

# hstack 两个矩阵相互叠加
# hsplit 按照行进行切分


# 矩阵的赋值 b=a b = a.view() b = a.copy()