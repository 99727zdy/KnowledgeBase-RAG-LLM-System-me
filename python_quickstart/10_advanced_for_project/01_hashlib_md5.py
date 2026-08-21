"""01 hashlib 与 MD5 —— 对照 knowledge_base 去重逻辑。"""

import hashlib


def get_string_md5(input_str: str, encoding: str = "utf-8") -> str:
    str_bytes = input_str.encode(encoding=encoding)
    md5_obj = hashlib.md5()
    md5_obj.update(str_bytes)
    return md5_obj.hexdigest()


def check_md5(md5_str: str, pool: set[str]) -> bool:
    return md5_str in pool


def save_md5(md5_str: str, pool: set[str]) -> None:
    pool.add(md5_str)


seen: set[str] = set()

for text in ["流星", "流星", "流星4"]:
    md5_hex = get_string_md5(text)
    if check_md5(md5_hex, seen):
        print(text, "-> [Repeat] 内容已存在知识库")
    else:
        save_md5(md5_hex, seen)
        print(text, "-> [Success]", md5_hex)

# 同一内容 => 同一 MD5；改一个字 => MD5 全变
print("相同?", get_string_md5("周杰伦") == get_string_md5("周杰伦"))
