"""02 继承 —— FileChatMessageHistory 继承 BaseChatMessageHistory 的简化版。"""


class BaseChatMessageHistory:
    """父类：约定子类要有的能力。"""

    def add_messages(self, messages):
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError


class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self, session_id: str):
        self.session_id = session_id
        self._messages = []

    def add_messages(self, messages):
        self._messages.extend(messages)

    def clear(self):
        self._messages = []

    def show(self):
        print(self.session_id, self._messages)


h = FileChatMessageHistory("user_001")
h.add_messages([{"role": "user", "content": "你好"}])
h.show()
h.clear()
h.show()

# isinstance：判断对象是不是某类（或其子类）
print(isinstance(h, FileChatMessageHistory))
print(isinstance(h, BaseChatMessageHistory))
