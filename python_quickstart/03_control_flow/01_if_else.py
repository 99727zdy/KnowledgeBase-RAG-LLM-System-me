"""01 条件判断。"""

size = 1200
max_size = 1000

if size > max_size:
    print("需要切分")
elif size == max_size:
    print("刚好边界")
else:
    print("整段入库")

# 真值判断：空字符串/空列表/None/0 都是 False
data = ""
if not data:
    print("无内容")

# 常见写法：先算再判断（类似 if err）
md5 = "abc"
seen = {"abc", "xyz"}
if md5 in seen:
    print("[Repeat] 内容已存在知识库")
else:
    print("[Success] 可以入库")

# 三元表达式（了解）
label = "长文本" if size > max_size else "短文本"
print(label)
