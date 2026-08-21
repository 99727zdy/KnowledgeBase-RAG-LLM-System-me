"""02 配置风格 —— 对照 config_data.py：用模块级变量当配置。

真实项目里是：
  import config_data as config
  config.chunk_size
"""

# ===== 下面就像一个迷你 config_data =====
md5_path = "./md5.text"
persist_directory = "./chroma_db"
chunk_size = 1000
chunk_overlap = 100
similarity_threshold = 1
embedding_model_name = "text-embedding-v4"
chat_model_name = "qwen3-max"

session_config = {
    "configurable": {
        "session_id": "user_001",
    }
}
# ===== 配置结束 =====


def demo_use_config():
    # 同文件内直接用；跨文件则 import 本模块 as config
    print("切分大小:", chunk_size)
    print("会话ID:", session_config["configurable"]["session_id"])
    print("嵌入模型:", embedding_model_name)


if __name__ == "__main__":
    demo_use_config()
