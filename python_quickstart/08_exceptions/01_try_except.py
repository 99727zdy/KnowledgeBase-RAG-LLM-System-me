"""01 try / except —— 上传失败、JSON 损坏时的保护。

对应：
- app_upload.py: except Exception as e
- file_history_store.py: except (FileNotFoundError, json.JSONDecodeError)
"""

import json
from pathlib import Path

path = Path(__file__).with_name("_broken.json")


def load_messages(file_path: Path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # 文件不存在或内容坏了：返回空列表，避免崩溃
        return []
    finally:
        # 无论成功失败都会走这里（了解即可）
        pass


print("文件不存在时:", load_messages(path))

path.write_text("{not-json", encoding="utf-8")
print("JSON 损坏时:", load_messages(path))

path.write_text('[{"role":"user","content":"hi"}]', encoding="utf-8")
print("正常时:", load_messages(path))

# 业务层常见：捕获后给用户看错误信息
try:
    raise RuntimeError("嵌入模型调用失败")
except Exception as e:
    print(f"入库失败：{e}")

path.unlink(missing_ok=True)
