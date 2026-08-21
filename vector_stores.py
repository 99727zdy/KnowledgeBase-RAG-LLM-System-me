import os
from langchain_core.vectorstores import InMemoryVectorStore
import config_data as config


def _store_path():
    return os.path.join(config.persist_directory, "store.json")


def get_vector_store(embedding):
    """加载或新建本地向量库。

    Python 3.13 + Windows 下 chromadb 写入会原生崩溃（access violation），
    因此改用 LangChain 自带的 InMemoryVectorStore 并持久化到 JSON。
    """
    os.makedirs(config.persist_directory, exist_ok=True)
    path = _store_path()
    if os.path.exists(path) and os.path.getsize(path) > 0:
        return InMemoryVectorStore.load(path, embedding)
    return InMemoryVectorStore(embedding=embedding)


def save_vector_store(store):
    os.makedirs(config.persist_directory, exist_ok=True)
    store.dump(_store_path())


class VectorStoreService(object):
    def __init__(self, embedding):
        """
        :param embedding: 嵌入模型的传入
        """
        self.embedding = embedding
        self.vector_store = get_vector_store(embedding)

    def get_retriever(self):
        """返回向量检索器，方便加入chain"""
        return self.vector_store.as_retriever(search_kwargs={"k": config.similarity_threshold})


if __name__ == "__main__":
    from langchain_community.embeddings import DashScopeEmbeddings
    retriever = VectorStoreService(DashScopeEmbeddings(model="text-embedding-v4")).get_retriever()

    res = retriever.invoke("我的身高180，尺码推荐")
    print(res)
