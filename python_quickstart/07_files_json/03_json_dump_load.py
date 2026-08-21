"""03 JSON 读写 —— 对照 file_history_store / store.json。"""

import json
from pathlib import Path

path = Path(__file__).with_name("_demo_history.json")

messages = [
    {"type": "human", "content": "你好"},
    {"type": "ai", "content": "在的，请问尺码？"},
]

# 写入
with open(path, "w", encoding="utf-8") as f:
    json.dump(messages, f, ensure_ascii=False, indent=2)

# 读取
with open(path, "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded)
print(type(loaded), type(loaded[0]))

# 清空（clear 的简化）
with open(path, "w", encoding="utf-8") as f:
    json.dump([], f)

path.unlink(missing_ok=True)
