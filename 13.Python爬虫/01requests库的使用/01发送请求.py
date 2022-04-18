

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

params = {
    "kw": "python"
}

resp = requests.get("https://www.baidu.com",headers=headers,params=params)
# print(type(resp.text))
# print(type(resp.content))
# 在网页传输过程中，都是bytes类型。resp.content是bytes类型，没有经过任何处理的
# resp.text：是requests库经过猜测resp.content的编码类型，然后自己提前解码后的

# print(resp.url)
# print(resp.encoding)
# 200：状态码代表请求正常
print(resp.status_code)