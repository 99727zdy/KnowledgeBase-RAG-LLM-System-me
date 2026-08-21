"""03 集合 —— 基础补齐；本项目用得少，入门知道即可。"""

tags = {"rag", "python", "langchain"}
tags.add("streamlit")
tags.add("rag")  # 重复无效
print(tags)

a = {1, 2, 3, 3}
print(a)  # {1, 2, 3} 重复的元素会被自动去重
b = {2, 3, 4}
print(a & b)  # 交集
print(a | b)  # 并集
print(a - b)  # 差集

# 去重小技巧
nums = [1, 2, 2, 3, 1]
print(set(nums))  # {1, 2, 3}
print(list(set(nums)))  # [1, 2, 3]

# 注意：
# 1) 集合无序：没有固定下标，list(set(...)) 去重后顺序可能变化
# 2) 元素须可哈希：数字/字符串/元组可以；list、dict 可变，不能直接放进 set
ok = {1, "a", (1, 2)}  # OK：int、str、tuple 都可以
print(ok)

# 下面两行如果取消注释会报 TypeError，仅作说明：
# {[1, 2]}      # 报错：list 不能放进 set
# {{"k": 1}}    # 报错：dict 不能放进 set