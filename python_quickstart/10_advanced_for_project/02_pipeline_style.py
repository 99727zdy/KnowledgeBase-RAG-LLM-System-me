"""02 管道式写法 —— 帮助读懂 rag.py 里 A | B | C 的数据流向。

注意：LangChain 的 | 是库重载后的「链接」，不是普通整数按位或。
这里用纯函数模拟「左边输出进右边」。
"""


def format_for_retriever(value: dict) -> str:
    return value["input"]


def fake_retriever(query: str) -> list[str]:
    return [f"资料: 与「{query}」相关的尺码建议"]


def format_document(docs: list[str]) -> str:
    if not docs:
        return "无相关参考资料"
    return "\n".join(docs)


def fake_prompt(context: str, user_input: str) -> str:
    return f"参考:{context}\n问题:{user_input}"


def fake_llm(prompt: str) -> str:
    return f"回答 >>> 基于资料回复：……（prompt长度={len(prompt)}）"


def pipe(data, *steps):
    """手动管道：把 data 依次送进每个 step。"""
    for step in steps:
        data = step(data)
    return data


user_payload = {"input": "身高180穿什么码"}

# 拆开看每一步
q = format_for_retriever(user_payload)
docs = fake_retriever(q)
ctx = format_document(docs)
prompt = fake_prompt(ctx, q)
answer = fake_llm(prompt)
print(answer)

# 等价「管道」写法
answer2 = pipe(
    user_payload,
    format_for_retriever,
    fake_retriever,
    format_document,
    lambda ctx: fake_prompt(ctx, user_payload["input"]),
    fake_llm,
)
print(answer2)

print("读 rag.py 时记住：左边的输出 = 右边的输入")
