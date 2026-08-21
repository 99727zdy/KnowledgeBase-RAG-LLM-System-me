"""03 @property —— 把方法当成属性来访问。

对应 file_history_store.py:

    @property
    def messages(self) -> list[BaseMessage]:
        ...
"""


class FileChatMessageHistory:
    def __init__(self):
        self._raw = [
            {"role": "user", "content": "你好"},
            {"role": "assistant", "content": "在的"},
        ]

    @property
    def messages(self):
        """外面用 hist.messages，而不是 hist.messages()。"""
        return list(self._raw)

    def add_messages(self, new_msgs):
        # 先读已有（走 property），再合并写回
        all_msgs = list(self.messages)
        all_msgs.extend(new_msgs)
        self._raw = all_msgs


hist = FileChatMessageHistory()
print(hist.messages)  # 注意：没有括号
hist.add_messages([{"role": "user", "content": "尺码？"}])
print(hist.messages)
