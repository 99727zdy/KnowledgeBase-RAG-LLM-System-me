"""01 变量与类型 —— Python 最基础的积木。"""

# 变量无需先声明类型，赋值即创建
name = "知识库" # 字符串
chunk_size = 1000 # 整数
score = 0.95 # 浮点数
is_ready = True # 布尔值
empty_value = None  # 表示「没有值」

print(name, chunk_size, score, is_ready, empty_value)

# 查看类型
print(type(name))       # <class 'str'>
print(type(chunk_size)) # <class 'int'>

# 类型转换（必须显式转换）
text_num = "42"
num = int(text_num)
print(num + 1)          # 43
print(str(100) + "KB")  # 100KB
print(bool(0), bool(1), bool(""))  # False True False

# 字符串常用操作（项目里到处都有）
s = "  hello RAG  "
print(s.strip())        # 去掉首尾空白，类似 knowledge_base 里 line.strip()
print(s.upper())        # 转换为大写，类似 knowledge_base 里 line.upper()
print("RAG" in s)       # True
