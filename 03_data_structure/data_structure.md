# Python 数据结构完整笔记（初学 → 进阶复习）

> 本文为**单一 Markdown 文件**，系统覆盖 Python 常用与核心数据结构。
> 包含：特点、常用方法、解包（unpacking）、典型用法、性能与注意事项。
> 适合：零基础入门、系统复习、面试与工程实践查阅。

---

## 一、整体速览

| 类型                 | 是否可变      | 是否有序    | 是否可重复 | 典型用途     |
| ------------------ | --------- | ------- | ----- | -------- |
| int / float / bool | 不可变       | —       | —     | 数值计算     |
| str                | 不可变       | 是       | 是     | 文本处理     |
| list               | 可变        | 是       | 是     | 通用容器     |
| tuple              | 不可变       | 是       | 是     | 固定数据、解包  |
| set                | 可变        | 否       | 否     | 去重、集合运算  |
| frozenset          | 不可变       | 否       | 否     | 只读集合、字典键 |
| dict               | 可变        | 是（3.7+） | 键不重复  | 映射关系     |
| bytes / bytearray  | bytes 不可变 | 是       | 是     | 二进制数据    |
| collections        | 视类型       | 视类型     | 视类型   | 专用结构     |

---

## 二、数值类型（int / float / bool）

### 1. 特点

* **不可变对象**（immutable）
* 参与运算会生成新对象
* bool 是 int 的子类：True == 1，False == 0

### 2. 常用操作

```python
x = 10
y = 3

x + y
x - y
x * y
x / y      # 浮点除
x // y     # 整除
x % y      # 取余
x ** y     # 幂
```

### 3. 类型转换

```python
int("10")
float("3.14")
bool(0)     # False
bool(1)     # True
```

### 4. 注意事项

* 浮点数存在**精度误差**（建议使用 decimal）
* 不要用 `is` 判断数值相等

---

## 三、字符串（str）

### 1. 特点

* 不可变
* 有序
* 支持切片

### 2. 常用方法

```python
s = "hello world"

s.upper()
s.lower()
s.title()
s.strip()
s.replace("world", "python")
s.split()
"-".join(["a", "b"])
```

### 3. 索引与切片

```python
s[0]
s[-1]
s[1:5]
s[::-1]   # 反转
```

### 4. 格式化

```python
name = "Tom"
age = 18

f"{name} is {age}"
"{} is {}".format(name, age)
```

### 5. 注意事项

* 频繁拼接字符串建议用 list + join
* 修改字符串本质是创建新对象

---

## 四、列表（list）

### 1. 特点

* 可变
* 有序
* 可存放任意类型

### 2. 创建方式

```python
a = [1, 2, 3]
b = list("abc")
c = [i for i in range(5)]
```

### 3. 常用方法

```python
a.append(4)
a.extend([5, 6])
a.insert(0, 0)

a.pop()
a.remove(2)
a.clear()

a.sort()
a.reverse()
```

### 4. 索引与切片

```python
a[0]
a[-1]
a[1:3]
a[::2]
```

### 5. 解包（unpacking）

```python
a = [1, 2, 3]
x, y, z = a

first, *rest = a
```

### 6. 注意事项

* `a = b` 只是引用复制
* 复制列表使用：`a.copy()` 或 `a[:]`
* list 查找是 O(n)

---

## 五、元组（tuple）

### 1. 特点

* 不可变
* 有序
* 常用于“只读数据”

### 2. 创建

```python
a = (1, 2, 3)
b = 1, 2, 3
c = (1,)   # 单元素必须加逗号
```

### 3. 解包（重点）

```python
x, y = (10, 20)

x, y = y, x   # 经典交换

first, *mid, last = (1, 2, 3, 4)
```

### 4. 常用方法

```python
a.count(1)
a.index(2)
```

### 5. 注意事项

* 元组不可变，但若内部包含 list，其内部元素可变

---

## 六、集合（set）

### 1. 特点

* 无序
* 不重复
* 可变

### 2. 创建

```python
a = {1, 2, 3}
b = set([1, 2, 2, 3])
```

### 3. 常用方法

```python
a.add(4)
a.remove(2)
a.discard(10)
a.pop()
```

### 4. 集合运算

```python
a | b   # 并集
a & b   # 交集
a - b   # 差集
a ^ b   # 对称差集
```

### 5. 注意事项

* 不能包含可变对象（如 list、dict）
* 常用于去重、成员判断（O(1)）

---

## 七、不可变集合（frozenset）

### 1. 特点

* 不可变
* 可作为 dict 的 key

```python
a = frozenset([1, 2, 3])
```

---

## 八、字典（dict）

### 1. 特点

* 键值映射
* 键必须不可变
* 3.7+ 保持插入顺序

### 2. 创建

```python
a = {"name": "Tom", "age": 18}
b = dict(x=1, y=2)
```

### 3. 常用方法

```python
a["name"]
a.get("score", 0)

a.keys()
a.values()
a.items()

a.update({"age": 20})

a.pop("age")
```

### 4. 遍历

```python
for k, v in a.items():
    print(k, v)
```

### 5. 解包

```python
d = {"a": 1, "b": 2}
{x: y for x, y in d.items()}
```

### 6. 注意事项

* 使用 `get` 避免 KeyError
* dict 查找平均 O(1)

---

## 九、bytes / bytearray

### 1. bytes（不可变）

```python
b = b"abc"
```

### 2. bytearray（可变）

```python
ba = bytearray(b"abc")
ba[0] = 100
```

### 3. 使用场景

* 文件
* 网络
* 编码解码

---

## 十、collections 模块（重点进阶）

### 1. defaultdict

```python
from collections import defaultdict
d = defaultdict(int)
d['a'] += 1
```

### 2. Counter

```python
from collections import Counter
Counter("abca")
```

### 3. deque

```python
from collections import deque
d = deque([1, 2, 3])
d.appendleft(0)
d.pop()
```

### 4. namedtuple

```python
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
```

---

## 十一、解包（Unpacking）总整理

```python
a, b = 1, 2

a, b = b, a

x, *y = [1, 2, 3, 4]

func(*args, **kwargs)
```

---

## 十二、可变 vs 不可变（核心理解）

| 类型                 | 是否可变 |
| ------------------ | ---- |
| int / float / bool | 否    |
| str                | 否    |
| tuple              | 否    |
| list               | 是    |
| set                | 是    |
| dict               | 是    |

* 不可变对象适合做 key
* 可变对象注意引用传递

---

## 十三、常见陷阱与最佳实践

1. 不要用 `is` 比较值
2. 默认参数不要用可变对象

```python
def func(x, lst=None):
    if lst is None:
        lst = []
```

3. 多用推导式，但避免过度复杂
4. 数据量大优先考虑 set / dict

---

## 十四、总结

* list：通用容器
* tuple：安全、解包
* dict：核心数据结构
* set：去重、集合逻辑
* collections：专业场景利器

---

**本文件可直接复制、提交 GitHub、作为长期 Python 数据结构速查文档使用。**
