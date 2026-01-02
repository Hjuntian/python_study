# sorted()和lamda表达式
data = ["apple", "hi", "banana", "a"]

result = sorted(data, key=lambda x: len(x))
# 等价于
def by_len(x):
    return len(x)

result = sorted(data, key=by_len)

---------------

# items() 是字典（dict）的方法
d = {"a": 1, "b": 2}
print(d.items())
# 输出
dict_items([('a', 1), ('b', 2)])


---------------

# 按 value 排序字典
scores = {"math": 90, "english": 85, "chinese": 95}

res = sorted(scores.items(), key=lambda x: x[1])
# 输出
[('english', 85), ('math', 90), ('chinese', 95)]


# ----------------------------
# len() —— 返回对象中元素的个数
s = "abc"
lst = [1, 2, 3]
print("len(s) =", len(s))    # 3
print("len(lst) =", len(lst))  # 3

# 对 dict，返回键的数量
d = {"a":1, "b":2}
print("len(d) =", len(d))  # 2

# ----------------------------
# type() —— 查看对象类型
print(type(10))       # <class 'int'>
print(type([1, 2]))   # <class 'list'>

# ----------------------------
# isinstance() —— 判断对象类型
print(isinstance(10, int))          # True
print(isinstance(True, int))        # True
print(isinstance(3.14, (int,float))) # True

# ----------------------------
# print() —— 输出
print("hello", end=" ")
print("world")  # 输出: hello world

# ----------------------------
# input() —— 从标准输入读取
# x = input("请输入：")
# print(type(x))  # str
# 注意返回值永远是字符串，需要手动转换

# ----------------------------
# int() / float() / str() —— 类型转换
print(int("10"))      # 10
print(float("3.14"))  # 3.14
print(str(100))       # "100"

# ----------------------------
# range() —— 生成整数序列
for i in range(1, 5):
    print("range:", i)

# ----------------------------
# enumerate() —— 获取索引和值
lst = ["a", "b", "c"]
for i, v in enumerate(lst):
    print("enumerate:", i, v)

# ----------------------------
# sum() —— 求和
lst = [1, 2, 3]
print("sum:", sum(lst))  # 6

# ----------------------------
# max() / min() —— 最大值/最小值
lst = [3, 1, 5]
print("max:", max(lst))  # 5
print("min:", min(lst))  # 1
# 支持 key 参数
print("max abs:", max([-3, 2, -5], key=abs))  # 5

# ----------------------------
# sorted() —— 返回排序后的新列表
lst = [3, 1, 2]
new_lst = sorted(lst)
print("sorted:", new_lst)  # [1, 2, 3]

# ----------------------------
# abs() —— 绝对值
print("abs:", abs(-5))  # 5

# ----------------------------
# zip() —— 多序列打包
a = [1, 2]
b = [3, 4]
print("zip:", list(zip(a, b)))  # [(1, 3), (2, 4)]

# ----------------------------
# map() —— 序列元素映射函数
nums = [1, 2, 3]
res = list(map(lambda x: x*2, nums))
print("map:", res)  # [2, 4, 6]

# ----------------------------
# filter() —— 过滤序列元素
nums = [1, 2, 3, 4]
res = list(filter(lambda x: x % 2 == 0, nums))
print("filter:", res)  # [2, 4]

# ----------------------------
# any() / all() —— 布尔运算
print("any:", any([0, 1, 0]))  # True
print("all:", all([1, 1, 0]))  # False

# ----------------------------
# map / filter / zip 偏函数式，理解即可
# 切片、range、enumerate 都遵循左闭右开
