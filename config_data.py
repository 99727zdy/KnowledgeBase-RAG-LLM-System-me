







md5_path = "./md5.text"  # 已入库文本的 MD5 记录文件；上传时先算哈希，已存在则跳过，避免重复入库

collection_name = "rag"  # 向量库集合名；原先给 Chroma 用，当前 JSON 向量库暂未读取，可先保留
persist_directory = "./chroma_db"  # 向量库本地目录；上传和问答共用，当前会在其中生成 store.json

chunk_size = 1000  # 每段文本最多保留多少字符；越大上下文越完整，但嵌入和检索更贵、更慢
chunk_overlap = 100  # 相邻两段重叠多少字符；避免一句话被从中间切断后检索不到
separators = ["\n\n", "\n", ".", "!", "?", "。", "！", "？", " ", ""]  # 切分优先按这些符号断开；空字符串表示硬切

max_spliter_char_number = 1000  # 超过这个长度才真正切分；短于它的文件整段入库

similarity_threshold = 1  # 每次提问从向量库取最相似的文档条数；1 表示只取最相关的 1 段

embedding_model_name = "text-embedding-v4"  # 文本转向量的嵌入模型（DashScope）；上传和检索必须用同一个
chat_model_name = "qwen3-max"  # 最终回答用户问题的对话模型（通义千问）

session_config = {  # LangChain 会话配置；RunnableWithMessageHistory 靠 session_id 区分对话
    "configurable": {
        "session_id": "user_001",  # 当前写死为一个用户；多用户时需改成每人不同的 id
    }
}
