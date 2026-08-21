"""02 路径与 os —— 向量库目录、历史目录都会用到。"""

import os

persist_directory = "./chroma_db_demo"
session_id = "user_001"
storage_path = "./chat_history_demo"

# 拼接路径（跨平台更安全）
store_path = os.path.join(persist_directory, "store.json")
history_path = os.path.join(storage_path, session_id)
print(store_path)
print(history_path)

# 目录不存在就创建（exist_ok=True：已存在不报错）
os.makedirs(persist_directory, exist_ok=True)
os.makedirs(storage_path, exist_ok=True)

print("存在?", os.path.exists(persist_directory))
print("是目录?", os.path.isdir(persist_directory))

# 写个空文件演示 getsize
with open(store_path, "w", encoding="utf-8") as f:
    f.write("")

print("大小:", os.path.getsize(store_path))  # vector_stores 会判断 > 0 才 load

# 清理演示
os.remove(store_path)
os.rmdir(persist_directory)
os.rmdir(storage_path)
