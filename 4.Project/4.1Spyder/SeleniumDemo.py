# 1.导入web驱动模块
from selenium import webdriver

# 2.创建Chrome驱动
driver = webdriver.Chrome()
# 3.发送请求
driver.get("https://www.baidu.com")
# 4.获取输入框
input = driver.find_element_by_css_selector('#kw')
# 5.输入搜索关键字
input.send_keys("廖雪峰")
# 6.获取提交按钮
button = driver.find_element_by_css_selector('#su')
# 7.提交文件
button.click()
