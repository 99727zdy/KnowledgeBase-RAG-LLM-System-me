"""03 字节与编解码 —— 上传文件、MD5 都会用到。

本项目对应：
- app_upload.py: uploader_file.getvalue().decode("utf-8")
- knowledge_base.py: input_str.encode(encoding=encoding)
"""

text = "流星"
# str -> bytes
data = text.encode("utf-8")   # 将字符串转换为字节串  编码
print(type(data), data) # <class 'bytes'> b'\xe6\xb5\x81\xe6\x98\x9f' b 表示这是 bytes（字节串）

# bytes -> str
back = data.decode("utf-8")   # 将字节串转换为字符串  解码
print(type(back), back)

# 模拟上传：网页拿到的是字节，入库前要解码成字符串
fake_upload_bytes = "衣物尺码表".encode("utf-8")
content = fake_upload_bytes.decode("utf-8")
print("入库文本:", content)

# 注意：hashlib.md5 需要的是 bytes，不是 str
need_bytes = content.encode("utf-8")
print("给 MD5 用的字节长度:",need_bytes,len(need_bytes)) 
