"""02 运算符与输入输出。"""

a, b = 10, 3
print(a + b, a - b, a * b, a / b)   # / 得到浮点
print(a // b, a % b, a ** 2)        # 整除、取余、幂

# 比较与逻辑
# Python 没有 ===；比内容用 ==，比是否同一对象用 is（见 01_list_tuple.py）
print(a > b, a == 10, a != b)
print(True and False, True or False, not True)
print(None is None)  # 判断 None 推荐用 is

# 成员判断（字典/列表里极常用）
keys = ["service", "message"]
print("service" in keys)

# f-string 格式化（项目里大量使用）
file_name = "尺码.txt"
file_size = 12.3456
print(f"文件名:{file_name}")
print(f"大小:{file_size:.2f}KB")   # 保留两位小数，见 app_upload.py

# print 技巧
print("=" * 20)  # 分隔线，见 rag.py 的 print_prompt
