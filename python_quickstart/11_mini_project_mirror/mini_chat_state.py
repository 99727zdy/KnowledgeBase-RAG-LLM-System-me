"""迷你聊天状态 —— 对照 app_chat.py 的 session_state 字典思路（无 Streamlit）。"""

from mini_history import get_history


session_state = {
    "message": [{"role": "assistant", "content": "你好，有什么可以帮助你？"}],
}


def render(messages):
    for m in messages:
        print(f"[{m['role']}] {m['content']}")


def fake_stream_answer(prompt: str):
    for piece in ["根据", "资料：", "推荐 L 码"]:
        yield piece


def handle_user_input(prompt: str):
    session_state["message"].append({"role": "user", "content": prompt})

    # 同步写入「文件历史」（简化版）
    hist = get_history("user_001")
    hist.add_messages([{"role": "user", "content": prompt}])

    ai_res_list = []
    for chunk in fake_stream_answer(prompt):
        ai_res_list.append(chunk)
        print(chunk, end="")
    print()

    full = "".join(ai_res_list)
    session_state["message"].append({"role": "assistant", "content": full})
    hist.add_messages([{"role": "assistant", "content": full}])


if __name__ == "__main__":
    print("=== 初始页面 ===")
    render(session_state["message"])

    print("\n=== 用户提问后 ===")
    handle_user_input("身高180穿什么")
    render(session_state["message"])
