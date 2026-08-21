"""迷你历史记录 —— 对照 file_history_store.py。"""

import json
import os
from typing import Sequence


class FileChatMessageHistory:
    def __init__(self, session_id: str, storage_path: str = "./_mini_chat_history"):
        self.session_id = session_id
        self.file_path = os.path.join(storage_path, session_id)
        os.makedirs(storage_path, exist_ok=True)

    def add_messages(self, messages: Sequence[dict]) -> None:
        all_messages = list(self.messages)
        all_messages.extend(messages)
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(all_messages, f, ensure_ascii=False)

    @property
    def messages(self) -> list[dict]:
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def clear(self) -> None:
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([], f)


def get_history(session_id: str) -> FileChatMessageHistory:
    return FileChatMessageHistory(session_id)


if __name__ == "__main__":
    h = get_history("user_001")
    h.add_messages([{"role": "user", "content": "你好"}])
    h.add_messages([{"role": "assistant", "content": "在的"}])
    print(h.messages)
    h.clear()
    print("清空后:", h.messages)
