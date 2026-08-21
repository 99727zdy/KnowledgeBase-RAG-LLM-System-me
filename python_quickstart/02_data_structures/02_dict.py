"""02 字典 —— 本项目最高频结构之一。

对应：
- metadata = {"source": ..., "create_time": ...}
- st.session_state["message"]
- session_config["configurable"]["session_id"]
- rag.py 里 value["input"]["input"]
"""

# 创建与读写
user = {"name": "小明", "role": "user"}
print(user["name"])
user["content"] = "你好"
print(user)

# 安全取值
print(user.get("age"))          # None，不报错
# print(user["age"])              # KeyError，报错    
print(user.get("age", 18))      # 默认值

# in 判断（app_upload / app_chat 里大量出现）
session_state = {}
if "service" not in session_state:
    session_state["service"] = "KnowledgeBaseService()"
print(session_state)

# 嵌套字典（务必会读）
session_config = {
    "configurable": {
        "session_id": "user_001",
    }
}
print(session_config["configurable"]["session_id"])

# 遍历
for k, v in user.items():
    print(k, "=>", v)

# 消息列表：list[dict]（app_chat 的核心状态）
messages = [
    {"role": "assistant", "content": "你好"},
    {"role": "user", "content": "尺码怎么选"},
]
messages.append({"role": "assistant", "content": "请告诉身高体重"})
print(messages)
