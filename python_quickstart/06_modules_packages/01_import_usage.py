"""01 导入用法与 __name__。

本项目常见写法：
  import config_data as config
  from vector_stores import get_vector_store
"""

import math
import os.path as osp  # as 起别名

from datetime import datetime

print(math.sqrt(16))
print(osp.join("chroma_db", "store.json"))
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def main():
    print("作为脚本直接运行时才会进这里")


# 关键模块被别人 import 时，下面不会执行；直接 python 本文件时会执行
if __name__ == "__main__":
    main()
