"""01 列表与元组。"""

# 列表：可变、有序（项目里：知识块、消息列表）
chunks = ["段落A", "段落B"]
chunks.append("段落C")  # 在列表末尾添加一个元素
chunks.extend(["段落D", "段落E"])  # 在列表末尾一次性添加多个元素
print(chunks)
print(len(chunks), chunks[0], chunks[-1])  # 长度、第一个、最后一个

# 切片：chunks[起始:结束]，含起始、不含结束
print(chunks[1:3])  # 取下标 1、2 -> ['段落B', '段落C']

# enumerate：同时拿到下标 i 和元素 c
for i, c in enumerate(chunks):
    print(i, c)

# 元组：不可变（函数多返回值本质常是元组）
# 解包时：左边变量个数必须等于右边元素个数
point = (10, 20)
x, y = point
print(x, y)

# ----- 列表拷贝 -----
# b = a：只是起了个别名，a 和 b 指向同一份列表
a = [1, 2]
b = a
b.append(3)
print(a)  # [1, 2, 3]  改 b 等于改 a
print(b)  # [1, 2, 3]

# copy()：复制出一份新列表，之后改 c 不会影响 a
c = a.copy()
print(c)  # [1, 2, 3]

# a[:]：切片拷贝，效果和 a.copy() 基本一样
c = a[:]
print(c)  # [1, 2, 3]

c.append(4)
print(c)  # [1, 2, 3, 4]
print(a)  # [1, 2, 3]  a 不会变

# ----- == 与 is（Python 没有 ===）-----
# == 比的是内容；is 比的是是不是同一块内存里的同一个对象
p = [1, 2]
q = [1, 2]
print(p == q)  # True：内容一样
print(p is q)  # False：不是同一个对象

r = p
print(r is p)  # True：r 和 p 指向同一份列表

# 判断 None 常用 is，不用 ==
x = None
print(x is None)      # True
print(x is not None)  # False
