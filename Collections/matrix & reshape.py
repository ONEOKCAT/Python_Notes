import numpy as np

# reshape 的用法: 即将原始矩阵按重新定义的行列数进行排列，但要满足倍数关系
a = np.array([1, 2, 3, 4])
b = np.array((5, 6, 7, 8))
c = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])
d = a.reshape((2, 2))
# print(d)
# [[1 2]
#  [3 4]]

e = a.reshape((-1, 1))
# print(e)
# [[1]
#  [2]s
#  [3]
#  [4]]

f = c.reshape(2, 6)  # 也可以使用(4,3)，满足倍数关系，e.g.使用 (2,5)则会报错
# print(f)
# [[ 1  2  3  4  4  5]
#  [ 6  7  7  8  9 10]]
