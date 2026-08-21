"""03 lambda 与可调用对象 —— 链里常把函数当参数传递。"""


def apply(func, value):
    """接收一个可调用对象。"""
    return func(value)


def double(x):
    return x * 2


print(apply(double, 5))

# lambda：一次性小函数
print(apply(lambda x: x + 1, 5))

# 管道直觉：一步步往下传（下一章生成器 + 10_项目进阶会继续）
def step1(x):
    return x.strip()


def step2(x):
    return x.upper()


text = "  hello  "
result = step2(step1(text))
print(result)

# 函数本身可以放进变量/字典
ops = {
    "upper": str.upper,
    "lower": str.lower,
}
print(ops["upper"]("rag"))
