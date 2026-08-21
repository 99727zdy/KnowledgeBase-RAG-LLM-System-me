"""01 函数定义与返回值。"""


def get_string_md5_demo(text: str, encoding: str = "utf-8") -> str:
    """模拟 knowledge_base.get_string_md5 的函数形态（此处不做真 MD5）。"""
    # 默认参数 encoding="utf-8"
    return f"md5({text}|{encoding})"


def check_exists(item, pool):
    """多返回值也可以，这里返回 bool。"""
    return item in pool


def split_or_keep(data: str, max_len: int = 1000):
    """对应 upload_by_str：超长才切分。"""
    if len(data) > max_len:
        # 简化：按句号硬切演示
        return data.split("。")
    return [data]


print(get_string_md5_demo("流星"))
print(check_exists("abc", {"abc", "xyz"}))
print(split_or_keep("短文本"))
print(split_or_keep("第一句。第二句。第三句。", max_len=5))


# *args / **kwargs（了解即可）
def log_event(event, *args, **kwargs):
    print("event:", event)
    print("args:", args)
    print("kwargs:", kwargs)


log_event("upload", "file.txt", size=12, ok=True)
