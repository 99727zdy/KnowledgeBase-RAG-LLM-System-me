"""01 类型提示 —— 能看懂即可，运行不依赖它们。

项目中常见：
  def check_md5(md5_str: str)
  knowledge_chunks: list[str]
  def add_messages(...) -> None
"""

from typing import Sequence


def check_md5(md5_str: str) -> bool:
    return len(md5_str) == 32


def upload(data: str, filename: str) -> str:
    return f"{filename}:{len(data)}"


def add_messages(messages: Sequence[dict]) -> None:
    # Sequence：list / tuple 等能迭代的序列都行
    for m in messages:
        print(m)


chunks: list[str] = ["a", "b"]
print(check_md5("a" * 32))
print(upload("hello", "a.txt"))
add_messages([{"role": "user", "content": "hi"}])

# Python 不会因为注解写错类型就报错（除非你另装检查工具）
x: int = "其实是字符串"  # 运行没问题，只是提示不严谨
print(x)
