"""迷你知识库 —— 对照 knowledge_base.py 的主流程（无向量库/无 LangChain）。"""

import hashlib
import os

import mini_config as config


def get_string_md5(input_str: str, encoding: str = "utf-8") -> str:
    md5_obj = hashlib.md5()
    md5_obj.update(input_str.encode(encoding))
    return md5_obj.hexdigest()


def check_md5(md5_str: str) -> bool:
    if not os.path.exists(config.md5_path):
        open(config.md5_path, "w", encoding="utf-8").close()
        return False
    with open(config.md5_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() == md5_str:
                return True
    return False


def save_md5(md5_str: str) -> None:
    with open(config.md5_path, "a", encoding="utf-8") as f:
        f.write(md5_str + "\n")


class KnowledgeBaseService:
    def __init__(self):
        os.makedirs(config.persist_directory, exist_ok=True)
        self.store_path = os.path.join(config.persist_directory, "chunks.txt")

    def upload_by_str(self, data: str, filename: str) -> str:
        md5_hex = get_string_md5(data)
        if check_md5(md5_hex):
            return "[Repeat] 内容已存在知识库"

        if len(data) > config.max_spliter_char_number:
            chunks = [data[i:i + config.chunk_size] for i in range(0, len(data), config.chunk_size)]
        else:
            chunks = [data]

        with open(self.store_path, "a", encoding="utf-8") as f:
            for c in chunks:
                f.write(f"{filename}\t{c}\n")

        save_md5(md5_hex)
        return f"[Success] 已写入 {len(chunks)} 段"


if __name__ == "__main__":
    svc = KnowledgeBaseService()
    print(svc.upload_by_str("短文本不切分", "a.txt"))
    print(svc.upload_by_str("短文本不切分", "a.txt"))  # 重复
    print(svc.upload_by_str("这是一段需要被切分的比较长的演示文本ABCDE", "b.txt"))
