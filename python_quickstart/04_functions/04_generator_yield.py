"""04 生成器与 yield —— 读懂 app_chat 流式输出的关键。

对应 app_chat.py:

    def capture(generator, cache_list):
        for chunk in generator:
            cache_list.append(chunk)
            yield chunk
"""


def fake_llm_stream():
    """模拟模型流式返回一个个片段。"""
    for piece in ["你", "好", "，", "请", "问", "身高"]:
        yield piece


def capture(generator, cache_list):
    """边输出边缓存，最后可拼完整答案。"""
    for chunk in generator:
        cache_list.append(chunk)
        yield chunk


# 普通 for 消费生成器
print("直接流式:")
for c in fake_llm_stream():
    print(c, end="")
print()

# 对照聊天页：一边展示一边收集
ai_res_list = []
print("capture 后:")
for c in capture(fake_llm_stream(), ai_res_list):
    print(c, end="")
print()
print("完整回复:", "".join(ai_res_list))

# 生成器特点：惰性、可迭代一次
g = fake_llm_stream()
print(next(g), next(g))
