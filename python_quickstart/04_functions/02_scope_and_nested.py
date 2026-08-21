"""02 作用域与嵌套函数 —— rag.py 的 __get_chain 里大量内嵌 def。"""

g = "全局"


def outer():
    x = "outer 局部"

    def format_document(docs):
        # 嵌套函数：只在 outer 内部用
        if not docs:
            return "无相关参考资料"
        return " | ".join(docs)

    def format_for_prompt(value: dict) -> dict:
        # 对应 rag.py 的 format_for_prompt_template 思路
        return {
            "input": value["input"]["input"],
            "context": value["context"],
            "history": value["input"]["history"],
        }

    docs = ["资料A", "资料B"]
    print(format_document(docs))
    print(format_document([]))

    packed = {
        "input": {"input": "尺码？", "history": []},
        "context": "身高180推荐L",
    }
    print(format_for_prompt(packed))
    print("能读到:", x, g)


outer()
# format_document(...)  # 外面调用会 NameError
