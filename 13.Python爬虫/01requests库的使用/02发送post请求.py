import requests

url = "http://httpbin.org/post"
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
	'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
}
data = {
    "username":"zhiliao",
    "password": "111111"
}

resp = requests.post(url=url,data=data,headers=headers)
print(resp.text)