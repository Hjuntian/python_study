# Python 数据结构完整笔记

本文档为**单一 Markdown 文件**，可直接整体复制使用，适合初学到进阶复习，不做章节分割文件，不插入无意义分隔符。

---

## 一、数据结构概述

数据结构用于**组织、存储和管理数据**，以便高效访问与修改。

Python 内置的核心数据结构包括：

* 数值类型（int, float, bool）
* 字符串（str）
* 列表（list）
* 元组（tuple）
* 集合（set, frozenset）
* 字典（dict）
* 其他：NoneType、bytes、bytearray

---

## 二、数值类型

### 1. int（整数）

```python
x = 10
y = -5
```

特点：

* 任意精度（不溢出）
* 支持常见算术运算

```python
x + y
x * 3
x // 2
x ** 2
```

---

### 2. float（浮点数）

```python
a = 3.14
b = 1.2e3
```

注意精度问题：

```python
0.1 + 0.2  # 0.30000000000000004
```

---

### 3. bool（布尔值）

```python
True
False
```

逻辑运算：

```python
True and False
True or False
not True
```

---

## 三、字符串（str）

### 1. 定义

```python
s1 = 'hello'
s2 = "world"
s3 = '''多行
字符串'''
```

---

### 2. 索引与切片

```python
s = "python"
s[0]      # 'p'
s[-1]     # 'n'
s[1:4]    # 'yth'
s[::-1]   # 反转
```

字符串**不可变**。

---

### 3. 常用方法

```python
s.upper()
s.lower()
s.strip()
s.replace('py', 'Py')
s.split('t')
```

---

## 四、列表（list）

### 1. 定义

```python
lst = [1, 2, 3, 'a', True]
```

列表是**有序、可变**的。

---

### 2. 访问与修改

```python
lst[0]
lst[1] = 100
```

---

### 3. 常用方法

```python
lst.append(4)
lst.extend([5, 6])
lst.insert(1, 'x')
lst.remove(2)
lst.pop()
lst.clear()
```

---

### 4. 切片

```python
lst[1:4]
lst[::-1]
```

---

### 5. 列表推导式

```python
[x * 2 for x in range(5)]
[x for x in range(10) if x % 2 == 0]
```

---

## 五、元组（tuple）

### 1. 定义

```python
t = (1, 2, 3)
```

单元素元组：

```python
t = (1,)
```

---

### 2. 特点

* 有序
* 不可变
* 可作为字典的 key

---

### 3. 解包

```python
a, b, c = (1, 2, 3)
```

---

## 六、集合（set）

### 1. 定义

```python
s = {1, 2, 3}
```

空集合：

```python
s = set()
```

---

### 2. 特点

* 无序
* 元素唯一
* 可变（frozenset 不可变）

---

### 3. 常用操作

```python
s.add(4)
s.remove(2)
```

集合运算：

```python
a | b   # 并集
a & b   # 交集
a - b   # 差集
a ^ b   # 对称差集
```

---

## 七、字典（dict）

### 1. 定义

```python
d = {'name': 'Tom', 'age': 18}
```

---

### 2. 访问与修改

```python
d['name']
d['age'] = 20
d['gender'] = 'male'
```

---

### 3. 常用方法

```python
d.keys()
d.values()
d.items()
d.get('score', 0)
d.pop('age')
```

---

### 4. 遍历

```python
for k in d:
    print(k, d[k])

for k, v in d.items():
    print(k, v)
```

---

### 5. 字典推导式

```python
{k: k*k for k in range(5)}
```

---

## 八、None 类型

```python
x = None
```

用于表示“空值 / 未定义”。

---

## 九、可变与不可变总结

| 类型    | 是否可变 |
| ----- | ---- |
| int   | 不可变  |
| float | 不可变  |
| str   | 不可变  |
| tuple | 不可变  |
| list  | 可变   |
| set   | 可变   |
| dict  | 可变   |

---

## 十、数据结构选择建议

* 顺序数据、频繁修改：list
* 不可修改、做 key：tuple
* 去重、集合运算：set
* 键值映射：dict
* 文本处理：str

---

## 十一、补充：浅拷贝与深拷贝

```python
import copy

a = [1, [2, 3]]
b = copy.copy(a)
c = copy.deepcopy(a)
```

---

## 十二、常见面试考点

* list 与 tuple 区别
* dict 为什么快
* set 去重原理
* 可变对象作为函数参数

---

完
