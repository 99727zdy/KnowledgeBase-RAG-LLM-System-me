"""04 推导式 —— 项目里真实出现过。

对应 knowledge_base.py:
  metadatas=[metadata for _ in knowledge_chunks]

对应 file_history_store.py:
  new_messages=[message_to_dict(message) for message in all_messages]
"""

chunks = ["段a", "段b", "段c"] # 列表
metadata = {"source": "demo.txt", "operator": "客户"} # 字典

# 列表推导：为每一段复制同一份 metadata
metadatas = [metadata for _ in chunks]
print(metadatas)  # [{'source': 'demo.txt', 'operator': '客户'}, {'source': 'demo.txt', 'operator': '客户'}, {'source': 'demo.txt', 'operator': '客户'}]

# 带变换
upper_chunks = [c.upper() for c in chunks]
print(upper_chunks)

# 带过滤
nums = [1, 2, 3, 4, 5]
evens = [n for n in nums if n % 2 == 0]
print(evens)

# 字典推导
roles = ["user", "assistant"]
role_map = {r: len(r) for r in roles}
print(role_map)
