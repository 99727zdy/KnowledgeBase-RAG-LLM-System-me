"""01 文件读写 —— with open 是项目标准写法。

对应：
- knowledge_base.save_md5 / check_md5
- file_history_store 读写历史
"""

from pathlib import Path

demo = Path(__file__).with_name("_demo_md5.txt")

# 写入（追加）
with open(demo, "a", encoding="utf-8") as f:
    f.write("aaa\n")
    f.write("bbb\n")

# 读取并逐行处理
with open(demo, "r", encoding="utf-8") as f:
    for line in f:
        print(repr(line), "->", line.strip())

# 覆盖写入
with open(demo, "w", encoding="utf-8") as f:
    f.write("only-one\n")

print("文件内容:", demo.read_text(encoding="utf-8"))

# 清理演示文件（可选）
demo.unlink(missing_ok=True)
