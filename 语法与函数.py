# sorted()和lamda表达式
data = ["apple", "hi", "banana", "a"]

result = sorted(data, key=lambda x: len(x))
# 等价于
def by_len(x):
    return len(x)

result = sorted(data, key=by_len)

# items() 是字典（dict）的方法
d = {"a": 1, "b": 2}
print(d.items())
# 输出
dict_items([('a', 1), ('b', 2)])

# 按 value 排序字典
scores = {"math": 90, "english": 85, "chinese": 95}

res = sorted(scores.items(), key=lambda x: x[1])
# 输出
[('english', 85), ('math', 90), ('chinese', 95)]
