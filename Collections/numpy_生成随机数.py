# numpy.random是numpy的一个子模块,
# 用于生成随机数，在新版的numpy中，有以下两种生成随机数的方式
# RandomState
# Generator

# 其中Generator是新版本推荐的方式，RandomState是之前旧版本的方式，
# 只是为了考虑兼容性，依然进行了保留

# 需要使用 print 命令来显示

import numpy as np

# RandomState
np.random.rand()

# Generator
rng = np.random.default_rng()
rng.random()

# 两种方式对应的方法大部分是相同的，但是也有小部分不一样，
# 在使用中需要注意，比如rand, randn等方法是RandomState独有的，
# 而integers方法是Generator独有的。

# 计算器模拟产生的随机数都是伪随机数，
# 通过设置随机数种子发生器，可以保证每次随机的结果都相同。

# 未设置，每次随机的结果不同
np.random.rand()

# 设置相同的seed, 可以保证重复性
np.random.seed(5)
np.random.rand()

rng = np.random.default_rng(1)
rng.random()

# 随机数的应用，主要有以下三种场景

# 1.  产生简单随机数
# 对于RandomState而言，有以下几种方法，示例如下

# rand函数
# 默认生成一个0到1之间，符合均匀分布的浮点数
np.random.rand()

# 设置数组的形状，1个参数表示1维数组
np.random.rand(2)

# 两个数组表示二维数组
np.random.rand(2, 2)

# sample函数
# 抽取0到1之间的随机数
np.random.sample((2, 2))

# random函数
# 抽取0到1之间的随机数
np.random.random((2, 2))

# randn函数
# 抽取标准正态分布的值
np.random.randn(2, 2)

# randint函数
# 从起始值和终止值之间随机抽取整数
# 默认的起始值为0
np.random.randint(9, 14, size=(2, 2))

# 在Generator中，则是提供了random和integers方法，示例如下
rng = np.random.default_rng()
rng.random()
rng.random(2)
rng.random((2, 2))
rng.integers(9, 14, size=(2, 2))

# 2. 从已有序列中进行随机抽样
# choice函数可以从一个序列中随机抽取其中的元素，支持有放回和无放回的抽样，默认为有放回的抽样，示例如下
a = np.arange(10)
np.random.choice(a, 2)
rng.choice(a, 2)

# shuffle函数可以随机打乱一个序列的顺序，示例如下
x = np.arange(10)
# print(x)
np.random.shuffle(x)
# print(x)
rng.shuffle(x)

# 3. 随机抽取符合特定分布的序列
# 支持非常多的分布，以正态分布为例，示例如下
np.random.normal(size=(2, 2))

rng.normal(size=(2, 2))

# 每个分布对应一个函数，常见的几种分布对应的函数如下
# binomial 二项分布
# chisquare 卡方分布
# normal 正态分布
# poisson 泊松分布
# standard_normal 标准正态分布
# uniform 均匀分布
