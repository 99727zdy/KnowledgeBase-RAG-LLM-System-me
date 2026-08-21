"""02 循环。"""

# for 遍历序列
messages = [
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "在的"},
]
for msg in messages:
    print(msg["role"], msg["content"])

# range
for i in range(3):
    print("tick", i)  

# enumerate：同时要下标和元素
for i, msg in enumerate(messages):
    print(i, msg["role"], msg["content"])  # 0 user 你好 / 1 assistant 在的

for i, msg in messages:
    print(i, msg)  # role content（解包到的是字典的 key，不是下标）

# for i, msg in messages:
#     print(i, msg["role"])  # 会报错：msg 已是字符串 "content"

for i in messages:
    print(i)  # {'role': 'user', 'content': '你好'} {'role': 'assistant', 'content': '在的'}

# while
n = 0
while n < 3:
    print("while", n)
    n += 1

# break / continue
for i in range(5):
    if i == 1:
        continue  # 跳过本次
    if i == 4:
        break     # 结束循环
    print("loop", i)

# 遍历文件行的直觉（knowledge_base.check_md5）
fake_lines = ["aaa\n", "bbb\n", "ccc\n"]
target = "bbb"
found = False
for line in fake_lines:
    if line.strip() == target:
        found = True
        break #结束整个for循环
print("找到了" if found else "没找到")
