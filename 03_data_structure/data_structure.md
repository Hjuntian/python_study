# Python 数据结构笔记

Python 常用的内置数据结构包括：
list（列表）、tuple（元组）、dict（字典）、set（集合）

---

## 一、list（列表）

### 1. 定义
列表是有序、可变的数据结构，用于存储多个元素。

```python
nums = [1, 2, 3, 4]
names = ["Tom", "Jack", "Alice"]
mixed = [1, "hello", True]
2. 常用操作
python
复制代码
nums.append(5)      # 添加元素
nums.insert(1, 100) # 指定位置插入
nums.remove(3)      # 删除指定值
nums.pop()          # 删除末尾元素
访问元素：

python
复制代码
print(nums[0])
print(nums[-1])
3. 遍历列表
python
复制代码
for x in nums:
    print(x)
python
复制代码
for i, v in enumerate(nums):
    print(i, v)
4. 列表切片
python
复制代码
nums = [0, 1, 2, 3, 4]
print(nums[1:4])
print(nums[::-1])
二、tuple（元组）
1. 定义
元组是有序、不可变的数据结构。

python
复制代码
point = (10, 20)
single = (1,)
2. 特点
元素不可修改

访问速度快

常用于表示固定结构的数据

python
复制代码
x, y = point
print(x, y)
三、dict（字典）
1. 定义
字典是由键值对组成的数据结构。

python
复制代码
student = {
    "name": "Tom",
    "age": 18,
    "score": 90
}
2. 访问与修改
python
复制代码
print(student["name"])

student["age"] = 19
student["gender"] = "male"
3. 常用方法
python
复制代码
student.get("score")
student.keys()
student.values()
student.items()
4. 遍历字典
python
复制代码
for key in student:
    print(key, student[key])
python
复制代码
for k, v in student.items():
    print(k, v)
四、set（集合）
1. 定义
集合是无序、不重复的元素集合。

python
复制代码
nums = {1, 2, 3, 3, 2}
print(nums)
2. 常用操作
python
复制代码
nums.add(4)
nums.remove(2)
3. 集合运算
python
复制代码
a = {1, 2, 3}
b = {3, 4, 5}

print(a & b)
print(a | b)
print(a - b)
五、数据结构对比
类型	有序	可变	是否重复
list	是	是	是
tuple	是	否	是
dict	是（3.7+）	是	key 不重复
set	否	是	否

六、使用场景总结
list：顺序存储、频繁修改

tuple：固定结构、函数返回值

dict：映射关系、对象属性

set：去重、集合运算
