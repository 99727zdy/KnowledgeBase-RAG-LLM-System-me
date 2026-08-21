"""01 类 / __init__ / self —— 项目里多个 Service 都是这种写法。"""


class KnowledgeBaseService:
    def __init__(self, chunk_size=1000):
        # self.xxx = 实例自己的数据
        self.chunk_size = chunk_size
        self.count = 0

    def upload_by_str(self, data: str, filename: str) -> str:
        self.count += 1
        preview = data[:20]
        return f"[Success] {filename} 已处理，预览={preview}，累计={self.count}"


# 创建实例再调方法（app_upload 里会把实例放进 session_state）
service = KnowledgeBaseService(chunk_size=500)
print(service.chunk_size)
print(service.upload_by_str("流星划过天际", "test.txt"))
print(service.upload_by_str("第二段内容", "test2.txt"))


class VectorStoreService:
    def __init__(self, embedding):
        self.embedding = embedding

    def get_retriever(self):
        return f"retriever(using={self.embedding})"


vs = VectorStoreService(embedding="text-embedding-v4")
print(vs.get_retriever())
