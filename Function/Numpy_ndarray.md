
# NumPy ndarray 常用方法与属性笔记

```python
import numpy as np
```

---

## 1. 创建 ndarray

```python
# 从列表创建
a = np.array([1, 2, 3])
print(a)             # 输出: [1 2 3]
print(type(a))       # 输出: <class 'numpy.ndarray'>

# 多维数组
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
# 输出:
# [[1 2 3]
#  [4 5 6]]

# 创建全零数组
c = np.zeros((2, 3))
print(c)
# 输出:
# [[0. 0. 0.]
#  [0. 0. 0.]]

# 创建全一数组
d = np.ones((3, 2))
print(d)
# 输出:
# [[1. 1.]
#  [1. 1.]
#  [1. 1.]]

# 创建单位矩阵
e = np.eye(3)
print(e)
# 输出:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# 创建等间隔数组
f = np.arange(0, 10, 2)  # start=0, stop=10, step=2
print(f)  # 输出: [0 2 4 6 8]

# 创建等间隔数组（包括终点）
g = np.linspace(0, 1, 5)  # 0到1等分5份
print(g)  # 输出: [0.   0.25 0.5  0.75 1.  ]

# 随机数组
h = np.random.rand(2, 3)  # [0,1)之间均匀分布
print(h)

i = np.random.randint(0, 10, size=(2, 3))  # 整数随机
print(i)
```

---

## 2. ndarray 常用属性

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)    # 输出: (2, 3) 维度
print(arr.ndim)     # 输出: 2 维数
print(arr.size)     # 输出: 6 元素总数
print(arr.dtype)    # 输出: int64 数据类型
print(arr.itemsize) # 输出: 8 每个元素字节大小
print(arr.data)     # 输出: <memory at 0x...> 数据缓冲区
```

---

## 3. ndarray 基本运算

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 加减乘除
print(a + b)   # [5 7 9]
print(a - b)   # [-3 -3 -3]
print(a * b)   # [4 10 18]
print(a / b)   # [0.25 0.4 0.5]

# 幂运算
print(a ** 2)  # [1 4 9]

# 比较
print(a > 1)   # [False  True  True]

# 矩阵乘法
X = np.array([[1, 2], [3, 4]])
Y = np.array([[5, 6], [7, 8]])
print(X.dot(Y))
# 输出:
# [[19 22]
#  [43 50]]
```

---

## 4. ndarray 索引与切片

```python
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

# 单元素访问
print(arr[0, 1])  # 输出: 2

# 行切片
print(arr[1, :])  # 输出: [4 5 6]

# 列切片
print(arr[:, 2])  # 输出: [3 6 9]

# 多维切片
print(arr[0:2, 1:3])
# 输出:
# [[2 3]
#  [5 6]]

# 布尔索引
print(arr[arr > 5])  # 输出: [6 7 8 9]

# 整数数组索引
print(arr[[0,2], [1,2]])  # 输出: [2 9]
```

---

## 5. ndarray 形状操作

```python
arr = np.arange(6)  # [0 1 2 3 4 5]

# reshape
print(arr.reshape((2,3)))
# [[0 1 2]
#  [3 4 5]]

# flatten / ravel
b = np.array([[1,2],[3,4]])
print(b.flatten())  # [1 2 3 4]
print(b.ravel())    # [1 2 3 4] (返回视图)

# 转置
print(b.T)
# [[1 3]
#  [2 4]]

# 改变维度
c = np.array([1,2,3,4])
print(c[:, np.newaxis])
# [[1]
#  [2]
#  [3]
#  [4]]
```

---

## 6. ndarray 统计方法

```python
arr = np.array([[1,2,3],[4,5,6]])

print(arr.sum())       # 21 总和
print(arr.sum(axis=0)) # [5 7 9] 按列
print(arr.sum(axis=1)) # [6 15] 按行

print(arr.mean())      # 3.5 平均值
print(arr.mean(axis=0)) # [2.5 3.5 4.5]
print(arr.std())       # 标准差
print(arr.var())       # 方差
print(arr.min())       # 最小值
print(arr.max())       # 最大值
print(arr.argmin())    # 返回展平后最小值索引
print(arr.argmax())    # 返回展平后最大值索引
```

---

## 7. ndarray 通用函数 (ufunc)

```python
arr = np.array([0, np.pi/2, np.pi])

print(np.sin(arr))   # [0. 1. 0.]
print(np.cos(arr))   # [ 1.  0. -1.]
print(np.exp(arr))   # [1.  4.81047738 23.14069263]
print(np.log(np.array([1, np.e, np.e**2]))) # [0. 1. 2.]

# 四舍五入
arr2 = np.array([1.2, 2.5, 3.7])
print(np.round(arr2)) # [1. 2. 4.]
```

---

## 8. ndarray 拼接与分割

```python
a = np.array([1,2,3])
b = np.array([4,5,6])

# 拼接
print(np.concatenate([a,b]))   # [1 2 3 4 5 6]

# 堆叠
print(np.vstack([a,b]))
# [[1 2 3]
#  [4 5 6]]

print(np.hstack([a,b]))  # [1 2 3 4 5 6]

# 分割
c = np.arange(10)
print(np.split(c, 2))    # [array([0,1,2,3,4]), array([5,6,7,8,9])]
print(np.array_split(c, 3)) # 可不均分
```

---

## 9. ndarray 排序与唯一值

```python
arr = np.array([3,1,2,3,4,1])

# 排序
print(np.sort(arr))   # [1 1 2 3 3 4]

# 原地排序
arr.sort()
print(arr)            # [1 1 2 3 3 4]

# 唯一值
print(np.unique(arr)) # [1 2 3 4]
```

---

## 10. ndarray 条件与逻辑操作

```python
arr = np.array([1,2,3,4,5])

# 条件筛选
print(arr[arr>3])       # [4 5]

# any / all
print(np.any(arr>4))    # True
print(np.all(arr>0))    # True

# 逻辑运算
bool_arr = (arr > 2) & (arr < 5)
print(bool_arr)         # [False False  True  True False]
```

---

## 11. ndarray 复制与视图

```python
arr = np.array([1,2,3])

# 视图
v = arr.view()
v[0] = 100
print(arr)  # [100   2   3] 原数组也变了

# 深拷贝
c = arr.copy()
c[1] = 200
print(arr)  # [100 2 3] 原数组不变
```

---

## 12. ndarray 线性代数

```python
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

# 点积
print(np.dot(A,B))
# [[19 22]
#  [43 50]]

# 转置
print(A.T)

# 逆矩阵
print(np.linalg.inv(A))
# [[-2.   1. ]
#  [ 1.5 -0.5]]

# 行列式
print(np.linalg.det(A))  # -2.0

# 特征值与特征向量
eigvals, eigvecs = np.linalg.eig(A)
print(eigvals)
print(eigvecs)
```


---
