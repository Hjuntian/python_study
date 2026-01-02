
````md

## 1️⃣ 核心属性

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

# 形状 (行数, 列数)
print(arr.shape)  # 输出: (2, 3)

# 维度
print(arr.ndim)   # 输出: 2

# 元素总数
print(arr.size)   # 输出: 6

# 数据类型
print(arr.dtype)  # 输出: int64 (或 int32)

# 每个元素占用字节大小
print(arr.itemsize)  # 输出: 8 (int64 每个元素占8字节)

# 数组总占用字节
print(arr.nbytes)    # 输出: 48 = 6 * 8
````

---

## 2️⃣ 创建数组

```python
# arange: 类似 range，但返回 ndarray
arr = np.arange(0, 10, 2)
print(arr)  # 输出: [0 2 4 6 8]

# linspace: 在指定区间生成等间隔数值
arr = np.linspace(0, 1, 5)
print(arr)  # 输出: [0.   0.25 0.5  0.75 1.  ]

# zeros / ones / full: 创建指定形状数组
arr = np.zeros((2,3))
print(arr)
# [[0. 0. 0.]
#  [0. 0. 0.]]

arr = np.ones((2,3))
print(arr)
# [[1. 1. 1.]
#  [1. 1. 1.]]

arr = np.full((2,3), 7)
print(arr)
# [[7 7 7]
#  [7 7 7]]

# identity / eye: 单位矩阵
arr = np.eye(3)
print(arr)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
```

---

## 3️⃣ 基本运算

```python
a = np.array([1,2,3])
b = np.array([4,5,6])

# 加减乘除
print(a + b)  # 输出: [5 7 9]
print(a * b)  # 输出: [ 4 10 18]
print(a - b)  # 输出: [-3 -3 -3]
print(a / b)  # 输出: [0.25 0.4  0.5 ]

# 幂运算
print(a ** 2)  # 输出: [1 4 9]

# 广播机制: 自动扩展维度进行运算
c = np.array([[1],[2]])
print(c + np.array([10,20,30]))
# 输出:
# [[11 21 31]
#  [12 22 32]]
```

---

## 4️⃣ 数组属性操作

```python
arr = np.array([[1,2,3],[4,5,6]])

# reshape: 改变数组形状
arr2 = arr.reshape(3,2)
print(arr2)
# [[1 2]
#  [3 4]
#  [5 6]]

# flatten / ravel: 展平为 1D
flat = arr.flatten()
print(flat)  # 输出: [1 2 3 4 5 6]
flat2 = arr.ravel()  # 返回视图，节省内存

# transpose / T: 转置
print(arr.T)
# [[1 4]
#  [2 5]
#  [3 6]]
```

---

## 5️⃣ 索引与切片

```python
arr = np.array([[1,2,3],[4,5,6]])

# 单个元素
print(arr[0,1])  # 输出: 2

# 行/列切片
print(arr[0,:])  # 输出: [1 2 3] 第一行
print(arr[:,1])  # 输出: [2 5] 第二列

# 布尔索引
mask = arr > 3
print(arr[mask])  # 输出: [4 5 6]

# fancy index: 同时指定行列索引
print(arr[[0,1],[2,0]])  # 输出: [3 4] -> arr[0,2], arr[1,0]
```

---

## 6️⃣ 常用统计方法

```python
arr = np.array([[1,2,3],[4,5,6]])

print(arr.sum())          # 输出: 21
print(arr.sum(axis=0))    # 列求和: [5 7 9]
print(arr.sum(axis=1))    # 行求和: [6 15]

print(arr.mean())         # 输出: 3.5
print(arr.mean(axis=0))   # 列平均: [2.5 3.5 4.5]
print(arr.min())          # 输出: 1
print(arr.max())          # 输出: 6
print(arr.argmin())       # 输出: 0 -> 展平后最小值索引
print(arr.argmax())       # 输出: 5 -> 展平后最大值索引
print(arr.cumsum())       # 输出: [ 1  3  6 10 15 21] 累积和
print(arr.cumprod())      # 输出: [  1   2   6  24 120 720] 累积积
```

---

## 7️⃣ 排序与唯一值

```python
arr = np.array([3,1,2,3,4])

print(np.sort(arr))      # 排序，返回新数组: [1 2 3 3 4]
print(arr)               # 原数组不变: [3 1 2 3 4]

arr.sort()               # 原地排序
print(arr)               # 输出: [1 2 3 3 4]

print(np.unique(arr))    # 去重并排序: [1 2 3 4]
```

---

## 8️⃣ 随机数生成（numpy.random）

```python
# 随机浮点 [0,1)
rand_arr = np.random.rand(3)
print(rand_arr)  # 示例: [0.5488135  0.71518937 0.60276338]

# 正态分布
norm_arr = np.random.randn(3)
print(norm_arr)  # 示例: [-0.0452  0.9325  0.1203]

# 整数 [low, high)
int_arr = np.random.randint(1, 10, size=5)
print(int_arr)  # 示例: [3 7 1 9 4]

# 打乱数组
arr = np.array([1,2,3,4])
np.random.shuffle(arr)
print(arr)  # 示例: [3 1 4 2]

# 从数组中随机抽样
print(np.random.choice(arr, size=3, replace=True))  # 示例: [1 3 4]
```

---

## 9️⃣ 线性代数

```python
A = np.array([[1,2],[3,4]])

# 矩阵乘法
B = np.array([[2,0],[1,2]])
print(A @ B)  # 输出: [[4 4]
              #       [10 8]]
# 或 np.dot(A,B)

# 转置
print(A.T)
# [[1 3]
#  [2 4]]

# 逆矩阵
print(np.linalg.inv(A))
# [[-2.   1. ]
#  [ 1.5 -0.5]]

# 行列式
print(np.linalg.det(A))  # 输出: -2.0
```

---

## 🔹 小结

* **属性**：`shape, ndim, size, dtype, itemsize, nbytes`
* **创建数组**：`arange, linspace, zeros, ones, full, eye`
* **运算**：加减乘除、广播
* **操作**：`reshape, flatten, ravel, transpose`
* **索引**：切片、布尔索引、fancy index
* **统计**：`sum, mean, min, max, argmin, argmax, cumsum, cumprod`
* **排序/去重**：`sort, unique`
* **随机**：`rand, randn, randint, shuffle, choice`
* **线代**：矩阵乘法、逆矩阵、行列式


