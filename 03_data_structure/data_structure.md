# Python 数据结构完整笔记（初学 → 进阶复习）
> 本文为**单一 Markdown 文件**，系统覆盖 Python 常用与核心数据结构。
> 包含：特点、常用方法、解包（unpacking）、典型用法、性能与注意事项。
> 适合：零基础入门、系统复习、面试与工程实践查阅。
---
## 一、整体速览
| 类型 | 是否可变 | 是否有序 | 是否可重复 | 典型用途 |
| ------------------ | --------- | ------- | ----- | -------- |
| int / float / bool | 不可变 | — | — | 数值计算 |
| str | 不可变 | 是 | 是 | 文本处理 |
| list | 可变 | 是 | 是 | 通用容器 |
| tuple | 不可变 | 是 | 是 | 固定数据、解包 |
| set | 可变 | 否 | 否 | 去重、集合运算 |
| frozenset | 不可变 | 否 | 否 | 只读集合、字典键 |
| dict | 可变 | 是（3.7+） | 键不重复 | 映射关系 |
| bytes / bytearray | bytes 不可变 | 是 | 是 | 二进制数据 |
| collections | 视类型 | 视类型 | 视类型 | 专用结构 |
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
x + y  # 加法
x - y  # 减法
x * y  # 乘法
x / y # 浮点除
x // y # 整除
x % y # 取余
x ** y # 幂
```
### 3. 类型转换
```python
int("10")  # 字符串转整数
float("3.14")  # 字符串转浮点数
bool(0) # False  # 转换为布尔值
bool(1) # True  # 转换为布尔值
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
s.upper()  # 转换为大写
s.lower()  # 转换为小写
s.title()  # 首字母大写
s.strip()  # 去除两端空白
s.replace("world", "python")  # 替换子串
s.split()  # 按空白分割成列表
"-".join(["a", "b"])  # 连接列表成字符串
```
### 3. 索引与切片
```python
s[0]  # 获取第一个字符
s[-1]  # 获取最后一个字符
s[1:5]  # 获取子串
s[::-1] # 反转  # 反转字符串
```
### 4. 格式化
```python
name = "Tom"
age = 18
f"{name} is {age}"  # f-string 格式化
"{} is {}".format(name, age)  # format 方法格式化
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
a = [1, 2, 3]  # 直接创建
b = list("abc")  # 从可迭代对象创建
c = [i for i in range(5)]  # 列表推导式
```
### 3. 常用方法
```python
a.append(4)  # 添加元素到末尾
a.extend([5, 6])  # 扩展列表
a.insert(0, 0)  # 在指定位置插入
a.pop()  # 移除并返回末尾元素
a.remove(2)  # 移除第一个匹配元素
a.clear()  # 清空列表
a.sort()  # 排序
a.reverse()  # 反转
```
### 4. 索引与切片
```python
a[0]  # 获取第一个元素
a[-1]  # 获取最后一个元素
a[1:3]  # 获取子列表
a[::2]  # 每隔一个元素
```
### 5. 解包（unpacking）
```python
a = [1, 2, 3]
x, y, z = a  # 基本解包
first, *rest = a  # 带星号解包
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
a = (1, 2, 3)  # 直接创建
b = 1, 2, 3  # 省略括号创建
c = (1,) # 单元素必须加逗号  # 单元素元组
```
### 3. 解包（重点）
```python
x, y = (10, 20)  # 基本解包
x, y = y, x # 经典交换  # 交换变量
first, *mid, last = (1, 2, 3, 4)  # 带星号解包
```
### 4. 常用方法
```python
a.count(1)  # 计数元素出现次数
a.index(2)  # 查找元素索引
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
a = {1, 2, 3}  # 直接创建
b = set([1, 2, 2, 3])  # 从可迭代对象创建
```
### 3. 常用方法
```python
a.add(4)  # 添加元素
a.remove(2)  # 移除元素（不存在则报错）
a.discard(10)  # 移除元素（不存在不报错）
a.pop()  # 移除并返回任意元素
```
### 4. 集合运算
```python
a | b # 并集  # 并集
a & b # 交集  # 交集
a - b # 差集  # 差集
a ^ b # 对称差集  # 对称差集
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
a = frozenset([1, 2, 3])  # 创建不可变集合
```
---
## 八、字典（dict）
### 1. 特点
* 键值映射
* 键必须不可变
* 3.7+ 保持插入顺序
### 2. 创建
```python
a = {"name": "Tom", "age": 18}  # 直接创建
b = dict(x=1, y=2)  # 使用 dict 函数创建
```
### 3. 常用方法
```python
a["name"]  # 通过键访问值
a.get("score", 0)  # 通过键获取值，默认值
a.keys()  # 获取所有键
a.values()  # 获取所有值
a.items()  # 获取键值对
a.update({"age": 20})  # 更新字典
a.pop("age")  # 移除键并返回值
```
### 4. 遍历
```python
for k, v in a.items():
    print(k, v)  # 遍历键值对
```
### 5. 解包
```python
d = {"a": 1, "b": 2}
{x: y for x, y in d.items()}  # 字典推导式
```
### 6. 注意事项
* 使用 `get` 避免 KeyError
* dict 查找平均 O(1)
---
## 九、bytes / bytearray
### 1. bytes（不可变）
```python
b = b"abc"  # 创建 bytes 对象
```
### 2. bytearray（可变）
```python
ba = bytearray(b"abc")  # 创建 bytearray 对象
ba[0] = 100  # 修改元素
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
d = defaultdict(int)  # 创建默认字典，默认值为 int
d['a'] += 1  # 访问不存在键自动创建
```
### 2. Counter
```python
from collections import Counter
Counter("abca")  # 计数元素出现次数
```
### 3. deque
```python
from collections import deque
d = deque([1, 2, 3])  # 创建双端队列
d.appendleft(0)  # 左侧添加
d.pop()  # 右侧移除
```
### 4. namedtuple
```python
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])  # 创建命名元组类
p = Point(1, 2)  # 实例化
```
---
## 十一、解包（Unpacking）总整理
```python
a, b = 1, 2  # 基本解包
a, b = b, a  # 交换变量
x, *y = [1, 2, 3, 4]  # 带星号解包
func(*args, **kwargs)  # 函数参数解包
```
---
## 十二、可变 vs 不可变（核心理解）
| 类型 | 是否可变 |
| ------------------ | ---- |
| int / float / bool | 否 |
| str | 否 |
| tuple | 否 |
| list | 是 |
| set | 是 |
| dict | 是 |
* 不可变对象适合做 key
* 可变对象注意引用传递
---
## 十三、常见陷阱与最佳实践
1. 不要用 `is` 比较值
2. 默认参数不要用可变对象
```python
def func(x, lst=None):  # 示例函数，避免可变默认参数
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
